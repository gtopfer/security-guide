import argparse
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.append(str(SCRIPTS_DIR))

spec = importlib.util.spec_from_file_location("osint_collector", SCRIPTS_DIR / "osint_collector.py")
osint_collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(osint_collector)  # type: ignore[arg-type]


def test_parse_ports_handles_duplicates_and_whitespace():
    assert osint_collector.parse_ports("80, 443,80,22") == [22, 80, 443]


def test_parse_ports_raises_for_invalid_value():
    with pytest.raises(argparse.ArgumentTypeError):
        osint_collector.parse_ports("abc,10")


def test_collect_records_artifacts_and_enriches_data(monkeypatch, tmp_path):
    def fake_resolve_dns(target):
        return {"ipv4": ["1.1.1.1"], "ipv6": ["2001:db8::1"]}

    def fake_http_metadata(*args, **kwargs):
        return {
            "scheme": "https",
            "status": 200,
            "reason": "OK",
            "headers": {"Server": "test"},
            "highlights": {"server": "test"},
            "tls_certificate_pem": "-----BEGIN CERT-----\nabc\n-----END CERT-----",
        }

    def fake_fetch_robots(*args, **kwargs):
        return "User-agent: *"

    def fake_fetch_http_body(*args, **kwargs):
        return "<html>hello</html>"

    def fake_whois(target):
        return "whois"

    def fake_check_ports(*args, **kwargs):
        return [{"ip": "1.1.1.1", "port": 80, "family": "ipv4"}]

    monkeypatch.setattr(osint_collector, "resolve_dns", fake_resolve_dns)
    monkeypatch.setattr(osint_collector, "http_metadata", fake_http_metadata)
    monkeypatch.setattr(osint_collector, "fetch_robots", fake_fetch_robots)
    monkeypatch.setattr(osint_collector, "fetch_http_body", fake_fetch_http_body)
    monkeypatch.setattr(osint_collector, "whois_lookup", fake_whois)
    monkeypatch.setattr(osint_collector, "check_ports", fake_check_ports)

    result = osint_collector.collect(
        target="example.com",
        ports=[80],
        tcp_timeout=1.0,
        http_timeout=1.0,
        user_agent="agent",
        workers=1,
        enable_http=True,
        enable_whois=True,
        artifacts_dir=tmp_path,
    )

    assert result["http"]["body_preview"].startswith("<html>")
    assert result["robots_txt"] == "User-agent: *"
    assert result["whois_raw"] == "whois"
    assert result["open_ports"][0]["family"] == "ipv4"
    assert len(result["artifacts_saved"]) == 3
    for saved in result["artifacts_saved"]:
        assert Path(saved).exists()
