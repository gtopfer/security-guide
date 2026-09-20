# Hardening visto pelo ataque

Depois de estudar classes ofensivas, inverta: **cada hipótese vira um controle**. Isso fecha o ciclo do Security Guide (defesa no `for-noobs`, ofensiva aqui).

## Tabela de inversão (exemplos)

| Hipótese ofensiva | Controle preventivo | Controle detetive |
|-------------------|---------------------|-------------------|
| Conta válida na VPN | MFA resistente a phishing, least privilege | Logon anômalo, geo impossível |
| Bucket listável | Block public ACLs, SCP | CloudTrail PutBucketAcl |
| XSS armazenado | Encoding, CSP | WAF + CSP report |
| IDOR | Authz no servidor por objeto | Log de acesso cross-tenant |
| Secret no Git | Pre-commit, vault, rotating | Gitleaks no CI (coleção OSINT) |
| Admin local em massa | LAPS/equivalente, GPO | Inventory de grupo Administrators |
| Pipeline poderoso | Branch protection, signed artifacts | Log de workflow |

## Baselines

CIS, STIG, ASVS nível adequado ao risco, CIS+cloud. Não aplique STIG inteiro em startup no dia 1 — priorize exposição internet e identidade.

## Pentest como verificação

O teste autorizado *mede* se o baseline pegou. Achado repetido no trimestre seguinte é falha de processo, não de scanner.

## Leitura seguinte

- [Detecção](deteccao-e-logs.md)
- [for-noobs](../../for-noobs/README.md)
