# Security-Guide

Hub de metodologias e automações de Segurança Ofensiva/Defensiva. Este repositório organiza duas coleções principais — **OSINT** e **Threat Intelligence** — com documentação navegável, scripts Python e templates de dados.

## Objetivos

- Padronizar investigações (escopo → coleta → enriquecimento → relatório) sem depender de ferramentas externas proprietárias.  
- Manter scripts versionados com requisitos claros (`scripts/requirements.txt`, `pytest tests`).  
- Facilitar o reuso de templates `.env`, relatórios e checklists durante operações reais.

## Estrutura

| Diretório | Conteúdo | Entrada recomendada |
|-----------|----------|---------------------|
| [`OSINT tools collection/`](OSINT%20tools%20collection/README.md) | Playbooks de coleta aberta, scripts automatizados e templates `.env`. | Leia o README local para navegar por `docs/`, `scripts/`, `data/`, `templates/`. |
| [`Threat Intelligence tools collection/`](Threat%20Intelligence%20tools%20collection/README.md) | Pipelines de TI (coleta, enriquecimento, correlação, disseminação) + conectores e templates STIX/TAXII. | Comece pelo README local e siga para `docs/`, `scripts/ti_collector.py` e `templates/`. |

## Como usar o repositório

1. **Preparar o ambiente**  
   - Linux/WSL com Python 3.10+, `pip install -r scripts/requirements.txt` em cada coleção.  
   - Segredos ficam fora do repo; crie arquivos `.env` a partir de `templates/` e adicione ao `.gitignore`.
2. **Escolher o domínio**  
   - OSINT: foco em rastreio público (domínios, perfis, infraestrutura).  
   - Threat Intel: perguntas táticas/estratégicas, ingestão de IOCs, relatórios para SOC/Executivos.
3. **Seguir o fluxo indicado** nos READMEs locais (metodologia → playbooks → scripts → dados).  
4. **Registrar resultados** em `data/outputs/` (não versionado) e usar os templates de relatório/disseminação.

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
