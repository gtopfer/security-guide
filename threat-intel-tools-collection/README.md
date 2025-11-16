# Threat Intelligence Tools Collection

Portal para metodologias, scripts e templates de Threat Intelligence. Use este diretório como guia único: todo o conteúdo que antes estava segmentado em `docs/` e `docs/grupos/` agora está resumido abaixo para consulta rápida.

## 📖 Índice

- [Estrutura principal](#estrutura-principal)
- [Configuração rápida](#configuração-rápida)
- [Visão geral](#visão-geral)
- [Metodologia de Threat Intelligence](#metodologia-de-threat-intelligence)
- [Playbooks operacionais](#playbooks-operacionais)
- [Ferramentas essenciais para Threat Intelligence em Linux](#ferramentas-essenciais-para-threat-intelligence-em-linux)
- [Scripts e automações](#scripts-e-automações)
- [Dados e templates](#dados-e-templates)
- [Execução guiada](#execução-guiada)
- [Testes e qualidade](#testes-e-qualidade)
- [Observações e melhores práticas](#observações-e-melhores-práticas)

## Estrutura principal

- `docs/` — metodologia, grupos e fluxos de coleta/enriquecimento.
- `scripts/` — `ti_collector.py` e módulos auxiliares.
- `templates/` — modelos de briefing, perfis e tracking.
- `data/examples/` — exemplos de casos e IOCs.
- `data/outputs/` — resultados de execuções (não versionar).

## Configuração rápida

### Ambiente virtual e dependências

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r threat-intel-tools-collection/scripts/requirements.txt
```

### Execução básica do coletor

```bash
python threat-intel-tools-collection/scripts/ti_collector.py \
  --case threat-intel-tools-collection/data/examples/sample_intel_case.json
```

### Variáveis de ambiente

- Copie `threat-intel-tools-collection/.env.example` para `.env` e preencha as credenciais necessárias.
- Não comprometa chaves sensíveis no repositório; mantenha-as fora do versionamento.

### Instalação em modo editable

```bash
pip install -e ./threat-intel-tools-collection
```

### CLI `ti-collector`

```bash
ti-collector \
  --ioc-file threat-intel-tools-collection/data/examples/sample_intel_case.json \
  --out threat-intel-tools-collection/data/outputs/ioc_report.json
```

### Testes rápidos

```bash
pytest -q threat-intel-tools-collection/tests
pre-commit run --all-files
```

## Visão geral

- **Stack:** Python 3.10+, Makefiles e documentação Markdown focada em Linux.
- **Fluxo principal:** Metodologia → coleta/enriquecimento → correlação → disseminação.
- **Governança:** dados sensíveis ficam fora do repo. Utilize os templates `.env`/CSV para padronizar variáveis e mantenha histórico de decisões em Issues/PRs.

## Metodologia de Threat Intelligence

### 1. Preparação e escopo

- Defina a pergunta de inteligência (tática, operacional ou estratégica) e mapeie os stakeholders responsáveis pela decisão.
- Estabeleça janelas de coleta, sensibilidade dos dados e controles legais (LGPD, SLAs ou acordos com fornecedores).
- Catalogue fontes internas disponíveis (EDR, SIEM, fluxos de incidentes) e dependências externas (ISAC, parceiros, feeds comerciais).

### 2. Coleta e enriquecimento

- Combine fontes abertas, comerciais e dados proprietários; documente formatos suportados (STIX/TAXII, JSON, CSV) e limites de uso.
- Automatize a ingestão com conectores (TAXII, APIs REST, buckets S3) e salve logs das execuções para auditoria.
- Enriqueca IOCs com metadados (timestamp, primeiro/último avistamento, TTPs MITRE ATT&CK) antes de consolidar.

### 3. Normalização e scoring

- Normalize campos (tipo de IOC, confiança, fonte) para suportar correlação e descarte duplicados.
- Calcule score composto usando peso por fonte + relevância para o ambiente.
- Estruture dados para consumo downstream (SIEM, playbooks SOAR, dashboards) e mantenha versionamento.

### 4. Correlação e hipóteses

- Aplique regras de associação (cluster de infraestrutura, sobreposição de TTPs) para conectar eventos.
- Busque evidências da cadeia completa de ataque e valide contra a linha de base do ambiente.
- Documente hipóteses, falsos positivos e lacunas que precisam de coleta adicional.

### 5. Disseminação e feedback

- Produza produtos orientados ao público correto: alertas rápidos, relatórios executivos ou pacotes para Red Team.
- Defina ações recomendadas (bloqueio, regra SIEM/EDR, awareness) e quem valida cada ação.
- Ao fechar o ciclo, colete feedback dos consumidores e atualize os requisitos da próxima iteração.

#### Checklist rápido

- [ ] Escopo, janela de coleta e controles legais documentados.
- [ ] Fontes catalogadas (owner, SLA, formato, custo).
- [ ] Regras de normalização e scoring publicadas.
- [ ] Processos de disseminação e confidencialidade definidos.
- [ ] Métricas de qualidade (tempo médio, taxa de ação aplicada) acompanhadas.

#### Referências úteis

- [MITRE ATT&CK](https://attack.mitre.org/)
- [ENISA Threat Landscape](https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends)
- [FIRST CTI SIG](https://www.first.org/global/sigs/cti)

## Playbooks operacionais

### Coleta e curadoria de IOCs

**Objetivo:** pipeline repetível para ingestão, validação e distribuição de indicadores (domínios, IPs, hashes, URLs) com metadados suficientes para ação rápida.

**Passo a passo:**

1. Inventariar fontes — nome do feed, owner, SLA, formato e credenciais.
2. Automatizar ingestão — configure `scripts/automation/Makefile.threatintel` para baixar/atualizar coleções diariamente.
3. Normalizar — use `scripts/ti_collector.py --detection-type ioc` para remover duplicados, aplicar tags ATT&CK e calcular score.
4. Analisar contexto — cruze com dados internos (telemetria SOC, varreduras) e marque indicadores já observados.
5. Publicar — exporte para STIX/TAXII, CSV sanitizado e blocos de regra (SIEM/EDR), registrando o responsável pela disseminação.

**Controles mínimos:**

- Salvar o log da coleta (timestamp, status HTTP, tamanho do arquivo).
- Documentar termos de uso dos feeds pagos e validade das credenciais.
- Rodar verificação de integridade (hash) antes de carregar no data lake.
- Executar testes de fumaça (conteúdo esperado) antes de mover para produção.

### Correlação de alertas e telemetria

**Escopo:** conectar eventos de múltiplas fontes (SIEM, EDR, NDR, proxies, CASB) com inteligência consumível para priorizar resposta.

**Pipeline sugerido:**

1. Ingestão — utilize conectores do SIEM ou exportações (`csv`, `cef`, `json`) para trazer alertas recentes.
2. Enriquecimento — envie campos críticos (IP, domínio, hash, usuário) para `scripts/ti_collector.py --detection-type alert` e anexe score de risco.
3. Agrupamento temporal — crie janelas de 15/60/240 minutos para unir eventos relacionados.
4. Contexto adversário — verifique sobreposição com clusters internos, campanhas públicas ou TTPs monitorados.
5. Saída — gere briefing tático (template `templates/intel_briefing/template.md`) e abra ticket no ITSM/Case Management.

**Métricas chave:**

- Percentual de alertas com inteligência contextualizada.
- Tempo médio entre alerta e recomendação acionável.
- Volume de falsos positivos detectados pela correlação.
- Feedback dos analistas SOC sobre clareza e utilidade.

### Threat hunting orientado por inteligência

**Objetivo:** transformar hipóteses derivadas de inteligência (TTPs, clusters, campanhas) em buscas proativas dentro do ambiente corporativo.

**Etapas:**

1. Selecionar hipótese — derive de relatórios estratégicos ou indicadores com alta relevância para o setor.
2. Traduzir para sinais técnicos — identifique eventos, campos e fontes necessários (process creation, DNS logs, proxy, AD).
3. Construir consultas — utilize KQL, SPL ou SQL conforme a plataforma e documente no repositório de detecções.
4. Executar e registrar — salve resultados, horário de execução e datasets utilizados para rastreabilidade.
5. Avaliar resultado — classifique achados (positivo, falso positivo, falta de dados) e gere ações corretivas.

**Boas práticas:**

- Priorize hipóteses alinhadas ao threat model local e mantenha backlog com pontuação de impacto.
- Sincronize com SOC/CSIRT para evitar sobreposição com incidentes em andamento.
- Capture aprendizados em `templates/ioc_tracking/template.csv` para alimentar campanhas futuras.

## Ferramentas essenciais para Threat Intelligence em Linux

### Ambiente base

1. **Sistema:** Ubuntu 22.04 LTS (ou distro equivalente) com kernel atualizado e suporte a containers.
2. **Python:** versão 3.10+ gerenciada com `pyenv` ou `asdf` para múltiplos runtimes.
3. **Containers:** Docker/Podman + Compose para subir feeds locais ou instâncias OpenCTI.

### Pacotes obrigatórios

| Categoria | Pacotes/Projetos | Observações |
|-----------|------------------|-------------|
| STIX/TAXII | `cti-toolkit`, `stix2`, `cabby` | Conversão e publicação de coleções STIX 2.1. |
| Enriquecimento | `ioc-fanger`, `urlscan`, `ipwhois`, `shodan` | Scripts CLI rápidos para contexto adicional. |
| Data wrangling | `pandas`, `duckdb`, `jq`, `miller` | Tratamento de grandes volumes de IOCs. |
| Visualização | `kibana`, `grafana`, `maltiverse`, `maltego` | Exploração gráfica de indicadores e relacionamentos. |
| Automação | `poetry`, `make`, `pre-commit`, `invoke` | Padroniza execução e empacotamento. |

### Boas práticas de hardening

- Utilize usuários dedicados para serviços (OpenCTI, MISP, Redis) e armazene secrets em Vault ou Pass.
- Configure `ufw`/`nftables` minimizando portas expostas dos feeds internos.
- Habilite registro detalhado (`auditd`, `journald`) para rastrear acesso a dados sensíveis.
- Prefira `pipx` para instalar CLIs de terceiros e evitar poluir ambientes do projeto.

### Dicas operacionais

- Automatize atualizações de taxonomias (MITRE, CAPEC) via `cron` ou GitHub Actions.
- Para notebooks colaborativos, use VS Code Remote ou JupyterLab com autenticação SSO.
- Registre sempre a origem e o contrato associado ao feed para facilitar auditoria e renovação.

## Scripts e automações

| Recurso | Descrição | Próximo passo |
|---------|-----------|---------------|
| [scripts/ti_collector.py](scripts/ti_collector.py) | Normaliza IOCs/alertas, remove duplicados e gera sumários JSON. | Use junto ao `data/examples/sample_intel_case.json` para testar. |
| `scripts/enrich/` | Espaço para conectores (API TAXII, Shodan, VirusTotal). Inclui `.gitkeep`. | Adicione módulos conforme integrações forem aprovadas. |
| [scripts/automation/Makefile.threatintel](scripts/automation/Makefile.threatintel) | Tarefas padronizadas (`make lint`, `make collect`, `make report`). | Rode `make help` para ver os comandos disponíveis. |

## Dados e templates

| Caminho | Conteúdo | Observações |
|---------|----------|-------------|
| [data/examples/sample_intel_case.json](data/examples/sample_intel_case.json) | Caso exemplo com indicadores e ações recomendadas. | Útil para testar pipelines locais. |
| `data/outputs/` | Destino padrão para resultados reais (mantém `.gitkeep`). | Adicione ao `.gitignore` conforme necessário. |
| `templates/intel_briefing/template.md` | Base para relatórios rápidos ao SOC/exec. | Preencha com resumo, impacto e ações. |
| `templates/ioc_tracking/template.csv` | Estrutura para controle de ciclo de vida de IOCs. | Use para mapear status, score e consumidores. |
| `templates/adversary_profile/template.md` | Perfil resumido de atores (motivações, TTPs, histórico). | Atualize quando surgirem novas campanhas. |

## Execução guiada

1. **Preparar ambiente:** crie venv (`python3 -m venv .venv && source .venv/bin/activate`) e instale dependências (`pip install -r scripts/requirements.txt`).
2. **Definir pergunta:** use a metodologia acima para registrar hipóteses e janela de coleta.
3. **Rodar pipeline inicial:** `python3 scripts/ti_collector.py --ioc-file data/examples/sample_intel_case.json --out data/outputs/sample_report.json`.
4. **Especializar:** avance para o playbook correspondente (IOCs, correlação ou hunting) e utilize os templates adequados.
5. **Disseminar e medir:** armazene resultados em `data/outputs/`, gere briefing (template `intel_briefing`) e capture feedback para a próxima iteração.

Para depuração ou execução direta, também é possível chamar:

```bash
python threat-intel-tools-collection/scripts/ti_collector.py \
  --ioc-file threat-intel-tools-collection/data/examples/sample_intel_case.json \
  --out threat-intel-tools-collection/data/outputs/ioc_report.json
```

## Testes e qualidade

- Dependências listadas em [scripts/requirements.txt](scripts/requirements.txt).
- Testes unitários em [`tests/test_ti_collector.py`](tests/test_ti_collector.py); execute `pytest -q threat-intel-tools-collection/tests`.
- Configure `pre-commit` a partir do diretório raiz para validar Markdown e scripts.

## Observações e melhores práticas

- Nunca versionar `data/outputs/` nem arquivos `.env` com chaves sensíveis.
- Registre owner e ciclo de vida de cada feed/templates para auditoria.
- Adapte os playbooks conforme maturidade do time e mantenha métricas de eficácia atualizadas.
