# Labs Red Team

| Lab | Descrição | Stack |
|-----|-----------|-------|
| `labs/adversary-emulation/azure-spear-phish` | Provisiona tenant Azure + vítimas simuladas para campanhas de phishing. | Terraform + Azure CLI + GoPhish. |
| `labs/detection-bypass/edr-evasion` | Testa payloads e técnicas para evadir EDR comerciais. | VMs Windows + Sliver/Brute Ratel. |

## Diretrizes
- Utilize infraestrutura descartável; nunca reaproveite domínios/certificados em operações reais.
- Versione apenas código/instruções (sem segredos). Variáveis sensíveis → `.env.example`.
- Documente pré-requisitos de custo e tempo de montagem.
