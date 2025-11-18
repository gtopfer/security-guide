# 🔍 Coleção de Ferramentas OSINT (Só FOSS)

> Biblioteca viva com projetos **100% open source**, hospedados em Git e executáveis local/offline, sem cadastros pagos. O objetivo é oferecer o conjunto mais completo possível para investigações OSINT/CTI.

Cada ferramenta abaixo traz:
- Link direto para o repositório oficial.
- Stack principal para facilitar troubleshooting.
- Um comando de inicialização/teste local (adequar conforme SO).

> ⚠️ Algumas integrações aceitam APIs externas opcionais (Shodan, Censys, etc.). Elas não são necessárias para iniciar o uso básico descrito aqui.

---

## ✅ Critérios de Curadoria

1. Licença permissiva (GPL, MIT, Apache, etc.) e código aberto auditável.
2. Instalação via `git clone`, `pip`, `poetry`, `npm`, `cargo`, `go install` ou Docker público.
3. Execução local sem portais proprietários obrigatórios.
4. Comunidade ativa ou manutenção mínima (issues, releases recentes).

Contribuições devem seguir os mesmos critérios.

---

## 📚 Índice

1. [Dorks Google & Macetes](#dorks-google--macetes)
2. [Frameworks & Suites de Recon](#frameworks--suites-de-recon)
3. [Perfis e Redes Sociais](#perfis-e-redes-sociais)
4. [Mensageria & Plataformas Nicho](#mensageria--plataformas-nicho)
5. [Email, Telefone & Credenciais](#email-telefone--credenciais)
6. [Domínios, IPs & Infraestrutura](#domínios-ips--infraestrutura)
7. [Varrimento Web & Serviços](#varrimento-web--serviços)
8. [Arquivos, Documentos & Metadados](#arquivos-documentos--metadados)
9. [Mídia (Imagem, Áudio, Vídeo)](#mídia-imagem-áudio-vídeo)
10. [Geoespacial & Sensoriamento Remoto](#geoespacial--sensoriamento-remoto)
11. [Código & Dados Públicos](#código--dados-públicos)
12. [Inteligência de Ameaças / IOC](#inteligência-de-ameaças--ioc)
13. [Automação & Pipelines](#automação--pipelines)
14. [Listas/Referências Complementares](#listasreferências-complementares)
15. [Começando](#começando)
16. [Contribuindo](#contribuindo)

---

## Dorks Google & Macetes

Resumo rápido disponível em [`docs/google-search/README.md`](docs/google-search/README.md) com operadores (`site`, `intitle`, `AROUND`, `filetype`), exemplos de dorks e workflow recomendado para consultas avançadas.

---

## Frameworks & Suites de Recon

| Ferramenta | Repositório | Stack | Uso rápido |
|------------|-------------|-------|------------|
| **SpiderFoot** | https://github.com/smicallef/spiderfoot | Python | `pip install spiderfoot && sf.py -s example.com -o simple` |
| **recon-ng** | https://github.com/lanmaster53/recon-ng | Python | `git clone ... && ./recon-ng` |
| **sn0int** | https://github.com/kpcyrd/sn0int | Rust | `cargo install sn0int && sn0int init` |
| **datasploit** | https://github.com/DataSploit/datasploit | Python | `pip install datasploit && datasploit -d example.com` |
| **theHarvester** | https://github.com/laramies/theHarvester | Python | `pip install theHarvester && theHarvester -d example.com -b all` |
| **Photon** | https://github.com/s0md3v/Photon | Python | `pip install photon && photon -u https://example.com` |
| **BlackWidow** | https://github.com/1N3/BlackWidow | Bash/Python | `./blackwidow -u https://example.com -s` |
| **GoWitness** | https://github.com/sensepost/gowitness | Go | `go install github.com/sensepost/gowitness@latest` |

---

## Perfis e Redes Sociais

| Ferramenta | Repositório | Foco |
|------------|-------------|------|
| **Sherlock** | https://github.com/sherlock-project/sherlock | Checagem de usernames em 600+ plataformas. |
| **Maigret** | https://github.com/soxoj/maigret | Perfil OSINT completo com ranking de confiança. |
| **Social Analyzer** | https://github.com/qeeqbox/social-analyzer | API/CLI para encontrar perfis por username + nome real. |
| **LittleBrother** | https://github.com/lulz3xploit/LittleBrother | OSINT sobre identidades (nome, domínios, redes). |
| **Osintgram** | https://github.com/Datalux/Osintgram | CLI para extrair dados de contas Instagram públicas. |
| **tiktok-scraper** | https://github.com/drawrowfly/tiktok-scraper | Coleta vídeos/perfis TikTok via Node.js. |
| **snscrape** | https://github.com/JustAnotherArchivist/snscrape | Scraper universal para Twitter, Reddit, Telegram channels etc. |
| **git-hound** | https://github.com/tillson/git-hound | Busca credenciais/leaks em GitHub (útil para perfis corporativos). |

---

## Mensageria & Plataformas Nicho

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **Telescan** | https://github.com/martinlindhe/telescan | Enumeração de usuários/links em Telegram via CLI. |
| **Telepathy** | https://github.com/mk-fg/telepathy | Ferramentas para scraping/monitoramento de canais Telegram. |
| **Matrix-Spyglass** | https://github.com/spantaleev/matrix-spotlight | Busca e indexação em salas Matrix auto-hospedadas. |
| **DiscordChatExporter** | https://github.com/Tyrrrz/DiscordChatExporter | Extrai chats de servidores (é preciso token, mas não há custo). |
| **Reddit Data Tools** | https://github.com/Watchful1/Pushshift-Importer | Operações locais com dumps Pushshift/Reddit. |

---

## Email, Telefone & Credenciais

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **holehe** | https://github.com/megadose/holehe | Verifica se emails aparecem em serviços populares. |
| **Infoga** | https://github.com/m4ll0k/Infoga | Enumeração de emails + vazamentos públicos. |
| **PhoneInfoga** | https://github.com/sundowndev/phoneinfoga | Recon OSINT de números telefônicos. |
| **WhatBreach** | https://github.com/Ekultek/WhatBreach | Consulta e baixa dumps públicos para uma identidade. |
| **GHunt** | https://github.com/mxrch/GHunt | Perfil OSINT focado em contas Google (cookies opcionais). |
| **pwndb** | https://github.com/davidtavarez/pwndb | CLI para consultar banco alternativo do serviço `pwndb2am4tzkvold`. |

---

## Domínios, IPs & Infraestrutura

| Ferramenta | Repositório | Stack | Destaque |
|------------|-------------|-------|----------|
| **OWASP Amass** | https://github.com/owasp-amass/amass | Go | Enumeração passiva/ativa de subdomínios. |
| **Subfinder** | https://github.com/projectdiscovery/subfinder | Go | Subdomínios via fontes públicas (ProjectDiscovery). |
| **Sublist3r** | https://github.com/aboul3la/Sublist3r | Python | Rápido e leve para wordlists pequenas. |
| **findomain** | https://github.com/Findomain/Findomain | Rust | Enumeração + monitoramento contínuo. |
| **assetfinder** | https://github.com/tomnomnom/assetfinder | Go | Descobre domínios vinculados a uma organização. |
| **puredns** | https://github.com/d3mondev/puredns | Go | Resolvedor + wordlist aware com filtros wildcard. |
| **dnsx** | https://github.com/projectdiscovery/dnsx | Go | Resolutor multi-record com outputs flexíveis. |
| **massdns** | https://github.com/blechschmidt/massdns | C | Resolução DNS massiva. |
| **Crt.sh scraper** | https://github.com/crtsh/certificate-transparency-go | Go | Lê CT Logs localmente. |

---

## Varrimento Web & Serviços

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **Naabu** | https://github.com/projectdiscovery/naabu | Scanner de portas TCP rápido. |
| **Nmap** | https://github.com/nmap/nmap | Scanner clássico multi-protoco. |
| **Masscan** | https://github.com/robertdavidgraham/masscan | Varrimento TCP ultra rápido. |
| **ZMap** | https://github.com/zmap/zmap | Scanner IP layer 3 (IPv4 completo). |
| **httpx** | https://github.com/projectdiscovery/httpx | Descobre serviços HTTP, títulos, fingerprints. |
| **katana** | https://github.com/projectdiscovery/katana | Web crawler para mapping OSINT. |
| **gau** | https://github.com/lc/gau | Coleta URLs arquivadas (Wayback, CommonCrawl). |
| **hakrawler** | https://github.com/hakluke/hakrawler | Crawler CLI leve para recon. |
| **EyeWitness** | https://github.com/RedSiege/EyeWitness | Captura screenshots e banners de serviços web. |

---

## Arquivos, Documentos & Metadados

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **ExifTool** | https://github.com/exiftool/exiftool | Extração universal de metadados. |
| **peepdf** | https://github.com/eternal-todo/peepdf | Análise de PDFs maliciosos. |
| **Metagoofil** | https://github.com/opsdisk/metagoofil | Busca docs públicos e extrai autor, SO, versão. |
| **bulk-extractor** | https://github.com/simsong/bulk_extractor | Mineração de artefatos em dumps/disk images. |
| **pdfid/pdf-parser** | https://github.com/DidierStevens/DidierStevensSuite | Ferramentas forenses para PDFs. |
| **oletools** | https://github.com/decalage2/oletools | Inspeção de arquivos Office (VBA, macros). |
| **Strelka** | https://github.com/target/strelka | Pipeline escalável para análise de arquivos (Docker/K8s). |

---

## Mídia (Imagem, Áudio, Vídeo)

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **gallery-dl** | https://github.com/mikf/gallery-dl | Downloader universal (Twitter, Reddit, Pixiv, etc.). |
| **yt-dlp** | https://github.com/yt-dlp/yt-dlp | Download/extração de metadata de vídeos/streams. |
| **Sherloq** | https://github.com/GuidoBartoli/sherloq | Ferramenta GUI para análise forense de imagens. |
| **Image-Hash** | https://github.com/JohannesBuchner/imagehash | Gera perceptual hashes para comparação offline. |
| **DeepFaceLive / insightface** | https://github.com/deepinsight/insightface | Reconhecimento/comparação facial (modo local). |
| **FFmpeg** | https://github.com/FFmpeg/FFmpeg | Manipulação/extração de frames, áudio, legendas. |

---

## Geoespacial & Sensoriamento Remoto

| Ferramenta | Repositório | Destaques |
|------------|-------------|-----------|
| **SatDump** | https://github.com/altillimity/SatDump | Decodifica dados de satélite (NOAA, GOES, METEOR) com SDR consumer. |
| **SARchiver** | https://github.com/planetlabs/notebooks | Scripts para processar dados SAR públicos (Sentinel-1). |
| **OpenAerialMap tools** | https://github.com/hotosm/oam-uploader | Interage com acervo OAM/OSM. |
| **gpxpy** | https://github.com/tkrajina/gpxpy | Manipula trilhas GPX, útil para analisar rotas físicas. |
| **heatmappy** | https://github.com/nikolaypavlov/heatmappy | Gera heatmaps offline usando Folium. |
| **QGIS** | https://github.com/qgis/QGIS | Plataforma GIS completa e open source (com plugins OSINT). |

---

## Código & Dados Públicos

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **git-dorks** | https://github.com/thewhiteh4t/gitdorker | Procura leaks sensíveis em GitHub pela CLI. |
| **TruffleHog OSS** | https://github.com/trufflesecurity/trufflehog | Busca segredos em repositórios/dumps. |
| **Gitleaks** | https://github.com/gitleaks/gitleaks | Auditoria de credenciais expostas. |
| **PublicWWW CLI** | https://github.com/xGCx/PublicWWWRipper | Interage com índice PublicWWW local. |
| **Common Crawl Index** | https://github.com/commoncrawl/cc-pyspark | Scripts para minerar dados do Common Crawl sem serviços pagos. |
| **datasette** | https://github.com/simonw/datasette | Publica datasets locais para consulta rápida. |

---

## Inteligência de Ameaças / IOC

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **IntelOwl** | https://github.com/intelowlproject/IntelOwl | Plataforma modular para consultar/analisar indicadores. |
| **OpenCTI** | https://github.com/OpenCTI-Platform/opencti | Plataforma CTI escalável (GraphQL + workers). |
| **MISP** | https://github.com/MISP/MISP | Compartilhamento colaborativo de IOCs. |
| **Yeti** | https://github.com/yeti-platform/yeti | Base de conhecimento para relacionar TTPs, atores, IOCs. |
| **Stoq** | https://github.com/PUNCH-Cyber/stoq | Orquestração de análises de artefatos (plugins locais). |
| **Viper** | https://github.com/viper-framework/viper | Gestão de amostras de malware e metadados IOC. |
| **Sigma** | https://github.com/SigmaHQ/sigma | Regras genéricas que podem alimentar hunts/monitoramento. |

---

## Automação & Pipelines

| Ferramenta | Repositório | Aplicação |
|------------|-------------|-----------|
| **OSINT Orchestrator** | https://github.com/cipher387/osint-tools | Scripts automatizados/schedulers. |
| **Cortex/Analyzer** | https://github.com/TheHive-Project/Cortex-Analyzers | Executa análises (YARA, hash, etc.) localmente. |
| **StackStorm Packs** | https://github.com/StackStorm-Exchange/stackstorm-osint | Automação baseada em eventos. |
| **n8n.io** | https://github.com/n8n-io/n8n | Automação low-code self-hosted (use webhooks/datasets OSINT). |
| **Prefect** | https://github.com/PrefectHQ/prefect | Orquestração de pipelines Python para coletas periódicas. |

---

## Listas/Referências Complementares

- **OSINT-Framework** — https://github.com/lockfale/osint-framework (taxonomia navegável de links; pode ser auto-hospedado).
- **Awesome OSINT** — https://github.com/jivoi/awesome-osint (curadoria comunitária extensa).
- **Awesome Threat Intelligence** — https://github.com/hslatman/awesome-threat-intelligence.
- **Punk Security OSINT Collection** — https://github.com/punk-security/OSINT_Collection.
- **Maltego-CE Transforms (local)** — https://github.com/maltegoct/maltego-trx (permite criar transforms offline).

---

## Começando

1. **Ambiente** — use `pyenv`/`virtualenv`, `conda`, `Go` >=1.20, `Rust` (`rustup`) e Docker para projetos containerizados.
2. **Clonar & instalar** — siga o `README` de cada ferramenta; quase todas fornecem `requirements.txt` ou scripts `install.sh`.
3. **Testes locais** — execute contra domínios controlados (ex.: `example.com`, labs internos) antes de mirar alvos reais.
4. **Automatizar** — padronize `Makefile`/`invoke`/`prefect` para rodar coleções periódicas e salvar em `data/outputs/`.
5. **Registrar artefatos** — guarde evidências em formatos interoperáveis (JSONL, CSV, Markdown) e sanitize antes de compartilhar.

> Recomendação: mantenha um inventário de wordlists, proxies e datasets em `data/examples/` para reproduzir análises sem dependências externas.

---

## Contribuindo

- Abra uma Issue ou PR propondo nova ferramenta **FOSS** (sem SaaS, sem paywall).
- Inclua link, stack, comando de uso rápido e descrição concisa.
- Caso o projeto precise de API key opcional, detalhe a configuração offline.
- Atualize apenas se o repositório estiver ativo (release/commit recente) para manter o guia confiável.

**Feliz hacking, agora só com código livre!**
