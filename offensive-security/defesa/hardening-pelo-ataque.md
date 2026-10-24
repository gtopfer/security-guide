# Hardening visto pelo ataque

Depois de estudar a classe ofensiva, inverta a pergunta: **cada hipótese vira um controle**. Isso fecha o ciclo deste guia (defesa em `for-noobs/`, ofensiva nesta pasta).

## Tabela de inversão (exemplos)

| Hipótese ofensiva | Controle preventivo | Controle detectivo |
|-------------------|---------------------|-------------------|
| Conta válida na VPN | MFA resistente a phishing e privilégio mínimo | Logon anômalo e localização impossível |
| Bucket listável | Bloqueio de ACL pública e política de controle de serviço | CloudTrail PutBucketAcl |
| XSS armazenado | Codificação de saída e CSP | WAF e relatório de CSP |
| IDOR | Autorização no servidor, por objeto | Log de acesso entre inquilinos |
| Segredo no Git | Hook de pre-commit, cofre e rotação | Gitleaks no CI (coleção OSINT) |
| Administrador local em massa | LAPS ou equivalente, e GPO | Inventário do grupo Administrators |
| Pipeline com privilégio alto | Proteção de branch e artefato assinado | Log do workflow |

## Linhas de base

CIS, STIG, ASVS no nível adequado ao risco, e o benchmark de nuvem. Não aplique o STIG inteiro no primeiro dia de uma organização pequena. Priorize a exposição à internet e a identidade.

## Pentest como verificação

O teste autorizado mede se a linha de base segurou. Um achado repetido no trimestre seguinte é falha de processo, não falha do scanner.

## Leitura seguinte

- [Detecção](deteccao-e-logs.md)
- [Fundamentos para iniciantes](../../for-noobs/README.md)
