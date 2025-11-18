# Playbook: Identity Hardening

## Objetivo
Reduzir superfície de ataque em identidades corporativas (AD/Azure AD/IdPs SaaS).

## Ações-chave
- Implementar MFA obrigatório com políticas adaptativas.
- Revisar privilégios/admins permanentes (PIM/PAM).
- Ativar proteção de token/cookies (Continuous Access Evaluation).
- Monitorar eventos críticos: logins suspeitos, MFA bypass, consent grants.
- Automatizar correções via scripts (`scripts/detections/` + `scripts/automations/`).

## Métricas
- % contas com MFA
- Tempo médio para revogar acesso comprometido
- Cobertura de detecções MITRE TA0006/TA0008
