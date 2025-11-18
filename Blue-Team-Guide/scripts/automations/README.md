# Automations

Scripts/flows para orquestrar resposta e registros.

- `soar/` — playbooks TheHive/Cortex, Shuffle, StackStorm.
- `cli/` — scripts Python/PowerShell para tarefas imediatas (isolamento, coleta de evidências).
- `workflows/` — pipelines n8n/Prefect.

Boas práticas:
- Usar `.env.example` para secrets.
- Registrar logs estruturados (JSON) para auditoria.
- Cobrir funções críticas com testes unitários/mocks.
