# Playbook: Spear Phishing Chain

## Objetivo
Simular campanhas de spear phishing com entrega de payload (macro/HTML smuggling) visando comprometer contas privilegiadas.

## Fases
1. **Recon**: coletar targets e temas relevantes (exec sponsor, finanças).
2. **Preparação**: configurar infraestrutura (domínio lookalike, certificados, servidor SMTP ou GoPhish).
3. **Execução**: disparar lotes controlados, monitorar entregas e capturar credenciais/token.
4. **Pós-comprometimento**: estabelecer C2, mover-se lateralmente para sistemas críticos.

## Métricas
- Taxa de abertura/clique
- Credenciais capturadas
- Tempo até detecção

## Evidências
Salvar e-mails enviados, templates, payload hashes e cronologia em `evidences/spear_phish_<data>.md`.
