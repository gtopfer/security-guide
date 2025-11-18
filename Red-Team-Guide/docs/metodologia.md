# Metodologia Red Team

## 1. Preparação
- Definir objetivo estratégico, escopo e regras de engajamento (ROE).
- Mapear superfícies e capacidades defensivas do alvo (Threat Intel, MITRE ATT&CK coverage).
- Provisionar infra segura para C2, staging e exfiltração controlada.

## 2. Emulação Adversária
- Selecionar TTPs alinhadas a adversários/referências (ex.: FIN7, APT29).
- Construir matriz de fases: Recon → Initial Access → Execution → Persistence → Lateral Movement → Collection → Exfiltration.
- Utilizar ferramentas documentadas (C2 frameworks, payload builders) com versionamento.

## 3. Execução Controlada
- Coletar evidências, timestamps e telemetria de cada TTP executada.
- Registrar desvios e improvisações para ajustar playbooks.
- Adotar canais de comunicação seguros (Slack/Matrix segregado, PGP).

## 4. Pós-operação
- Consolidar achados, impacto e recomendações acionáveis.
- Atualizar MITRE mapping (`docs/mitre-mapping.md`).
- Criar pacotes de aprendizado para Blue/Purple Teams.
