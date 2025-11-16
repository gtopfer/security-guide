# Playbook: Correlação de alertas e telemetria

## Escopo

Conectar eventos de múltiplas fontes (SIEM, EDR, NDR, proxies, CASB) com inteligência consumível para priorizar resposta.

## Pipeline sugerido

1. **Ingestão** – utilize conectores do SIEM ou exportações em lote (`csv`, `cef`, `json`) para trazer alertas recentes.
2. **Enriquecimento** – alimente os campos críticos (IP, domínio, hash, usuário) em `scripts/ti_collector.py --detection-type alert` para anexar score de risco.
3. **Agrupamento temporal** – crie janelas de 15/60/240 minutos para unir eventos relacionados a mesma entidade.
4. **Contexto adversário** – verifique se há sobreposição com clusters internos, campanhas públicas ou TTPs monitorados.
5. **Saída** – gere um briefing tático (ver template `templates/intel_briefing/template.md`) e abra ticket no ITSM/Case Management.

## Métricas chave

- % de alertas com inteligência contextualizada.
- Tempo médio entre alerta e recomendação acionável.
- Volume de falsos positivos detectados pela correlação.
- Feedback dos analistas SOC sobre clareza e utilidade.
