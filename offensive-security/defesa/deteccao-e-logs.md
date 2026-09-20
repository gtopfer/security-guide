# Detecção e logs — estudar ofensiva pelo lado blue

Se você só “entra no lab” e nunca pergunta **quem veria**, está treinando vandalismo, não pentest profissional. Purple team é o atalho de aprendizado.

## Telemetria mínima que o analista ofensivo deve conhecer

| Ambiente | Exemplos de pergunta |
|----------|----------------------|
| Windows | Logon (sucesso/falha), logon explícito, criação de serviço, PowerShell 4104, Sysmon se existir |
| Linux | auth/sudo, new user, systemd, auditd |
| AD | replicação, Kerberos anômalo, GPO, gold/silver *como ideia de IR* (não como tutorial) |
| Nuvem | CloudTrail: CreateUser, AttachPolicy, PutBucketAcl |
| Web | 401/403 em massa, user-agent de scanner, path de admin |
| E-mail | fail DMARC, anexos |

Sigma: regras genéricas — <https://github.com/SigmaHQ/sigma> (já apontado na coleção OSINT/CTI).

## ATT&CK para defesa

Cada técnica tem seção **Detections** e **Mitigations**. Estude *isso* tanto quanto a descrição ofensiva.

## O que o pentester deve entregar

Não só “achamos XSS”. Também: “não vimos alerta no WAF / o EDR não registrou o binário do lab”. Isso exige combinado no ROE (às vezes o teste é *stealth*, às vezes é *barulhento de propósito*).

## Logging failures (Top 10)

Falta de log é achado. Evidência: você fez ação ruidosa autorizada e o SIEM não tem evento. Documente horário — senão o SOC não consegue procurar.

## Leitura seguinte

- [Relatório](relatorio-e-comunicacao.md)
- [Taxonomias](../fundamentos/taxonomias-mitre-owasp-cwe.md)
