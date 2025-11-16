# Threat Intelligence Tools Collection

Resumo de uso rápido para a coleção de Threat Intelligence.

Estrutura principal:

- `docs/` — metodologia, grupos e fluxos de coleta/enriquecimento.
- `scripts/` — `ti_collector.py` e módulos auxiliares.
- `templates/` — modelos de briefing, perfis e tracking.
- `data/examples/` — exemplos de casos e IOCs.
- `data/outputs/` — resultados de execuções (não versionar).

Como usar (exemplo):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r threat-intel-tools-collection/scripts/requirements.txt
python threat-intel-tools-collection/scripts/ti_collector.py --case threat-intel-tools-collection/data/examples/sample_intel_case.json
```

Variáveis de ambiente

- Copie `threat-intel-tools-collection/.env.example` para `.env` e preencha as credenciais necessárias.
- Não comprometa chaves sensíveis no repositório.

Testes

```bash
pytest -q threat-intel-tools-collection/tests
```

Execute `pre-commit run --all-files` antes de enviar PRs.
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
## Execução e passo a passo local

Siga estes passos para preparar e executar o fluxo de Threat Intelligence localmente.

1. Criar e ativar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instalar a coleção em modo editable (recomendado):

```bash
# a partir da raiz do repositório
pip install -e ./threat-intel-tools-collection
```

3. Preparar credenciais/variáveis (não versionar):

```bash
cp threat-intel-tools-collection/.env.example threat-intel-tools-collection/.env
# edite threat-intel-tools-collection/.env e preencha chaves/API keys necessárias
```

4. Executar o coletor e gerar relatório JSON:

```bash
ti-collector --ioc-file threat-intel-tools-collection/data/examples/sample_intel_case.json --out threat-intel-tools-collection/data/outputs/ioc_report.json
```

5. Verificar resultado e gerar briefing:

- O relatório JSON será salvo em `threat-intel-tools-collection/data/outputs/`.
- Utilize os templates em `threat-intel-tools-collection/templates/` para montar briefings e relatórios executivos.

6. Testes e qualidade:

```bash
# rodar testes locais da coleção
pytest -q threat-intel-tools-collection/tests

# rodar pre-commit hooks antes de abrir PR
pre-commit run --all-files
```

Observações:
- Nunca versionar `data/outputs/` nem arquivos `.env` com chaves sensíveis.
- Para depuração, o script também pode ser executado diretamente:

```bash
python threat-intel-tools-collection/scripts/ti_collector.py --ioc-file threat-intel-tools-collection/data/examples/sample_intel_case.json --out threat-intel-tools-collection/data/outputs/ioc_report.json
```
