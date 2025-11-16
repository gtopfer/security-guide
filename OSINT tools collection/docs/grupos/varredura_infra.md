# Varredura de infraestrutura

Embora existam vários scanners, o Nmap continua sendo a base. Este guia aprofunda uso, perfis e exportações para pipelines.

## Nmap

### Visão geral
Nmap identifica portas abertas, serviços, versões e pode executar scripts NSE. Use-o após identificar hosts com `httpx/massdns` para reduzir ruído.

### Instalação e preparação
```bash
sudo apt install -y nmap xmlstarlet
mkdir -p scans
```
- `xmlstarlet` ajuda a parsear saída XML do Nmap.

### Perfis de execução
1. **Scan rápido para validação**
    ```bash
    nmap -Pn -T4 -F -oA scans/nmap_fast alvo.com
    ```
    - `-F` varre portas mais comuns.
2. **Scan completo com detecção de versão**
    ```bash
    nmap -sV -sC -Pn -p- alvo.com -oA scans/nmap_full
    ```
    - `-sC` executa scripts NSE "default".
3. **Scan a partir de lista**
    ```bash
    nmap -iL data/httpx_vivos.txt -p 80,443,8080,8443 -sV -oA scans/nmap_web
    ```

### Pós-processamento detalhado
```bash
xmlstarlet sel -t -m "//host[ports/port/state/@state='open']" \
  -v "concat(address/@addr,';',ports/port/@portid,';',ports/port/service/@name)" -n \
  scans/nmap_full.xml > data/nmap_full.csv
```
- Exporta IP;porta;serviço para Excel ou ingestão em Recon-ng.

### Scripts NSE úteis
```bash
nmap --script "ssl-enum-ciphers,vulners" -p 443 alvo.com -oN scans/nmap_ssl.txt
nmap --script http-title,http-headers -p 80,443 -iL data/http_alvos.txt -oN scans/nmap_http.txt
```
- Atualize o banco NSE: `sudo nmap --script-updatedb`.

### Fluxo sugerido
1. Pegue `data/httpx_empresa.txt`, filtre status 200/302 para `alive.txt`.
2. Rode `nmap` focado em portas HTTP + portas raras identificadas.
3. Se o alvo permitir, use `--traceroute` e `--reason` para análises de rede.
