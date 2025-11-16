# Security-Guide

[![CI](https://github.com/gtopfer/O11y/actions/workflows/ci.yml/badge.svg)](https://github.com/gtopfer/O11y/actions/workflows/ci.yml)

Hub de metodologias e automações de Segurança Ofensiva/Defensiva. Este repositório organiza duas coleções principais — **OSINT** e **Threat Intelligence** — com documentação navegável, scripts Python e templates de dados.

## Objetivos

- Padronizar investigações (escopo → coleta → enriquecimento → relatório) sem depender de ferramentas externas proprietárias.  
- Manter scripts versionados com requisitos claros (`scripts/requirements.txt`, `pytest tests`).  
- Facilitar o reuso de templates `.env`, relatórios e checklists durante operações reais.

## Estrutura

| Diretório | Conteúdo | Entrada recomendada |
|-----------|----------|---------------------|
| [`osint-tools-collection/`](osint-tools-collection/README.md) | Playbooks de coleta aberta, scripts automatizados e templates `.env`. | Leia o README local para navegar por `docs/`, `scripts/`, `data/`, `templates/`. |
| [`threat-intel-tools-collection/`](threat-intel-tools-collection/README.md) | Pipelines de TI (coleta, enriquecimento, correlação, disseminação) + conectores e templates STIX/TAXII. | Comece pelo README local e siga para `docs/`, `scripts/ti_collector.py` e `templates/`. |

## Como usar o repositório
1. **Passo a passo (início → fim)**

Siga este roteiro para executar uma investigação completa usando as coleções do repositório.

Pré-requisitos:
- Sistema Linux/WSL ou similar
- Python 3.10+ instalado
- `git` configurado

Passos:

1. Clone o repositório e entre na pasta:

```bash
git clone https://github.com/gtopfer/O11y.git
cd O11y/Security-Guide
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale apenas a coleção que vai usar (recomendado) em modo editable:

```bash
# Para OSINT
pip install -e ./osint-tools-collection

# Para Threat Intelligence
pip install -e ./threat-intel-tools-collection
```

Obs: instalar apenas a coleção necessária reduz dependências e acelera testes. Se preferir, instale as duas coleções.

4. Preparar credenciais e variáveis: copie os exemplos de `.env` e atualize com valores reais (local fora do repo):

```bash
cp osint-tools-collection/.env.example osint-tools-collection/.env
cp threat-intel-tools-collection/.env.example threat-intel-tools-collection/.env
# Edite os arquivos e preencha chaves de APIs se necessário
```

5. Executar a coleta inicial (OSINT):

```bash
osint-collector --target example.com --out osint-tools-collection/data/outputs/example.json --artifacts-dir osint-tools-collection/data/artifacts/example
```

6. Executar a normalização/relatório (Threat Intel):

```bash
ti-collector --ioc-file threat-intel-tools-collection/data/examples/sample_intel_case.json --out threat-intel-tools-collection/data/outputs/ioc_report.json
```

7. Validar saídas e artifacts:

- Os JSONs de saída ficam em `data/outputs/` (cada coleção tem seu próprio subdiretório não versionado).  
- Artefatos brutos (HTML, certificados, robots.txt) ficam em `data/artifacts/<alvo>` quando `--artifacts-dir` é usado.

8. Testes e qualidade:

```bash
# Rodar testes unitários da coleção
pytest -q osint-tools-collection/tests
pytest -q threat-intel-tools-collection/tests

# Rodar pre-commit hooks antes de abrir PR
pre-commit run --all-files
```

9. Gerar relatório final e anexar evidências:

- Combine as saídas relevantes em um briefing utilizando os templates em `threat-intel-tools-collection/templates` ou `osint-tools-collection/templates`.

10. Submeter mudanças e resultados:

- Commit das mudanças relevantes (ex.: novos exemplos sanitized em `data/examples/`) e abrir PR seguindo o template de PR.

Dicas rápidas:
- Nunca versionar `data/outputs/` nem arquivos `.env` com chaves. Use `data/examples/` para exemplos sanitizados.
- Use `pip install -e .` dentro da pasta da coleção para expor somente os comandos daquela coleção.


## Convenções e boas práticas

- Documentação em `docs/` sempre começa por uma metodologia macro e deriva para playbooks temáticos (`docs/grupos/*`).  
- Scripts Python devem expor CLI simples e testes em `tests/`. Execute `pytest` antes de qualquer PR.  
- Use os Makefiles dos diretórios `scripts/automation/` para rodar tarefas (`make collect`, `make report`, etc.).  
- Integrar APIs pagas (Shodan, Censys, TAXII) exige módulos em `scripts/enrich/` com `README.md` descrevendo parâmetros.  
- Dados sensíveis nunca vão para o Git; utilize `data/outputs/` e copie apenas exemplos anonimizados para `data/examples/`.

## Próximos passos sugeridos

- Criar notebooks de exploração (Jupyter/DuckDB) consumindo `data/examples/` para acelerar análises.  
- Conectar pipelines CI/CD (GitHub Actions) para lint/test das coleções sempre que scripts forem alterados.  
- Expandir a biblioteca de templates (`templates/*`) com briefings executivos, runbooks e planilhas de rastreio.  
- Revisar periodicamente os READMEs das coleções ao adicionar novos playbooks ou dependências.
