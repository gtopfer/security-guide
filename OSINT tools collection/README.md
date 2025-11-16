# OSINT tools collection

Portal de navegação para todas as metodologias, scripts e templates OSINT do repositório. Use esta página para escolher rapidamente o fluxo correto antes de abrir cada subpasta.

## Visão geral

- **Stack:** Python 3.10+, shell scripts e documentação Markdown (Linux-first, suportado em WSL).  
- **Fluxo principal:** Metodologia → scripts → dados/templates → relatório.  
- **Governança:** dados reais ficam fora do repo; utilize `.env` base a partir dos templates e registre decisões em Issues/PRs.

## Navegação rápida

### Documentação base (`docs/`)

| Recurso | Descrição | Quando usar |
|---------|-----------|-------------|
| [metodologia.md](docs/metodologia.md) | Pipeline completo de investigação (escopo, critérios legais e checklist de execução). | Comece qualquer operação por aqui. |
| [ferramentas_linux_osint.md](docs/ferramentas_linux_osint.md) | Toolchain essencial (CLI, pacotes, dicas de hardening para workstation). | Preparar ambiente ou revisar requisitos. |
| `docs/grupos/` | Playbooks temáticos (ver tabela abaixo). | Consultar etapas específicas (domínios, perfis, etc.). |

### Playbooks por grupo (`docs/grupos/`)

| Documento | Foco |
|-----------|------|
| [coleta_geral.md](docs/grupos/coleta_geral.md) | Checklist macro de coleta passiva/ativa. |
| [coleta_dominios.md](docs/grupos/coleta_dominios.md) | CRT.sh, subfinder, amass e heurísticas de DNS. |
| [varredura_infra.md](docs/grupos/varredura_infra.md) | Perfis Nmap, fingerprint HTTP e possíveis portas-alvo. |
| [busca_perfis.md](docs/grupos/busca_perfis.md) | Alvos em redes sociais e validação cruzada de personas. |
| [redes_sociais.md](docs/grupos/redes_sociais.md) | Referências adicionais por plataforma. |
| [metadados_arquivos.md](docs/grupos/metadados_arquivos.md) | Coleta de EXIF/strings em documentos públicos. |
| [darkweb.md](docs/grupos/darkweb.md) | Fluxo controlado para investigações em camadas onion. |
| [automacao_scripts.md](docs/grupos/automacao_scripts.md) | Como agendar tarefas, integrar com cron/GitHub Actions. |

### Scripts e automações (`scripts/`)

| Recurso | Descrição | Próximo passo |
|---------|-----------|---------------|
| [osint_collector.py](scripts/osint_collector.py) | Scanner inicial: DNS, portas IPv4/IPv6, WHOIS, fingerprint HTTP/TLS e export de artefatos (`--artifacts-dir`). | Ver exemplos de uso em `docs/metodologia.md` §Coleta inicial. |
| `scripts/domains/` | Complementos (CRT.sh, resoluções). | Encadear após playbook de domínios. |
| `scripts/recon/` | Perfis para theHarvester/recon-ng. | Emparelhar com `docs/grupos/busca_perfis.md`. |
| `scripts/automation/Makefile.osint` | Tarefas padronizadas (`make enumerate`, `make report`). | Usar para pipelines locais/CI. |

### Dados e templates

| Caminho | Conteúdo | Observações |
|---------|----------|-------------|
| `data/examples/` | Exemplos anonimizados (ex.: [sample_target.json](data/examples/sample_target.json)). | Útil para testar dashboards e notebooks. |
| `data/outputs/` | Local padrão para resultados reais (não versionados). | Adicione ao `.gitignore` ao criar novos arquivos. |
| `templates/` | Estruturas `.env` por tipo de investigação (busca_perfis, domains, etc.). | Copie e personalize (`cp templates/... .env`). |

### Execução guiada

1. **Preparar ambiente:** siga os pré-requisitos de `docs/ferramentas_linux_osint.md` e crie uma venv (`python3 -m venv .venv && source .venv/bin/activate && pip install -r scripts/requirements.txt`).  
2. **Definir escopo:** aplique o checklist de `docs/metodologia.md` (Regras de engajamento + matriz de risco).  
3. **Rodar coleta inicial:** `python3 scripts/osint_collector.py --target <alvo> --out data/outputs/<alvo>.json --artifacts-dir data/artifacts/<alvo>`  
4. **Especializar fluxo:** avance para o playbook correspondente (domínios, perfis, infraestrutura).  
5. **Consolidar:** gere relatórios conforme instruções da seção “Consolidação” em `docs/metodologia.md`.

### Testes e qualidade

- Dependências listadas em [scripts/requirements.txt](scripts/requirements.txt).  
- Testes unitários em [`tests/test_osint_collector.py`](tests/test_osint_collector.py); execute com `pytest tests`.  
- Configure `pre-commit` no repositório raiz para validar Markdown e scripts antes de submeter PRs.

## Próximos passos

- Integrar APIs autenticadas (Shodan, Censys) mantendo chaves em Vault/Secrets Manager.  
- Publicar dashboards (Grafana/PowerBI) lendo `data/outputs/`.  
- Acrescentar novos templates `.env` quando surgirem casos específicos (dark web, malware, etc.).
