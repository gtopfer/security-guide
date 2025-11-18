# Arquitetura Defensiva

## Camadas
1. **Coleta** — agentes (EDR, Sysmon, auditd) enviando para um data lake central.
2. **Ingestão** — pipelines (Logstash, Fluentd, Kinesis) aplicando normalização (ECS/ASIM).
3. **Armazenamento/SIEM** — Splunk, Elastic, Sentinel ou OpenSearch SIEM.
4. **Detecção** — motores Sigma/KQL/SPL + UEBA.
5. **Resposta** — SOAR (Shuffle, StackStorm, TheHive/Cortex), playbooks automatizados.
6. **Observabilidade** — métricas, tracing e dashboards de saúde.

## Considerações
- Usar infraestrutura como código para replicar ambientes.
- Segmentar dados sensíveis (PII) e aplicar retenção adequada.
- Integrar fontes externas (Threat Intel) apenas via conectores auditáveis.
