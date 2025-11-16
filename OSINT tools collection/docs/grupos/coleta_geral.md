# Coleta geral – Pipeline base

Este guia descreve em profundidade como combinar SpiderFoot, Recon-ng e theHarvester para montar um pipeline de coleta inicial. Cada ferramenta tem perfis distintos, mas todas são open source e rodam bem em Linux.

## SpiderFoot

### Visão detalhada
SpiderFoot é um orquestrador de automação OSINT. Ele oferece mais de 200 módulos cobrindo DNS, WHOIS, redes sociais, vazamentos e dark web. Você pode comandá-lo via web (UI em CherryPy) ou CLI (`sf.py`). A vantagem é empilhar módulos e armazenar resultados em um banco SQLite único (`spiderfoot.db`).

### Instalação
```bash
sudo apt install -y python3-venv build-essential libffi-dev libssl-dev
cd ~/Tools && git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot && python3 -m venv venv && source venv/bin/activate
pip install --upgrade pip && pip install -r requirements.txt
```
- `python3-venv` isola dependências.
- `build-essential/libffi-dev/libssl-dev` evitam erros com módulos TLS.

### Configuração
```bash
source ~/Tools/spiderfoot/venv/bin/activate
cd ~/Tools/spiderfoot
./generate-certificate --hostname 0.0.0.0 --out certs/server
cp config/example.spiderfootrc config/spiderfootrc
sed -i "s/^_maxthreads=.*/_maxthreads=5/" config/spiderfootrc
```
- O script `generate-certificate` protege a UI com TLS.
- `config/spiderfootrc` mantém opções globais (proxies, chaves API, limites de threads).

### Uso aprofundado
1. **Web UI completa**
    ```bash
    source ~/Tools/spiderfoot/venv/bin/activate
    python3 sf.py -l 0.0.0.0:5001 -w -m passive -s exemplo.com
    ```
    - `-w` inicia a interface web.
    - `-m passive` limita módulos a fontes passivas (útil para coletar sem tocar no alvo).

2. **CLI para execuções headless**
    ```bash
    python3 sf.py -s exemplo.com -t SUBDOMAIN_NAME,EMAILADDR -f csv > data/spiderfoot_exemplo.csv
    ```
    - `-t` filtra os tipos de eventos armazenados.

3. **Exportar resultados**
    ```bash
    sqlite3 data/spiderfoot.db "SELECT type,data FROM tbl_event WHERE scanid='1'" > data/spiderfoot_scan1.tsv
    ```
    - Útil para alimentar outras ferramentas como `httpx` e `nmap`.

### Fluxo recomendado
1. Inicie um scan `passive` para mapear entidades gerais.
2. Exporte subdomínios vivos e envie para `httpx` → `nmap`.
3. Aproveite o módulo `sfp_spiderfoot` para reusar resultados em Recon-ng.

## Recon-ng

### Visão detalhada
Recon-ng é um framework modular inspirado em Metasploit. Ele organiza workspaces, módulos e chaves de API para facilitar investigações reprodutíveis. Cada módulo produz/consome tabelas padronizadas no banco SQLite integrado. Ideal para pivotar dados coletados do SpiderFoot.

### Instalação
```bash
sudo apt install -y python3-pip libpq-dev
cd ~/Tools && git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng && pip install --user -r REQUIREMENTS
```
- O pacote `libpq-dev` permite módulos que falam com PostgreSQL.

### Configuração
```bash
mkdir -p ~/Tools/recon-ng/rc
cp OSINT/scripts/recon/setup_workspace.rc ~/Tools/recon-ng/rc/
cd ~/Tools/recon-ng
./recon-ng -r rc/setup_workspace.rc
```
- O arquivo `setup_workspace.rc` cria um workspace chamado `empresa` e adiciona chaves básicas (edite o arquivo copiado antes de executar).

### Uso aprofundado
1. **Inventário de hosts públicos**
    ```bash
    cp OSINT/scripts/recon/bing_inventory.rc rc/
    ./recon-ng -r rc/bing_inventory.rc
    ```
2. **Exportar para CSV**
    ```bash
    cp OSINT/scripts/recon/export_csv.rc rc/
    ./recon-ng -r rc/export_csv.rc
    ```
3. **Integração com SpiderFoot** – importe subdomínios encontrados e valide com módulos de DNS (`recon/domains-hosts/brute_hosts`).

### Fluxo recomendado
- Use Recon-ng para centralizar apenas fontes que exigem API (Bing, VirusTotal, SecurityTrails).
- Mantenha workspaces por alvo para histórico.
- Combine módulos `recon/domains-contacts/` para identificar personas.

## theHarvester

### Visão detalhada
theHarvester é perfeito para coleta inicial “shotgun”: consulta vários buscadores, lê certificados SSL e retorna e-mails, hosts e IPs. Ideal antes de partir para ferramentas mais pesadas.

### Instalação
```bash
sudo apt install -y python3-poetry
cd ~/Tools && git clone https://github.com/laramies/theHarvester.git
cd theHarvester && poetry install
```
- O projeto suporta `poetry`, que cuida de dependências e scripts (`poetry run`).

### Configuração
```bash
cd ~/Tools/theHarvester
mkdir -p ~/.config/theHarvester
cp api-keys.yaml ~/.config/theHarvester/api-keys.yaml
sed -i "s/google:.*/google: 'SUA_CHAVE'/" ~/.config/theHarvester/api-keys.yaml
```
- Alimente apenas os motores que você realmente tem chave (Google, Shodan, Bing).

### Uso aprofundado
1. **Relatório HTML completo**
    ```bash
    cd ~/Tools/theHarvester
    poetry run python theHarvester.py -d empresa.com -l 500 -b google,bing,crtsh -f reports/empresa.html
    ```
2. **Saída em JSON para automação**
    ```bash
    poetry run python theHarvester.py -d empresa.com -b bing -f reports/empresa.json -T json
    jq '.["emails"]' reports/empresa.json > data/emails.txt
    ```
3. **Cadeia com `holehe`/`sherlock`**
    ```bash
    while read email; do
      holehe "$email" | tee -a data/holehe.txt
    done < <(cut -d ':' -f2 data/emails.txt)
    ```

### Fluxo recomendado
- Rode theHarvester com poucos motores primeiro para evitar rate limits.
- Combine resultados com SpiderFoot (`-s` import) e Recon-ng (tabela `contacts`).
- Use a opção `-v` para ver em tempo real cada fonte consultada e detectar bloqueios.
