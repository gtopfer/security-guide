# 🛠️ Ferramentas Personalizadas

Scripts e ferramentas Python desenvolvidas para automação de OSINT.

## Estrutura

```
ferramentas/
├── coletores/              # Scripts para coleta de dados
│   ├── osint_collector.py  # Coletor geral OSINT
│   └── ...
├── analise/                # Scripts de análise de dados
│   └── ...
├── automacao/              # Automação e agendamento
│   └── Makefile
└── requirements.txt        # Dependências Python
```

## Coletores

### osint_collector.py
Coletor principal para investigações OSINT.

**Uso:**
```bash
python ferramentas/coletores/osint_collector.py --target example.com --output data/outputs/
```

**Características:**
- Coleta DNS e WHOIS
- Enumeration de subdomínios
- Análise de IPs
- Verificação de porta
- Fingerprint HTTP/TLS
- Export de artefatos

## Análise

Ferramentas para análise de dados coletados.

## Automação

### Makefile
Automação de tarefas comuns.

**Comandos disponíveis:**
```bash
make enumerate    # Executar coleta completa
make report       # Gerar relatório
make clean        # Limpar outputs
```

## Instalação

```bash
# A partir do diretório raiz
pip install -r ferramentas/requirements.txt
```

## Configuração

Crie um arquivo `.env`:

```bash
cp .env.example .env
# Edite .env com suas chaves/credenciais
```

## Exemplos

Ver exemplos de saída em `data/examples/sample_target.json`

---

**Contribuições:** Pull requests para novas ferramentas são bem-vindas!
