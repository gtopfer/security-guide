# Playbook: Threat hunting orientado por inteligência

## Objetivo

Transformar hipóteses derivadas de inteligência (TTPs, clusters, campanhas) em buscas proativas dentro do ambiente corporativo.

## Etapas

1. **Selecionar hipótese** – derive de relatórios estratégicos ou indicadores com alta relevância para o setor.
2. **Traduzir para sinais técnicos** – identifique eventos, campos e fontes necessárias (Process Creation, DNS Logs, Proxy, AD).
3. **Construir consultas** – utilize KQL, SPL ou SQL de acordo com a plataforma; documente as consultas no repositório de detecções.
4. **Executar e registrar** – salve resultados, hora da execução e datasets utilizados para rastreabilidade.
5. **Avaliar resultado** – classifique achados (positivo, falso positivo, necessidade de mais dados) e gere ações corretivas.

## Boas práticas

- Priorize hipóteses alinhadas ao threat model local e mantenha backlog com pontuação de impacto.
- Sincronize com SOC/CSIRT para evitar sobreposição com incidentes em andamento.
- Capture aprendizados em `templates/ioc_tracking/template.csv` para alimentar futuras campanhas.
