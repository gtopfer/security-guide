# Playbook: Coleta e curadoria de IOCs

## Objetivo

Criar pipeline repetível para ingestão, validação e distribuição de indicadores (domínios, IPs, hashes, URLs) com metadados suficientes para ação rápida.

## Passo a passo

1. **Inventariar fontes** – liste nome do feed, owner, SLA, formato e credenciais.
2. **Automatizar ingestão** – configure `scripts/automation/Makefile.threatintel` para baixar/atualizar coleções diariamente.
3. **Normalizar** – utilize `scripts/ti_collector.py --detection-type ioc` para remover duplicados, preencher tags ATT&CK e calcular score.
4. **Analisar contexto** – cruze os indicadores com dados internos (telemetria SOC, varreduras) e marque aqueles já observados.
5. **Publicar** – exporte para STIX/TAXII, CSV sanitizado e blocos de regra (SIEM/EDR). Documente owner responsável pela disseminação.

## Controles mínimos

- Salve o log da coleta (timestamp, status HTTP, tamanho do arquivo).
- Documente termos de uso dos feeds pagos e a duração das credenciais.
- Rode verificação de integridade (hash) dos arquivos antes de carregar no data lake.
- Implemente testes de fumaça (conteúdo esperado) antes de mover o arquivo para produção.
