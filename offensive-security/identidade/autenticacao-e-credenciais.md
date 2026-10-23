# Autenticação e credenciais

Identidade é o atalho favorito de atacantes reais: **usar uma conta válida** (ATT&CK T1078) muitas vezes supera exploit. Estude o ciclo de vida da credencial.

## Tipos

- **Senha / passphrase** — segredo memorizado; reuso é o buraco de stuffing.
- **Hash** — o que o sistema *guarda*. Algoritmo importa (lento + salt vs legado).
- **OTP / app / FIDO2** — segundo fator; SMS é fator fraco (SIM swap) — o guia [for-noobs](../../for-noobs/README.md) já fala disso para o usuário.
- **Certificado / chave** — mTLS, SSH, smart card.
- **Token de sessão / API key / PAT** — frequentemente vazam em git, CI, ticket.

## Ataques *como classes* (para threat model e defesa)

| Classe | Ideia | Controle típico |
|--------|--------|-----------------|
| Stuffing | Senha vazada em outro site | MFA, bloqueio, haveibeenpwned no onboarding (com ética) |
| Spraying | Poucas senhas, muitos usuários | MFA, lockout inteligente, detecção |
| Brute force | Muitas senhas, um alvo | Rate limit, MFA, senha longa |
| Phishing de credencial | Usuário entrega | FIDO2, awareness, DMARC |
| Replay / roubo de sessão | Cookie/token | rotação, binding, tempo de vida curto |
| Secret no código | Key no repo | scanning, vault, rotação |

Este repositório **não** ensina a executar stuffing/spray contra sistemas reais. Hydra e similares na coleção de pentest são para **lab autorizado**.

## Kerberos vs NTLM vs OAuth (mapa)

Três mundos: empresa Windows, legado, internet SaaS. Misturar (ADFS, Entra ID) cria *trust*. Estude o diagrama oficial do seu lab (Entra Connect, etc.) se for o seu contexto.

## MFA bypass *lógico* vs *canal*

Lógico: o reset de senha não exige o segundo fator; o cookie “remember” é eterno.  
Canal: interceptar SMS — fora do escopo ético típico e muitas vezes ilegal.

Foque estudos em **lógica de aplicação e IAM**.

## Segredos de máquina

Contas gMSA, roles IAM, workload identity (K8s). O erro clássico é humano copiar a mesma key em 40 jobs. Ver [CI/CD](../nuvem/cicd-e-supply-chain.md).

## Leitura seguinte

- [APIs](../web/apis-e-auth.md)
- [AD](active-directory-conceitos.md)
- NIST SP 800-63B (digital identity guidelines) — <https://pages.nist.gov/800-63-3/>
