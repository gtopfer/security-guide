# Detections

Armazene consultas Sigma, KQL, SPL e YARA-L para monitoração contínua.

Estrutura sugerida:
- `sigma/`: regras Sigma + conversões.
- `kql/`: caças e alertas para Microsoft Sentinel.
- `spl/`: buscas Splunk prontas para agendamento.
- `tests/`: dados sintéticos para validação (`pytest + pytest-splunk-addon`).

Inclua metadata (autor, data, MITRE) em cada arquivo.
