# 🔍 Coleção de Ferramentas OSINT

> Uma lista curada de ferramentas e recursos incríveis de Inteligência de Código Aberto (OSINT) em português.

[Open-source intelligence (OSINT)](https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_de_c%C3%B3digo_aberto) é inteligência coletada de fontes publicamente disponíveis. Na comunidade de inteligência, o termo "aberto" refere-se a fontes públicas overt (em oposição a fontes encobertas ou clandestinas).

Esta coleção foi desenvolvida para ajudar todos aqueles interessados em Inteligência de Ameaças Cibernéticas (CTI), caça de ameaças (threat hunting) ou OSINT. Do iniciante ao avançado.

**Feliz hacking e hunting 🧙‍♂️**

---

## 📖 Índice de Conteúdo

- [Buscas Gerais](#buscas-gerais)
- [Redes Sociais](#redes-sociais)
- [Busca de Pessoas](#busca-de-pessoas)
- [Email e Telefone](#email-e-telefone)
- [Domínio e IP](#domínio-e-ip)
- [Busca de Imagens](#busca-de-imagens)
- [Análise de Imagens](#análise-de-imagens)
- [Geoespacial e Mapas](#geoespacial-e-mapas)
- [Notícias e Dados](#notícias-e-dados)
- [Inteligência de Ameaças](#inteligência-de-ameaças)
- [Privacidade e Segurança](#privacidade-e-segurança)
- [Ferramentas Personalizadas](#ferramentas-personalizadas)
- [Começando](#começando)
- [Contribuindo](#contribuindo)

---

## 🔎 Buscas Gerais

Motores de busca e ferramentas de pesquisa geral. Use estas fontes para pesquisas amplas, Google Dorks e buscas especializadas.

- **Google / Google Dorks:** pesquisa avançada com operadores (`site:`, `filetype:`, `inurl:`). Ferramentas úteis: DorkGenius, DorkGPT.
- **Bing / Brave / DuckDuckGo:** alternativas para diferentes indexações e privacidade.
- **Buscas especializadas:** Shodan, Censys, ZoomEye (dispositivos/IoT); PublicWWW / grep.app (busca em código/HTML);
- **Arquivo histórico:** Wayback Machine, Archive.is.

Principais referências rápidas: Google Search, Shodan, Censys, PublicWWW.

---

## 📱 Redes Sociais

Ferramentas para investigação em redes sociais (busca de perfis, monitoramento e extração).

- **Busca multiplataforma:** `Sherlock`, `Maigret` — procura usernames em centenas de sites.
- **Twitter / X:** `Twitter Advanced Search`, `ExportData`, `Trends24` para análise de tendências.
- **Instagram:** `Osintgram`, `Toutatis` para coleta de perfis públicos.
- **Telegram / Reddit / TikTok / YouTube:** `TgramSearch`, `Pushshift`, `yt-dlp` e ferramentas de extração de metadados.

Boas práticas: use contas dedicadas e documente ações; respeite termos de serviço e leis locais.

---

## 👥 Busca de Pessoas

Ferramentas e fontes para identificar pessoas (diretórios, genealogia, perfis públicos e bancos de dados).

- **People search / diretórios:** `PeekYou`, `Spokeo`, `WhitePages` (varia por país).
- **Genealogia e registros públicos:** `FamilySearch`, `FamilyTreeNow`.
- **Identificação por imagem:** `PimEyes`, `FaceCheck.ID` (uso responsável).

Dicas rápidas: combine resultados de redes sociais com registros públicos e valide identidades com múltiplas fontes.

---

## 📧 Email e Telefone

Recursos para descobrir, validar e verificar emails e números de telefone.

- **Breach / dumps:** `Have I Been Pwned`, `DeHashed`, `LeakCheck`, `h8mail`.
- **Verificação de email:** `EmailHippo`, `MailTester`.
- **Encontrar emails corporativos:** `Hunter`, `Snov.io`.
- **Pesquisa de telefone:** `PhoneInfoga`, `TrueCaller`, `FreeCarrierLookup`.

Observação: manipule dados pessoais com responsabilidade e conforme legislação aplicável.

---

## 🌐 Domínio e IP

Ferramentas para investigação de infraestrutura: DNS, subdomínios, certificados, ASN e reputação.

- **Enumeração de subdomínios:** `Amass`, `Subfinder`, `Merklemap` (CT logs).
- **Whois / histórico DNS:** `SecurityTrails`, `DomainTools`, `ViewDNS`.
- **Certificados / CT logs:** `CRT.sh`, `Censys`.
- **Reputação / análise de IP:** `VirusTotal`, `AbuseIPDB`, `GreyNoise`.

Fluxo recomendado: coleta passiva → enumeração → verificação de serviços → avaliação de reputação.

---

## 🖼️ Busca de Imagens

Ferramentas para buscar imagens por conteúdo visual.

**Veja:** [05_busca_imagens/README.md](./05_busca_imagens/README.md)

---

## 📸 Análise de Imagens

Ferramentas para análise de metadados e forensia de imagens.

**Veja:** [06_analise_imagens/README.md](./06_analise_imagens/README.md)

---

## 🗺️ Geoespacial e Mapas

Ferramentas de geolocalização, mapeamento e pesquisa espacial.

**Veja:** [07_geoespacial_mapas/README.md](./07_geoespacial_mapas/README.md)

---

## 📰 Notícias e Dados

Ferramentas para coleta de notícias, dados e estatísticas.

**Veja:** [08_noticias_dados/README.md](./08_noticias_dados/README.md)

---

## 🎯 Inteligência de Ameaças

Ferramentas de inteligência de ameaças, análise de malware e segurança.

**Veja:** [09_threat_intelligence/README.md](./09_threat_intelligence/README.md)

---

## 🔒 Privacidade e Segurança

Ferramentas para proteção de privacidade, criptografia e segurança.

**Veja:** [10_privacidade_seguranca/README.md](./10_privacidade_seguranca/README.md)

---

## 🛠️ Ferramentas Personalizadas

Scripts e ferramentas Python desenvolvidas para automação de OSINT.

**Veja:** [ferramentas/README.md](./ferramentas/README.md)

---

## 🚀 Começando

### Requisitos
- Python 3.8+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/osint-tools-collection.git
cd osint-tools-collection

# Crie um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### Uso Rápido

```bash
# Configure variáveis de ambiente
cp .env.example .env
# Edite .env e preencha as chaves/API keys necessárias

# Execute o coletor
python ferramentas/coletores/osint_collector.py --target example.com --output data/outputs/
```

### Estrutura de Diretórios

```
osint-tools-collection/
├── 00_buscas_gerais/              # Buscas gerais e Google Dorks
├── 01_redes_sociais/              # Ferramentas para redes sociais
├── 02_busca_pessoas/              # Busca de pessoas
├── 03_email_telefone/             # Pesquisa de email e telefone
├── 04_dominio_ip/                 # Análise de domínios e IPs
├── 05_busca_imagens/              # Busca de imagens
├── 06_analise_imagens/            # Análise de metadados
├── 07_geoespacial_mapas/          # Geolocalização e mapas
├── 08_noticias_dados/             # Notícias e dados
├── 09_threat_intelligence/        # Inteligência de ameaças
├── 10_privacidade_seguranca/      # Privacidade e segurança
├── ferramentas/                   # Scripts Python personalizados
│   ├── coletores/                 # Coletores de dados
│   ├── analise/                   # Scripts de análise
│   └── automacao/                 # Scripts de automação
├── modelos/                       # Templates de configuração
├── dados/                         # Dados e exemplos
│   ├── examples/                  # Arquivos de exemplo
│   └── outputs/                   # Saídas processadas
├── docs/                          # Documentação
└── testes/                        # Testes unitários
```

---

## 📚 Documentação

Veja a [documentação completa](./docs/) para detalhes sobre cada ferramenta.

- [Metodologia](./docs/metodologia.md)
- [Ferramentas Linux OSINT](./docs/ferramentas_linux_osint.md)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia [CONTRIBUTING.md](../CONTRIBUTING.md) para detalhes sobre nosso código de conduta e processo de submissão.

---

## 📝 Licença

Este trabalho está licenciado sob a licença [Creative Commons Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/).

---

**Última atualização:** 16 de novembro de 2025 | **Status:** Em desenvolvimento ativo 🚀
