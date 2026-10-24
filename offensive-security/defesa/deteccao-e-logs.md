# Detecção e logs: estudar a ofensiva pelo lado da defesa

Se você entra no laboratório e não pergunta **quem veria o evento**, o treino não é um pentest profissional. O purple team é o caminho curto de aprendizado.

## Telemetria mínima que o analista ofensivo deve conhecer

| Ambiente | Exemplos de pergunta |
|----------|----------------------|
| Windows | Logon (sucesso e falha), logon explícito, criação de serviço, PowerShell 4104, Sysmon se existir |
| Linux | auth e sudo, usuário novo, systemd, auditd |
| AD | replicação, Kerberos anômalo, GPO, ticket anômalo como tema de resposta a incidente (não como tutorial) |
| Nuvem | CloudTrail: CreateUser, AttachPolicy, PutBucketAcl |
| Web | 401 e 403 em massa, user-agent de scanner, caminho de administração |
| E-mail | falha de DMARC, anexo |

Sigma: regras genéricas — <https://github.com/SigmaHQ/sigma> (também na coleção OSINT e de CTI).

## Repositórios de purple team

[Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), [CALDERA](https://github.com/mitre/caldera), [Wazuh](https://github.com/wazuh/wazuh), [HELK](https://github.com/Cyb3rWard0g/HELK), [falco](https://github.com/falcosecurity/falco). Tabela: [coleção de pentest — purple team](../../pentest-tools-collection/README.md#purple-team-detecção-e-emulação).

## ATT&CK para defesa

Cada técnica tem as seções **Detections** e **Mitigations**. Estude essas seções tanto quanto a descrição ofensiva.

## O que o pentester entrega

Não entregue só "encontramos XSS". Entregue também: "não vimos alerta no WAF" ou "o EDR não registrou o binário do laboratório". Isso exige acordo nas regras de engajamento. Às vezes o teste é discreto. Às vezes o teste é ruidoso de propósito.

## Falha de registro (Top 10)

A falta de log é um achado. A evidência é esta: você executou uma ação ruidosa e autorizada, e o SIEM não tem o evento. Documente o horário. Sem o horário, o SOC não consegue procurar.

## Leitura seguinte

- [Relatório](relatorio-e-comunicacao.md)
- [Taxonomias](../fundamentos/taxonomias-mitre-owasp-cwe.md)
