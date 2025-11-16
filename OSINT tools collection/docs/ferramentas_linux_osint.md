# Ferramentas OSINT para Linux

Material “mão na massa” para conduzir coletas OSINT em ambientes Linux. O documento está organizado em um menu de navegação rápido para que você encontre a fase desejada, execute os comandos e registre resultados sem precisar voltar ao início.

## Menu rápido

0. [Panorama rápido de ferramentas](#mapa-ferramentas)
1. [Ambiente e instalação](#ambiente-e-instalacao)
2. [Visão de infraestrutura (DNS/WHOIS/IP)](#infra)
3. [Superfície web e serviços HTTP](#web)
4. [Perfis, e-mails e redes sociais](#sociais)
5. [Arquivos públicos e histórico](#arquivos)
6. [Frameworks e automação](#frameworks)
7. [Playbooks passo a passo](#playbooks)
8. [Checklist e boas práticas](#checklist)

---

## Panorama rápido de ferramentas <a id="mapa-ferramentas"></a>

> Seguem os grupos descritos pelo usuário, cada um com um README próprio dentro de `OSINT/docs/grupos/`. Todos os conteúdos continuam 100% open source e trazem instalação, configuração, uso e fluxos práticos extremamente detalhados.

| Grupo | Conteúdo | Referência |
|-------|----------|------------|
| Coleta geral | SpiderFoot, Recon-ng, theHarvester, pipeline sugerido com integrações. | [`docs/grupos/coleta_geral.md`](grupos/coleta_geral.md) |
| Busca em sites/pessoas/perfis | Uso offline do OSINT Framework e coleções comunitárias (Bellingcat/cipher387). | [`docs/grupos/busca_perfis.md`](grupos/busca_perfis.md) |
| Redes sociais | Twint, Sherlock e Instagram Scraper com exemplos de scraping, grafos e custódia. | [`docs/grupos/redes_sociais.md`](grupos/redes_sociais.md) |
| Coleta de domínios | CRT.sh (script), subfinder, amass, assetfinder e massdns integrados. | [`docs/grupos/coleta_dominios.md`](grupos/coleta_dominios.md) |
| Varredura de infraestrutura | Perfis completos de Nmap, scripts NSE e pós-processamento. | [`docs/grupos/varredura_infra.md`](grupos/varredura_infra.md) |
| Metadados e arquivos | Playbooks para ExifTool e Metagoofil, inclusive extração em lote. | [`docs/grupos/metadados_arquivos.md`](grupos/metadados_arquivos.md) |
| Dark web / deep web | Operação segura com Tor Browser, Ahmia e OnionSearch. | [`docs/grupos/darkweb.md`](grupos/darkweb.md) |
| Automação e scripts | Reaproveitamento do `osint_stuff_tool_collection` e boilerplate Python. | [`docs/grupos/automacao_scripts.md`](grupos/automacao_scripts.md) |

> Todos os scripts e templates mencionados nos READMEs vivem em `OSINT/scripts/` e `OSINT/templates/`. Copie-os para o ambiente de trabalho antes de executar para manter o repositório limpo.

> Categorias “Busca de vazamentos e dumps” e “Imagens e vídeos” continham apenas serviços proprietários. Assim que surgirem alternativas abertas, crie novos READMEs no mesmo diretório.

---

## 1. Ambiente e instalação <a id="ambiente-e-instalacao"></a>

| Tarefa | Comando |
|--------|---------|
| Atualizar pacotes essenciais | `sudo apt update && sudo apt install -y whois dnsutils nmap curl wget jq git python3-pip` |
| Instalar `pipx` (Python isolado) | `python3 -m pip install --user pipx && pipx ensurepath` |
| Ferramentas Python (theHarvester, holehe, sherlock) | `pipx install theHarvester && pipx install holehe && pipx install sherlock` |
| Tooling em Go (`subfinder`, `httpx`, `katana`, `waybackurls`) | `go install github.com/projectdiscovery/{subfinder/v2/cmd/subfinder,httpx/cmd/httpx,katana/cmd/katana,waybackurls}@latest` (adicione `~/go/bin` ao `PATH`) |
| Instalar `amass`, `assetfinder`, `gau` via `snap`/`apt`/`go` | `sudo snap install amass` ou `go install github.com/tomnomnom/assetfinder@latest` / `go install github.com/lc/gau/v2/cmd/gau@latest` |
| Automação (Osmedeus, ReconFTW) | `git clone https://github.com/osmedeus/osmedeus ; cd osmedeus && ./install.sh` / `git clone https://github.com/six2dez/reconftw` |

> Use ambientes virtuais ou contêineres para separar projetos e garantir reprodutibilidade.

---

## 2. Visão de infraestrutura (DNS/WHOIS/IP) <a id="infra"></a>

| Ferramenta | Objetivo | Exemplo rápido |
|------------|----------|----------------|
| `whois` | Consultar registrante, datas e registradores | `whois exemplo.com | tee data/whois.txt` |
| `dig` | Mapear registros DNS específicos e brute-force manual | `dig exemplo.com A +short`, `dig -t TXT _dmarc.exemplo.com` |
| `amass` | Enumeração extensa de subdomínios (passivo/ativo) | `amass enum -passive -d exemplo.com -o data/amass_passivo.txt` |
| `subfinder` | Subdomínios via APIs/parcerias | `subfinder -d exemplo.com -all -o data/subfinder.txt` |
| `assetfinder` | Subdomínios com foco em certificados e ASN | `assetfinder --subs-only exemplo.com >> data/subs_raw.txt` |
| `massdns` + wordlist | Resolução em massa (brute-force) | `./massdns -r resolvers.txt -t A -o S -w data/massdns.txt lista_subs.txt` |
| `nmap` | Descoberta de portas e detecção de serviços | `nmap -sV -Pn -p- exemplo.com -oN scans/nmap_full.txt` |

### Mini tutorial – inventário inicial
1. Validar WHOIS e datas críticas: `whois alvo.com | grep -i 'Creation Date'`.
2. Resolver registros chave: `for t in A AAAA MX TXT; do dig alvo.com $t +short; done`.
3. Enumerar subdomínios via APIs: `subfinder -d alvo.com -all | tee data/subs.txt`.
4. Validar quais respondem a ping/HTTP: `cat data/subs.txt | httpx -title -status-code -ip -o data/httpx.txt`.
5. Rodar um scan direcionado: `nmap -sV -Pn -iL <(cut -d' ' -f2 data/httpx.txt) -p 80,443,8080 -oN scans/nmap_web.txt`.

---

## 3. Superfície web e serviços HTTP <a id="web"></a>

| Ferramenta | Uso prático | Comando base |
|------------|-------------|--------------|
| `httpx` (ProjectDiscovery) | Checar status, título, IP, tecnologias | `httpx -l data/subs.txt -title -tech-detect -status-code -web-server -o data/httpx_full.txt` |
| `katana` | Crawler rápido para descobrir endpoints | `katana -u https://app.exemplo.com -d 3 -jc -fs robots -o data/katana.txt` |
| `gau`/`waybackurls` | URLs históricas/arquivadas para fuzz | `echo exemplo.com | gau > data/gau.txt` |
| `nuclei` | Templates de fingerprint e detecção rápida | `nuclei -l alive.txt -t cves/ -severity critical,high -o results/nuclei.txt` |
| `curl`/`wget` | Baixar `robots.txt`, `sitemap`, APIs | `curl -A "Mozilla" https://exemplo.com/robots.txt` |
| `ffuf`/`feroxbuster` | Fuzzing de diretórios/param | `ffuf -u https://api.exemplo.com/FUZZ -w wordlists/commons.txt -mc 200,302 -o scans/ffuf.json` |

### Tabela rápida (copie e cole)

```bash
TARGET=exemplo.com
subfinder -d $TARGET | httpx -title -status-code -tech-detect -o data/httpx_$TARGET.txt
katana -list data/httpx_$TARGET.txt -jc -o data/katana_$TARGET.txt
echo $TARGET | gau > data/gau_$TARGET.txt
cat data/gau_$TARGET.txt | grep -i ".php" | sort -u > wordlists/$TARGET_php.txt
```

---

## 4. Perfis, e-mails e redes sociais <a id="sociais"></a>

| Ferramenta | Escopo | Comando |
|------------|--------|---------|
| `theHarvester` | Coleta inicial de e-mails/hosts a partir de motores de busca | `theHarvester -d exemplo.com -b all -f reports/harvester.html` |
| `holehe` | Verificar se e-mail existe em cadastros populares | `holehe alvo@exemplo.com` |
| `sherlock` | Username em múltiplas redes | `sherlock alias --print-found --folderoutput outputs/sherlock` |
| `maigret` | Similar ao sherlock, com foco em perfis russos/europeus | `maigret alias --site 50 --timeout 10` |
| `ghunt` | Investigação de contas Google (Calendar, Photos, Maps) | `python3 ghunt.py email alvo@exemplo.com` |
| `emailrep` | Reputação de e-mail (APIs) | `curl https://emailrep.io/alvo@exemplo.com | jq` |

### Playbook rápido – validação de persona
1. Rodar `theHarvester` para listar e-mails e hosts relacionados.
2. Para cada e-mail, executar `holehe` e `emailrep`.
3. Para usernames conhecidos, rodar `sherlock` e `maigret`.
4. Registrar evidências (prints, JSON) em `data/perfis/`.

---

## 5. Arquivos públicos e histórico <a id="arquivos"></a>

| Ferramenta | Objetivo | Exemplo |
|------------|----------|---------|
| `metagoofil` | Buscar documentos (PDF/DOC/PPT) e extrair metadados | `metagoofil -d exemplo.com -t pdf,docx -n 100 -o dumps/ -w` |
| `exiftool` | Ver metadados de imagens/localização | `exiftool imagem.jpg` |
| `wget` (mirror) | Download controlado de sites | `wget --mirror --convert-links --page-requisites https://portal.exemplo.com -P mirrors/portal` |
| `waybackurls` | URLs antigas (Wayback) | `echo exemplo.com | waybackurls | tee data/wayback.txt` |
| `unfurl` | Extrair parâmetros de URLs | `cat data/wayback.txt | unfurl keys` |
| `maltego`/`casefile` | Pivot visual entre entidades | `maltego` (UI) |

---

## 6. Frameworks e automação <a id="frameworks"></a>

| Ferramenta | Destaque | Execução sugerida |
|------------|----------|-------------------|
| `Osmedeus` | Pipeline modular (recon, scan, relatório) | `osmedeus scan -t exemplo.com -m recon/web` |
| `ReconFTW` | Automação ofensiva completa (subdomínios, cloud, vulnerabilidades) | `./reconftw.sh -d exemplo.com -r out/` |
| `Hakrawler + httpx + nuclei` | Cadeia customizada | `hakrawler -url https://exemplo.com | sort -u | httpx | nuclei -t cves/` |
| `SpiderFoot` | Web UI para 200+ fontes | `docker run -p 5001:5001 spiderfoot` |

> Ajuste limites de requisições e chaves de API antes de rodar frameworks para evitar bloqueios.

---

## 7. Playbooks passo a passo <a id="playbooks"></a>

### Playbook A – Recon passivo em 15 minutos
1. `whois alvo.com` → salvar datas em `notes.md`.
2. `subfinder -d alvo.com | tee data/subs.txt`.
3. `amass enum -passive -d alvo.com -o data/amass.txt`.
4. `cat data/subs.txt data/amass.txt | sort -u > data/all_subs.txt`.
5. `httpx -l data/all_subs.txt -title -status-code -tech-detect -o data/http_alive.txt`.
6. `waybackurls < data/all_subs.txt > data/historico.txt`.

### Playbook B – Coleta web ativa
1. Selecionar 10 hosts com status 200/302 de `httpx`.
2. Para cada host, rodar `katana -u https://host --d 3 -jc -o data/katana_host.txt`.
3. Filtrar endpoints com parâmetros: `grep '=' data/katana_host.txt | unfurl keys`.
4. Rodar `ffuf` com wordlist curta em `/api/v1/FUZZ`.
5. Com URLs coletadas, rodar `nuclei -list urls_parametrizadas.txt -t exposures/`.

### Playbook C – Persona / rede social
1. `theHarvester -d empresa.com -b linkedin,bing`.
2. `holehe user@empresa.com` para ver cadastros.
3. `sherlock nome_sobrenome`.
4. `ghunt email_gmail` (necessário configurar tokens).
5. Montar quadro resumo (fonte, URL, status de verificação).

Cada playbook pode ser transformado em script; utilize `tmux` ou `GNU parallel` para dividir etapas.

---

## 8. Checklist e boas práticas <a id="checklist"></a>

- [ ] Documentar todas as fontes consultadas e timestamps.
- [ ] Salvar saída bruta (`tee`/`jq`) antes de filtrar.
- [ ] Organizar diretórios por alvo (`data/<alvo>/...`).
- [ ] Utilizar VPN/infra dedicada quando requisitado.
- [ ] Respeitar limites legais, termos de uso e LGPD.
- [ ] Automatizar limpeza e criptografia de dados sensíveis após o projeto.

> Execute sempre em ambientes autorizados e respeite limites legais e políticas de uso das APIs consultadas.
