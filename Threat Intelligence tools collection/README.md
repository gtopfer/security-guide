# Threat Intelligence tools collection

Portal para metodologias, scripts e templates de Threat Intelligence. Use este diretório como guia de navegação antes de abrir cada subpasta ou automatizar fluxos.

## Visão geral

- **Stack:** Python 3.10+, Makefiles e documentação Markdown focada em Linux.
- **Fluxo principal:** Metodologia → coleta/enriquecimento → correlação → disseminação.
- **Governança:** dados sensíveis ficam fora do repo. Utilize os templates `.env`/CSV para padronizar variáveis e mantenha histórico de decisões em Issues/PRs.

## Navegação rápida

### Documentação base (`docs/`)

| Recurso | Descrição | Quando usar |
|---------|-----------|-------------|
| [metodologia.md](docs/metodologia.md) | Pipeline completo (pergunta de inteligência, coleta, scoring e disseminação). | Kick-off de qualquer campanha. |
| [ferramentas_linux_ti.md](docs/ferramentas_linux_ti.md) | Tooling de suporte (STIX/TAXII, automação, hardening da estação). | Preparar o ambiente e revisar dependências. |
| `docs/grupos/` | Playbooks temáticos (IOCs, correlação, hunting). | Quando precisar de passos detalhados por domínio. |

### Playbooks por trilha (`docs/grupos/`)

| Documento | Foco |
|-----------|------|
| [colecao_iocs.md](docs/grupos/colecao_iocs.md) | Pipeline de ingestão, curadoria e publicação de indicadores. |
| [correlacao_alertas.md](docs/grupos/correlacao_alertas.md) | Uso de inteligência para priorizar alertas do SOC. |
| [hunting_proativo.md](docs/grupos/hunting_proativo.md) | Como transformar hipóteses em buscas estruturadas. |

### Scripts e automações (`scripts/`)

| Recurso | Descrição | Próximo passo |
|---------|-----------|---------------|
| [ti_collector.py](scripts/ti_collector.py) | Normaliza IOCs/alertas, remove duplicados e gera sumários JSON. | Use junto ao `sample_intel_case.json` para testar fluxo. |
| `scripts/enrich/` | Espaço para conectores (API TAXII, Shodan, VirusTotal). Inclui `.gitkeep` para versionar a pasta. | Adicionar novos módulos conforme integrações forem aprovadas. |
| [automation/Makefile.threatintel](scripts/automation/Makefile.threatintel) | Tarefas padronizadas (`make lint`, `make collect`, `make report`). | Rode `make help` para ver comandos disponíveis. |

### Dados e templates

| Caminho | Conteúdo | Observações |
|---------|----------|-------------|
| [data/examples/sample_intel_case.json](data/examples/sample_intel_case.json) | Caso exemplo com indicadores e ações recomendadas. | Útil para testar pipelines locais. |
| `data/outputs/` | Destino padrão para resultados reais (mantém `.gitkeep`). | Adicione ao `.gitignore` conforme necessário. |
| `templates/intel_briefing/template.md` | Base para relatórios rápidos ao SOC/exec. | Preencha com resumo, impacto e ações. |
| `templates/ioc_tracking/template.csv` | Estrutura para controle de ciclo de vida de IOCs. | Use para mapear status, score e consumidores. |
| `templates/adversary_profile/template.md` | Perfil resumido de atores (motivações, TTPs, histórico). | Atualize quando surgirem novas campanhas. |

### Execução guiada

1. **Preparar ambiente:** crie venv (`python3 -m venv .venv && source .venv/bin/activate`) e instale deps (`pip install -r scripts/requirements.txt`).
2. **Definir pergunta:** revise `docs/metodologia.md` e registre hipóteses + janela de coleta.
3. **Rodar pipeline inicial:** `python3 scripts/ti_collector.py --ioc-file data/examples/sample_intel_case.json --out data/outputs/sample_report.json`.
4. **Especializar:** avance para o playbook correspondente (IOCs, correlação ou hunting).
5. **Disseminar:** utilize os templates na pasta `templates/` e registre feedback para a próxima iteração.

### Testes e qualidade

- Dependências listadas em [scripts/requirements.txt](scripts/requirements.txt).
- Testes unitários em [`tests/test_ti_collector.py`](tests/test_ti_collector.py); execute com `pytest tests`.
- Configure `pre-commit` a partir do diretório raiz para validar Markdown e scripts.

## Próximos passos

- Integrar conectores STIX/TAXII autenticados.
- Criar notebooks de análise exploratória (DuckDB, pandas) para aceleração de hunting.
- Automatizar publicação de relatórios (S3, Confluence) via pipelines CI/CD.
