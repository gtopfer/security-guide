#!/usr/bin/env python3
"""Coleta básica de informações para um alvo (domínio ou IP)."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import ipaddress
import json
import re
import socket
import ssl
import http.client
import urllib.request
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Iterable, List, Optional, Tuple, Union

DEFAULT_PORTS = [22, 80, 443, 8080, 8443]
DEFAULT_MAX_WORKERS = 16
WHOIS_SERVERS = ["whois.iana.org", "whois.verisign-grs.com"]
HTTP_BODY_PREVIEW_LIMIT = 10000
HTTP_BODY_PREVIEW_SNIPPET = 800

_WHOIS_CACHE: Dict[str, str] = {}


def sanitize_filename(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", value)


def _infer_family(ip: str) -> socket.AddressFamily:
    try:
        parsed = ipaddress.ip_address(ip)
        return socket.AF_INET6 if parsed.version == 6 else socket.AF_INET
    except ValueError:
        return socket.AF_INET6 if ":" in ip else socket.AF_INET


def _prepare_endpoint(ip: str, port: int) -> Tuple[socket.AddressFamily, Tuple[object, ...]]:
    family = _infer_family(ip)
    if family == socket.AF_INET6:
        return family, (ip, port, 0, 0)
    return family, (ip, port)


def _persist_artifact(base_dir: Path, filename: str, data: Union[str, bytes], binary: bool = False) -> str:
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / filename
    if binary:
        with path.open("wb") as handle:
            handle.write(data)  # type: ignore[arg-type]
    else:
        with path.open("w", encoding="utf-8") as handle:
            handle.write(str(data))
    return str(path)


def _highlight_headers(headers: Dict[str, str]) -> Dict[str, str]:
    lowercase = {k.lower(): v for k, v in headers.items()}
    interesting = ["server", "x-powered-by", "via", "content-type"]
    return {key: lowercase[key] for key in interesting if key in lowercase}


def _format_x509_name(raw: Tuple[Tuple[Tuple[str, str], ...], ...]) -> str:
    return ", ".join(f"{k}={v}" for part in raw for k, v in part)


def fetch_http_body(host: str, use_https: bool, timeout: float, user_agent: str) -> Optional[str]:
    scheme = "https" if use_https else "http"
    url = f"{scheme}://{host}/"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(HTTP_BODY_PREVIEW_LIMIT)
            return data.decode("utf-8", errors="ignore")
    except Exception:
        return None


def resolve_dns(target: str) -> Dict[str, List[str]]:
    records = {"ipv4": [], "ipv6": []}
    try:
        infos = socket.getaddrinfo(target, None)
    except socket.gaierror:
        return records

    for family, _, _, _, sockaddr in infos:
        ip = sockaddr[0]
        if ":" in ip:
            records["ipv6"].append(ip)
        else:
            records["ipv4"].append(ip)

    records["ipv4"] = sorted(set(records["ipv4"]))
    records["ipv6"] = sorted(set(records["ipv6"]))
    return records


def _try_connect(ip: str, port: int, timeout: float) -> Optional[Dict[str, str]]:
    family, address = _prepare_endpoint(ip, port)
    sock = socket.socket(family, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect(address)
    except (socket.error, OSError):
        return None
    finally:
        sock.close()
    return {
        "ip": ip,
        "port": port,
        "family": "ipv6" if family == socket.AF_INET6 else "ipv4",
    }


def check_ports(
    addresses: Iterable[str],
    ports: Iterable[int],
    timeout: float = 2.0,
    workers: int = DEFAULT_MAX_WORKERS,
) -> List[Dict[str, str]]:
    openings: List[Dict[str, str]] = []
    targets = [(ip, port) for ip in addresses for port in ports]
    if not targets:
        return openings

    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {
            executor.submit(_try_connect, ip, port, timeout): (ip, port)
            for ip, port in targets
        }
        for future in as_completed(future_map):
            result = future.result()
            if result:
                openings.append(result)
    return openings


def http_metadata(host: str, use_https: bool, timeout: float, user_agent: str) -> Optional[Dict[str, object]]:
    conn: http.client.HTTPConnection
    certificate_pem: Optional[str] = None
    tls_info: Dict[str, Optional[str]] = {}
    try:
        if use_https:
            context = ssl.create_default_context()
            conn = http.client.HTTPSConnection(host, timeout=timeout, context=context)
        else:
            conn = http.client.HTTPConnection(host, timeout=timeout)
        headers = {"User-Agent": user_agent}
        conn.request("HEAD", "/", headers=headers)
        resp = conn.getresponse()
        resp_headers = {k: v for k, v in resp.getheaders()}
        if use_https and isinstance(conn, http.client.HTTPSConnection):
            try:
                ssl_sock = conn.sock  # type: ignore[attr-defined]
                if ssl_sock is not None:
                    der_cert = ssl_sock.getpeercert(True)
                    certificate_pem = ssl.DER_cert_to_PEM_cert(der_cert)
                    fingerprint = hashlib.sha256(der_cert).hexdigest()
                    tls_info = {
                        "fingerprint_sha256": fingerprint,
                        "protocol": getattr(ssl_sock, "version", lambda: None)(),
                    }
                    cipher_info = getattr(ssl_sock, "cipher", lambda: None)()
                    if cipher_info:
                        tls_info["cipher"] = cipher_info[0]
                    cert_dict = ssl_sock.getpeercert()
                    if cert_dict:
                        issuer = cert_dict.get("issuer")
                        subject = cert_dict.get("subject")
                        if issuer:
                            tls_info["issuer"] = _format_x509_name(tuple(issuer))
                        if subject:
                            tls_info["subject"] = _format_x509_name(tuple(subject))
                        if cert_dict.get("notAfter"):
                            tls_info["not_after"] = cert_dict["notAfter"]
            except Exception:
                pass
        data: Dict[str, object] = {
            "scheme": "https" if use_https else "http",
            "status": resp.status,
            "reason": resp.reason,
            "headers": resp_headers,
            "highlights": _highlight_headers(resp_headers),
        }
        if tls_info:
            data["tls"] = {k: v for k, v in tls_info.items() if v}
        if certificate_pem:
            data["tls_certificate_pem"] = certificate_pem
        return data
    except Exception:
        return None
    finally:
        try:
            conn.close()
        except Exception:
            pass


def fetch_robots(host: str, use_https: bool, timeout: float, user_agent: str) -> Optional[str]:
    scheme = "https" if use_https else "http"
    url = f"{scheme}://{host}/robots.txt"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": user_agent})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8", errors="ignore")
            return data[:5000]
    except Exception:
        return None


def whois_lookup(target: str) -> Optional[str]:
    cached = _WHOIS_CACHE.get(target)
    if cached:
        return cached

    servers = list(WHOIS_SERVERS)
    visited = set()
    while servers:
        server = servers.pop(0)
        if server in visited:
            continue
        visited.add(server)
        for _ in range(2):
            try:
                with socket.create_connection((server, 43), timeout=5) as sock:
                    query = f"{target}\r\n".encode()
                    sock.sendall(query)
                    response = sock.recv(65535)
                    data = response.decode("utf-8", errors="ignore")
                    refer = next(
                        (
                            line.split(":", 1)[1].strip()
                            for line in data.splitlines()
                            if line.lower().startswith("refer:")
                        ),
                        None,
                    )
                    if refer and refer not in visited:
                        servers.insert(0, refer)
                    _WHOIS_CACHE[target] = data
                    return data
            except Exception:
                continue
    return None


def collect(
    target: str,
    ports: List[int],
    tcp_timeout: float,
    http_timeout: float,
    user_agent: str,
    workers: int,
    enable_http: bool,
    enable_whois: bool,
    artifacts_dir: Optional[Path],
) -> Dict[str, object]:
    dns_info = resolve_dns(target)
    addresses = dns_info.get("ipv4", []) + dns_info.get("ipv6", [])
    safe_target = sanitize_filename(target)
    artifact_paths: List[str] = []

    def record_artifact(suffix: str, data: Union[str, bytes], binary: bool = False) -> None:
        if artifacts_dir is None or data is None:
            return
        path = _persist_artifact(artifacts_dir, f"{safe_target}_{suffix}", data, binary)
        artifact_paths.append(path)

    http_https: Optional[Dict[str, object]] = None
    robots = None
    http_body_preview = None
    if enable_http:
        http_https = http_metadata(target, True, http_timeout, user_agent) or http_metadata(
            target, False, http_timeout, user_agent
        )
        schemes_to_try = [True, False]
        if http_https:
            main_is_https = http_https.get("scheme") == "https"
            schemes_to_try = [main_is_https, not main_is_https]
            certificate_pem = http_https.pop("tls_certificate_pem", None)
            if certificate_pem:
                record_artifact(f"{http_https['scheme']}_cert.pem", certificate_pem)
        for use_https in schemes_to_try:
            if robots:
                break
            candidate = fetch_robots(target, use_https, http_timeout, user_agent)
            if candidate:
                robots = candidate
                record_artifact(f"{'https' if use_https else 'http'}_robots.txt", candidate)
        body_scheme = None
        for use_https in schemes_to_try:
            if http_body_preview:
                break
            body = fetch_http_body(target, use_https, http_timeout, user_agent)
            if body:
                http_body_preview = body[:HTTP_BODY_PREVIEW_SNIPPET]
                body_scheme = "https" if use_https else "http"
                record_artifact(f"{body_scheme}_root.html", body)
        if http_body_preview:
            if http_https:
                http_https["body_preview"] = http_body_preview
            else:
                http_https = {"scheme": body_scheme or "https", "body_preview": http_body_preview}
    whois_data = whois_lookup(target) if enable_whois else None
    open_ports = check_ports(addresses, ports, tcp_timeout, workers)

    return {
        "target": target,
        "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "dns": dns_info,
        "http": http_https,
        "robots_txt": robots,
        "open_ports": open_ports,
        "whois_raw": whois_data,
        "artifacts_saved": artifact_paths,
    }


def parse_ports(raw: Optional[str]) -> List[int]:
    if not raw:
        return DEFAULT_PORTS
    ports = []
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            ports.append(int(chunk))
        except ValueError:
            raise argparse.ArgumentTypeError(f"Porta inválida: {chunk}")
    return sorted(set(port for port in ports if 0 < port < 65536))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Coleta OSINT básica para domínio ou IP")
    parser.add_argument("--target", required=True, help="Domínio ou endereço IP a ser analisado")
    parser.add_argument("--out", help="Arquivo de saída (JSON). Se omitido, imprime no stdout")
    parser.add_argument("--ports", help="Lista de portas TCP separadas por vírgula (padrão: 22,80,443,8080,8443)")
    parser.add_argument("--tcp-timeout", type=float, default=2.0, help="Timeout em segundos para conexão TCP (padrão: 2s)")
    parser.add_argument("--http-timeout", type=float, default=5.0, help="Timeout em segundos para requisições HTTP/HTTPS (padrão: 5s)")
    parser.add_argument("--workers", type=int, default=DEFAULT_MAX_WORKERS, help="Número máximo de threads para varredura de portas")
    parser.add_argument("--user-agent", default="EstudosGT-OSINT/1.0", help="User-Agent utilizado nas requisições HTTP")
    parser.add_argument("--disable-http", action="store_true", help="Pular coleta HTTP/HTTPS (HEAD e robots.txt)")
    parser.add_argument("--disable-whois", action="store_true", help="Pular consulta WHOIS")
    parser.add_argument("--artifacts-dir", help="Diretório para salvar artefatos crus (HTML, robots.txt, certificados)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ports = parse_ports(args.ports)
    artifacts_dir = Path(args.artifacts_dir).expanduser() if args.artifacts_dir else None
    result = collect(
        target=args.target,
        ports=ports,
        tcp_timeout=args.tcp_timeout,
        http_timeout=args.http_timeout,
        user_agent=args.user_agent,
        workers=max(1, args.workers),
        enable_http=not args.disable_http,
        enable_whois=not args.disable_whois,
        artifacts_dir=artifacts_dir,
    )
    payload = json.dumps(result, indent=2, ensure_ascii=False)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(payload, encoding="utf-8")
        print(f"[+] Resultado salvo em {out_path}")
    else:
        print(payload)


if __name__ == "__main__":
    main()
