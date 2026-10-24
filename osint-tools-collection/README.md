# Coleção de ferramentas OSINT (somente software livre)

> Catálogo de projetos **100% de código aberto**, hospedados em Git e executáveis no ambiente local, sem cadastro pago. O objetivo é cobrir investigação OSINT e CTI com ferramentas que você instala e controla.

Por que esta lista existe:

- Cobre a maior parte dos casos OSINT e CTI sem SaaS obrigatório e sem paywall.
- Executa no ambiente local, com Python, Go, Rust ou Docker. Você controla o dado e a consulta.
- Permite montar um laboratório repetível para treino e para investigação curta.

Como ler e aplicar:

- Cada ferramenta traz o link oficial, a stack principal e um comando de uso rápido. Ajuste o comando ao seu sistema.
- Execute em ambiente isolado (`venv` ou contêiner). Nos testes, use domínio e dado sob o seu controle.
- Combine as ferramentas nesta ordem: enumere, colete o artefato, correlacione e grave em CSV ou JSONL.

> Algumas integrações aceitam API externa opcional (Shodan, Censys e outras). Essa API não é necessária para o uso básico descrito aqui.

---

## Critérios de curadoria

1. Licença permissiva (GPL, MIT, Apache ou equivalente) e código-fonte auditável.
2. Instalação por `git clone`, `pip`, `poetry`, `npm`, `cargo`, `go install` ou Docker público.
3. Execução local, sem portal proprietário obrigatório.
4. Comunidade ativa ou manutenção mínima (issue e release recentes).

A contribuição segue os mesmos critérios.

---

## Índice

0. [Kit rápido](#kit-rápido)
1. [Dorks do Google](#dorks-do-google)
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

## Kit rápido

- Ambiente mínimo: Python 3.11+ (`venv`), Go 1.21+, Rust (`rustup`) e Docker.
- Instale as ferramentas de rede: `nmap`, `masscan`, `curl` e `jq`.
- Dados de teste: `example.com`, domínio sob o seu controle e dump público (Common Crawl, Arctic Shift).
- Fluxo curto:
  1. Enumere domínio e subdomínio (Amass ou Subfinder) e capture a tela (EyeWitness ou GoWitness).
  2. Colete perfil público (Sherlock ou Maigret) e verifique credencial vazada (holehe ou mosint).
  3. Correlacione em planilha, CSV ou JSONL. Monte um dork para validar o achado. Automatize com `make` ou `n8n`.

---

## Dorks do Google

O resumo está em [`docs/google-search/README.md`](docs/google-search/README.md). O guia cobre operadores (`site`, `intitle`, `AROUND`, `filetype`), exemplos de consulta e um fluxo para busca avançada.

---

## Frameworks & Suites de Recon

| Ferramenta | Repositório | Stack | Uso rápido |
|------------|-------------|-------|------------|
| **SpiderFoot** | <https://github.com/smicallef/spiderfoot> | Python | `pip install spiderfoot && sf.py -s example.com -o simple` |
| **recon-ng** | <https://github.com/lanmaster53/recon-ng> | Python | `git clone ... && ./recon-ng` |
| **sn0int** | <https://github.com/kpcyrd/sn0int> | Rust | `cargo install sn0int && sn0int init` |
| **datasploit** (manutenção irregular) | <https://github.com/DataSploit/datasploit> | Python | `pip install datasploit && datasploit -d example.com` |
| **theHarvester** | <https://github.com/laramies/theHarvester> | Python | `pip install theHarvester && theHarvester -d example.com -b all` |
| **Photon** | <https://github.com/s0md3v/Photon> | Python | `pip install photon && photon -u https://example.com` |
| **BlackWidow** (manutenção irregular) | <https://github.com/1N3/BlackWidow> | Bash/Python | `./blackwidow -u https://example.com -s` |
| **GoWitness** | <https://github.com/sensepost/gowitness> | Go | `go install github.com/sensepost/gowitness@latest` |
| **bbot** | <https://github.com/blacklanternsecurity/bbot> | Python | `pip install bbot && bbot -t example.com -f subdomain-enum` |
| **reNgine** | <https://github.com/yogeshojha/rengine> | Python/Django | Framework de reconhecimento com interface web (Docker Compose). |
| **Mr.Holmes** | <https://github.com/Lucksi/Mr.Holmes> | Python | `python mrholmes.py` — conjunto OSINT com menu interativo. |
| **seekr** | <https://github.com/seekr-osint/seekr> | Rust/Web | Conjunto OSINT hospedado por você, com interface web. |

Ordem sugerida: comece com o SpiderFoot para a varredura ampla. Valide domínio e subdomínio com Amass ou Subfinder. Capture a tela com GoWitness ou EyeWitness e priorize a revisão manual.

> **Manutenção irregular** significa ausência de commit ou de release recente. A ferramenta ainda executa. Quando existir alternativa com manutenção ativa, prefira essa alternativa (por exemplo, SpiderFoot, theHarvester ou Photon no lugar de datasploit e BlackWidow).

---

## Perfis e Redes Sociais

| Ferramenta | Repositório | Foco |
|------------|-------------|------|
| **Sherlock** | <https://github.com/sherlock-project/sherlock> | Verifica um nome de usuário em mais de 600 plataformas. |
| **Maigret** | <https://github.com/soxoj/maigret> | Monta um perfil OSINT e atribui um nível de confiança. |
| **Social Analyzer** | <https://github.com/qeeqbox/social-analyzer> | API e CLI para localizar perfil por nome de usuário e por nome. |
| **LittleBrother** (manutenção irregular) | <https://github.com/lulz3xploit/LittleBrother> | OSINT de identidade: nome, domínio e rede social. |
| **Osintgram** | <https://github.com/Datalux/Osintgram> | CLI para coletar dado de conta pública do Instagram. |
| **tiktok-scraper** | <https://github.com/drawrowfly/tiktok-scraper> | Coleta vídeo e perfil do TikTok com Node.js. |
| **snscrape** | <https://github.com/JustAnotherArchivist/snscrape> | Coleta Reddit, Telegram, Mastodon e outras fontes. O suporte a Twitter/X deixou de funcionar após a mudança de API de 2023. |
| **git-hound** | <https://github.com/tillson/git-hound> | Busca credencial e vazamento no GitHub. Útil em perfil corporativo. |
| **gosearch** | <https://github.com/ibnaleem/gosearch> | Consulta a pegada de um nome de usuário em mais de 300 sites. Escrito em Go. |
| **tookie-osint** | <https://github.com/Alfredredbird/tookie-osint> | Busca conta por nome de usuário. A taxa de acerto publicada pelo projeto é de cerca de 80%. |
| **instaloader** | <https://github.com/instaloader/instaloader> | Baixa e estrutura perfil e publicação públicos do Instagram. |
| **toutatis** | <https://github.com/megadose/toutatis> | Lê dado de conta do Instagram (e-mail ou telefone parcial, bio, seguidores) com um session ID. |

Ordem sugerida: use Sherlock, Maigret ou gosearch para localizar o perfil. Use Osintgram, instaloader ou toutatis para a coleta detalhada. Use git-hound para vazamento ligado ao usuário ou à organização.

---

## Mensageria & Plataformas Nicho

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **Telescan** | <https://github.com/pielco11/telescan> | Enumera usuário e link no Telegram pela linha de comando. |
| **DiscordChatExporter** | <https://github.com/Tyrrrz/DiscordChatExporter> | Exporta conversa de servidor. Exige um token da conta. Não há custo de licença. |
| **Arctic Shift** | <https://github.com/ArthurHeitmann/arctic_shift> | Dump do Reddit após o fim do Pushshift. Baixa e pesquisa comentário e publicação no ambiente local. |
| **BAScraper** | <https://github.com/maxjo020418/BAScraper> | Cliente Python assíncrono para PullPush.io e Arctic Shift, substitutos comunitários do Pushshift. |

> O Pushshift original foi desativado em 2023. Use Arctic Shift ou PullPush para dado histórico do Reddit.

Use o token somente em conta autorizada. Prefira dump público. Isso reduz conflito com os termos de uso da plataforma.

---

## Email, Telefone & Credenciais

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **holehe** | <https://github.com/megadose/holehe> | Verifica se o e-mail está cadastrado em serviços populares. |
| **PhoneInfoga** | <https://github.com/sundowndev/phoneinfoga> | Reconhecimento OSINT de número de telefone. |
| **WhatBreach** | <https://github.com/Ekultek/WhatBreach> | Consulta e baixa dump público associado a uma identidade. |
| **GHunt** | <https://github.com/mxrch/GHunt> | Perfil OSINT de conta Google. O cookie é opcional. |
| **mosint** | <https://github.com/alpkeskin/mosint> | OSINT de e-mail em Go: vazamento, validação e pastebin. |
| **pwndb** (manutenção irregular) | <https://github.com/davidtavarez/pwndb> | Consulta um banco alternativo do serviço `pwndb2am4tzkvold` via Tor. |

Trate o resultado antes de gravar. Não armazene senha nem dado pessoal em texto claro. Guarde o hash ou uma referência.

---

## Domínios, IPs & Infraestrutura

| Ferramenta | Repositório | Stack | Destaque |
|------------|-------------|-------|----------|
| **OWASP Amass** | <https://github.com/owasp-amass/amass> | Go | Enumeração passiva e ativa de subdomínio. |
| **Subfinder** | <https://github.com/projectdiscovery/subfinder> | Go | Subdomínio a partir de fonte pública (ProjectDiscovery). |
| **Sublist3r** | <https://github.com/aboul3la/Sublist3r> | Python | Enumeração leve, adequada a wordlist pequena. |
| **findomain** | <https://github.com/Findomain/Findomain> | Rust | Enumeração e monitoramento contínuo. |
| **assetfinder** | <https://github.com/tomnomnom/assetfinder> | Go | Localiza domínio ligado a uma organização. |
| **puredns** | <https://github.com/d3mondev/puredns> | Go | Resolvedor com wordlist e filtro de wildcard. |
| **dnsx** | <https://github.com/projectdiscovery/dnsx> | Go | Resolvedor de vários tipos de registro, com saída flexível. |
| **massdns** | <https://github.com/blechschmidt/massdns> | C | Resolução DNS em grande volume. |
| **ct-go (CT Logs)** | <https://github.com/google/certificate-transparency-go> | Go | Lê Certificate Transparency no ambiente local. |

Ordem sugerida: Subfinder ou Amass, depois puredns ou dnsx para limpar o resultado, depois naabu ou nmap para portas, depois httpx ou katana para serviços, depois gowitness ou eyewitness para captura de tela.

---

## Varrimento Web & Serviços

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **Naabu** | <https://github.com/projectdiscovery/naabu> | Scanner de portas TCP de alta velocidade. |
| **Nmap** | <https://github.com/nmap/nmap> | Scanner clássico de vários protocolos. |
| **Masscan** | <https://github.com/robertdavidgraham/masscan> | Varredura TCP de alta velocidade. |
| **ZMap** | <https://github.com/zmap/zmap> | Scanner de camada de rede para o espaço IPv4. |
| **httpx** | <https://github.com/projectdiscovery/httpx> | Identifica serviço HTTP, título e fingerprint. |
| **katana** | <https://github.com/projectdiscovery/katana> | Rastreador web para mapeamento OSINT. |
| **gau** | <https://github.com/lc/gau> | Coleta URL arquivada (Wayback, Common Crawl). |
| **hakrawler** | <https://github.com/hakluke/hakrawler> | Rastreador leve de linha de comando. |
| **EyeWitness** | <https://github.com/RedSiege/EyeWitness> | Captura tela e banner de serviço web. |
| **web-check** | <https://github.com/lissy93/web-check> | Consulta OSINT de um site: DNS, TLS, cabeçalhos, tecnologias e localização do servidor. |

Combine httpx com gau ou katana para mapear a superfície. Use o resultado na descoberta de conteúdo do escopo autorizado.

---

## Arquivos, Documentos & Metadados

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **ExifTool** | <https://github.com/exiftool/exiftool> | Extração de metadados de vários formatos. |
| **peepdf** | <https://github.com/digitalsleuth/peepdf-3> | Análise de PDF malicioso. Porte para Python 3 (GPL-3.0). O repositório do autor permanece em <https://github.com/jesparza/peepdf>. |
| **Metagoofil** | <https://github.com/opsdisk/metagoofil> | Busca documento público e extrai autor, sistema e versão. |
| **bulk-extractor** | <https://github.com/simsong/bulk_extractor> | Extrai artefato de dump e de imagem de disco. |
| **pdfid/pdf-parser** | <https://github.com/DidierStevens/DidierStevensSuite> | Ferramentas forenses para PDF. |
| **oletools** | <https://github.com/decalage2/oletools> | Inspeção de arquivo Office (VBA e macro). |
| **Strelka** | <https://github.com/target/strelka> | Pipeline para análise de arquivo (Docker ou Kubernetes). |

Extraia o metadado em JSONL (ExifTool). Calcule o SHA-256 de cada arquivo para rastrear a evidência.

---

## Mídia (Imagem, Áudio, Vídeo)

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **gallery-dl** | <https://github.com/mikf/gallery-dl> | Download de mídia (Twitter, Reddit, Pixiv e outros). |
| **yt-dlp** | <https://github.com/yt-dlp/yt-dlp> | Download e extração de metadado de vídeo e de stream. |
| **Sherloq** | <https://github.com/GuidoBartoli/sherloq> | Interface gráfica para análise forense de imagem. |
| **Image-Hash** | <https://github.com/JohannesBuchner/imagehash> | Gera hash perceptual para comparação offline. |
| **DeepFaceLive / insightface** | <https://github.com/deepinsight/insightface> | Reconhecimento e comparação facial no ambiente local. |
| **FFmpeg** | <https://github.com/FFmpeg/FFmpeg> | Extrai quadro, áudio e legenda. |

Fluxo típico: baixe com yt-dlp ou gallery-dl, gere o hash perceptual, compare ou deduplique, e guarde o quadro ou a legenda relevante.

---

## Geoespacial & Sensoriamento Remoto

| Ferramenta | Repositório | Destaques |
|------------|-------------|-----------|
| **SatDump** | <https://github.com/altillimity/SatDump> | Decodifica dado de satélite (NOAA, GOES, METEOR) com SDR de consumo. |
| **OpenSarToolkit** | <https://github.com/ESA-PhiLab/OpenSarToolkit> | Inventário, download e pré-processamento de dado SAR do Sentinel-1 em Python. |
| **OpenAerialMap tools** (manutenção irregular) | <https://github.com/hotosm/oam-uploader> | Interage com o acervo OpenAerialMap e OpenStreetMap. |
| **gpxpy** | <https://github.com/tkrajina/gpxpy> | Lê e grava trilha GPX. Serve para analisar rota. |
| **Folium** | <https://github.com/python-visualization/folium> | Gera mapa e mapa de calor em Python (interface para Leaflet.js). |
| **QGIS** | <https://github.com/qgis/QGIS> | Plataforma GIS de código aberto, com plugins úteis para OSINT. |

Registre o código EPSG ao cruzar camadas. Documente a fonte (satélite ou contribuição coletiva) para repetir a análise.

---

## Código & Dados Públicos

| Ferramenta | Repositório | Uso |
|------------|-------------|-----|
| **TruffleHog OSS** | <https://github.com/trufflesecurity/trufflehog> | Busca segredo em repositório e em dump. |
| **Gitleaks** | <https://github.com/gitleaks/gitleaks> | Auditoria de credencial exposta. |
| **Zoekt** | <https://github.com/sourcegraph/zoekt> | Motor de busca de código por trigrama, hospedado por você, para indexar vários repositórios. |
| **octosuite** | <https://github.com/bellingcat/octosuite> | Ferramenta de terminal (Bellingcat) para analisar usuário, repositório e organização no GitHub. |
| **Common Crawl Index** | <https://github.com/commoncrawl/cc-pyspark> | Scripts para minerar o Common Crawl sem serviço pago. |
| **datasette** | <https://github.com/simonw/datasette> | Publica um conjunto de dados local para consulta. |

Normalize a saída em JSONL ou CSV. Para arquivo grande, use Git LFS.

---

## Inteligência de Ameaças / IOC

| Ferramenta | Repositório | Descrição |
|------------|-------------|-----------|
| **IntelOwl** | <https://github.com/intelowlproject/IntelOwl> | Plataforma modular para consultar e analisar indicador. |
| **OpenCTI** | <https://github.com/OpenCTI-Platform/opencti> | Plataforma de CTI (GraphQL e workers). |
| **MISP** | <https://github.com/MISP/MISP> | Compartilhamento de IOC entre equipes. |
| **Yeti** | <https://github.com/yeti-platform/yeti> | Base para relacionar TTP, ator e IOC. |
| **Stoq** | <https://github.com/PUNCH-Cyber/stoq> | Orquestra análise de artefato com plugin local. |
| **Viper** | <https://github.com/viper-framework/viper> | Organiza amostra de malware e metadado de IOC. |
| **Sigma** | <https://github.com/SigmaHQ/sigma> | Regra genérica de detecção para caça e monitoramento. |
| **World Monitor** | <https://github.com/koala73/worldmonitor> | Painel de eventos globais: notícia, evento geopolítico e infraestrutura. Inclui funções de IA. |

Em laboratório isolado, use o Docker Compose de OpenCTI, MISP e Cortex. Sincronize o IOC por feed exportável (STIX ou MISP).

---

## Automação & Pipelines

| Ferramenta | Repositório | Aplicação |
|------------|-------------|-----------|
| **Cortex/Analyzer** | <https://github.com/TheHive-Project/Cortex-Analyzers> | Executa análise local (YARA, hash e outros). |
| **Huginn** | <https://github.com/huginn/huginn> | Automação por evento e por agente, no modelo IFTTT, hospedada por você. |
| **n8n.io** | <https://github.com/n8n-io/n8n> | Automação com pouca programação, hospedada por você (webhook e conjunto OSINT). |
| **Prefect** | <https://github.com/PrefectHQ/prefect> | Orquestra pipeline Python para coleta periódica. |

Crie a pasta `data/` com `inputs/`, `outputs/` e `cache/`. Grave o log em JSONL.

---

## Listas/Referências Complementares

- **OSINT-Framework** — <https://github.com/lockfale/osint-framework> (taxonomia navegável de links; pode ser hospedada por você).
- **Awesome OSINT** — <https://github.com/jivoi/awesome-osint> (curadoria comunitária extensa).
- **osint_stuff_tool_collection** — <https://github.com/cipher387/osint_stuff_tool_collection> (serviços e ferramentas online, por categoria).
- **Legendary OSINT** — <https://github.com/K2SOsint/Legendary_OSINT> (lista para fraude, CTI, KYC e AML, com mais de 25 categorias).
- **Awesome Threat Intelligence** — <https://github.com/hslatman/awesome-threat-intelligence>.
- **Maltego Transforms (SDK local)** — <https://github.com/MaltegoTech/maltego-transforms> (MIT; cria transforms que executam na sua máquina. O `maltego-trx` legado foi arquivado).

---

## Começando

1. **Ambiente.** Instale `pyenv` ou `venv`, Go 1.21 ou superior, Rust via `rustup`, Docker Compose e as ferramentas de rede (`nmap`, `curl`, `jq`).
2. **Instalação.** Cada projeto traz `requirements.txt`, `poetry.lock` ou um binário Go ou Rust. Isole cada ferramenta.
3. **Teste.** Use domínio sob o seu controle e laboratório. Não dispare varredura agressiva em rede de terceiro.
4. **Automação.** Use `Makefile`, `invoke`, Prefect ou n8n para repetir o pipeline (`make recon`, `make collect-social`).
5. **Registro.** Grave a saída em JSONL ou CSV, com hash e horário. Remova o dado pessoal antes de compartilhar.
6. **Correlação.** Cruze o resultado com dork, dump público e IOC. Documente a hipótese e o limite da evidência.

> Mantenha um inventário de wordlist, proxy e conjunto de dados em `data/examples/`. Assim você repete a análise sem dependência externa.

---

## Contribuindo

Leia o [guia de contribuição](../CONTRIBUTING.md). Resumo:

- Abra uma issue ou um pull request com uma ferramenta **de software livre** (sem SaaS obrigatório e sem paywall).
- Inclua o link, a stack, o comando de uso rápido e uma descrição curta.
- Se o projeto aceita uma chave de API opcional, descreva a configuração offline.
- Atualize a linha somente quando o repositório tem release ou commit recente.

## Prática e limites

- Respeite a lei, os termos de uso e o consentimento. Não ataque um sistema e não colete dado de terceiro sem autorização.
- Limite a taxa de varredura. Prefira fonte passiva quando ela responde à pergunta.
- Proteja a privacidade: descarte o dado pessoal que não é necessário, criptografe a cópia de segurança e anonimize o relatório.
- Documente o contexto: origem do dado, horário da coleta, ferramenta e parâmetro.

Consulte também os [estudos de segurança ofensiva](../offensive-security/README.md) quando o trabalho sair do reconhecimento passivo.
