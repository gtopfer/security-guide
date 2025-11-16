# 🎨 Visualização da Estrutura Final

## Estrutura Completa do Repositório

```
osint-tools-collection/
│
├── 📘 README.md                          ← COMECE AQUI!
├── 📄 REORGANIZACAO.md                   ← Resumo das mudanças
├── 📋 CONTRIBUTING.md                    ← Como contribuir
├── 📄 pyproject.toml                     ← Configuração do projeto
│
├── 📁 00_buscas_gerais/
│   ├── README.md                         (Google, Bing, DuckDuckGo, etc)
│   └── .gitkeep
│
├── 📁 01_redes_sociais/
│   ├── README.md                         (Twitter, Facebook, Instagram, etc)
│   └── .gitkeep
│
├── 📁 02_busca_pessoas/
│   ├── README.md                         (FaceCheck, genealogia, etc)
│   └── .gitkeep
│
├── 📁 03_email_telefone/
│   ├── README.md                         (Email search, telefone, etc)
│   └── .gitkeep
│
├── 📁 04_dominio_ip/
│   ├── README.md                         (WHOIS, DNS, SSL, etc)
│   └── .gitkeep
│
├── 📁 05_busca_imagens/
│   ├── README.md                         (Google Images, TinEye, etc)
│   └── .gitkeep
│
├── 📁 06_analise_imagens/
│   ├── README.md                         (EXIF, metadados, forensia)
│   └── .gitkeep
│
├── 📁 07_geoespacial_mapas/
│   ├── README.md                         (Google Maps, satélite, etc)
│   └── .gitkeep
│
├── 📁 08_noticias_dados/
│   ├── README.md                         (Notícias, estatísticas, etc)
│   └── .gitkeep
│
├── 📁 09_threat_intelligence/
│   ├── README.md                         (Malware, APT, CVE, etc)
│   └── .gitkeep
│
├── 📁 10_privacidade_seguranca/
│   ├── README.md                         (VPN, criptografia, etc)
│   └── .gitkeep
│
├── 📁 ferramentas/                       ← SCRIPTS PYTHON
│   ├── README.md                         (Documentação)
│   ├── requirements.txt                  (Dependências)
│   │
│   ├── 📁 coletores/
│   │   ├── osint_collector.py            (Coletor principal)
│   │   ├── crtsh.sh                      (Certificados SSL)
│   │   └── ...
│   │
│   ├── 📁 analise/
│   │   ├── export_csv.rc                 (Export de dados)
│   │   ├── import_list.rc                (Import de dados)
│   │   └── ...
│   │
│   └── 📁 automacao/
│       ├── Makefile.osint                (Automação de tarefas)
│       └── ...
│
├── 📁 modelos/                           ← TEMPLATES DE CONFIG
│   ├── README.md                         (Documentação)
│   │
│   ├── 📁 busca_perfis/
│   │   └── osint-framework.env
│   │
│   ├── 📁 darkweb/
│   │   └── onionsearch.env
│   │
│   ├── 📁 domains/
│   │   ├── amass_config.ini
│   │   ├── resolvers.txt
│   │   └── subfinder_config.yaml
│   │
│   ├── 📁 metadados/
│   │   ├── exiftool_osint.args
│   │   └── metagoofil.env
│   │
│   └── 📁 redes_sociais/
│       ├── alvos_sherlock.txt
│       ├── instagram_config.json
│       ├── twint_proxy.env
│       └── twint.env
│
├── 📁 dados/                             ← DADOS E EXEMPLOS
│   ├── 📁 examples/
│   │   └── sample_target.json            (Exemplo de saída)
│   │
│   └── 📁 outputs/
│       └── .gitkeep                      (Salve outputs aqui)
│
├── 📁 docs/                              ← DOCUMENTAÇÃO
│   ├── INDICE.md                         ← COMECE AQUI se quer aprender
│   ├── metodologia.md                    (Pipeline de investigação)
│   ├── ferramentas_linux_osint.md        (Ferramentas CLI)
│   │
│   └── 📁 grupos/
│       ├── coleta_geral.md               (Coleta passiva/ativa)
│       ├── coleta_dominios.md            (Enumeration de domínios)
│       ├── varredura_infra.md            (Scanning de infraestrutura)
│       ├── busca_perfis.md               (Busca em redes sociais)
│       ├── redes_sociais.md              (Por plataforma)
│       ├── metadados_arquivos.md         (Análise de metadados)
│       ├── darkweb.md                    (Investigação Tor)
│       └── automacao_scripts.md          (Automação e scheduling)
│
├── 📁 testes/                            ← TESTES UNITÁRIOS
│   ├── test_osint_collector.py
│   └── __init__.py
│
└── 📁 scripts/                           ← SCRIPTS ORIGINAIS (mantidos)
    ├── osint_collector.py
    ├── requirements.txt
    ├── 📁 domains/
    │   └── crtsh.sh
    ├── 📁 recon/
    │   └── *.rc
    └── 📁 automation/
        └── Makefile.osint
```

## 🗺️ Mapa de Navegação Recomendado

### 📍 Para Iniciantes

```
1. Leia README.md (raiz)
        ↓
2. Veja INDICE.md em docs/
        ↓
3. Escolha uma categoria (ex: 01_redes_sociais)
        ↓
4. Explore a documentação
        ↓
5. Use as ferramentas
```

### 📍 Para Usuários de Scripts

```
1. Leia ferramentas/README.md
        ↓
2. Instale dependências (requirements.txt)
        ↓
3. Configure (.env)
        ↓
4. Execute coletores em ferramentas/coletores/
        ↓
5. Use templates em modelos/
```

### 📍 Para Pesquisadores

```
1. Comece em docs/INDICE.md
        ↓
2. Escolha um playbook em docs/grupos/
        ↓
3. Siga o checklist
        ↓
4. Use dados em dados/examples/
        ↓
5. Salve resultados em dados/outputs/
```

## 📊 Distribuição de Conteúdo

```
OSINT Tools Collection
│
├── 11 Categorias Temáticas
│   └── 200+ Ferramentas Documentadas
│
├── 15+ Arquivos README
│   └── 100% em Português
│
├── 8 Guias de Metodologia
│   └── Com checklists práticos
│
├── 3 Grupos de Scripts
│   ├── Coletores (coleta de dados)
│   ├── Análise (processamento)
│   └── Automação (scheduling)
│
├── 5 Grupos de Templates
│   └── Configurações pré-prontas
│
└── Exemplos e Documentação
    └── Pronto para começar
```

## 🎯 Fluxo de Uso Típico

```
Escolhe Objetivo
    ↓
    ├─→ Buscar Informação
    │       ↓
    │   Categoria Apropriada
    │       ↓
    │   Escolhe Ferramenta
    │       ↓
    │   Consulta URL/Link
    │
    ├─→ Automatizar Coleta
    │       ↓
    │   ferramentas/coletores/
    │       ↓
    │   Instala dependências
    │       ↓
    │   Configura .env
    │       ↓
    │   Executa script
    │
    └─→ Aprender Metodologia
            ↓
        docs/INDICE.md
            ↓
        Escolha um playbook
            ↓
        Siga o checklist
```

## 🔄 Fluxo de Dados

```
Raw Input (Target)
    ↓
Scripts em ferramentas/coletores/
    ↓
data/outputs/ (JSON/CSV)
    ↓
Scripts em ferramentas/analise/
    ↓
Relatório Final
```

## 📚 Hierarquia de Leitura

### Priority 1 (Obrigatório)
- README.md (raiz)
- docs/INDICE.md

### Priority 2 (Recomendado)
- Sua categoria de interesse
- docs/metodologia.md

### Priority 3 (Complementar)
- Outros README.md em docs/grupos/
- ferramentas/README.md

---

**💡 Dica:** Use esta visualização como mapa mental do repositório!
