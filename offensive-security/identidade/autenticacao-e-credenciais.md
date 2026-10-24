# Autenticação e credenciais

A identidade é o atalho mais usado por atacante real: **usar uma conta válida** (ATT&CK T1078) muitas vezes supera um exploit. Estude o ciclo de vida da credencial.

## Tipos

- **Senha e frase-senha** — segredo memorizado. O reuso é a condição do credential stuffing.
- **Hash** — o que o sistema guarda. O algoritmo importa: função lenta com salt, ou algoritmo legado.
- **OTP, aplicativo e FIDO2** — segundo fator. O SMS é um fator fraco (troca de chip). O guia [para iniciantes](../../for-noobs/README.md) descreve isso para o usuário.
- **Certificado e chave** — mTLS, SSH e smart card.
- **Token de sessão, chave de API e token de acesso pessoal** — vazam com frequência em Git, CI e ticket.

## Ataques como classes (modelo de ameaça e defesa)

| Classe | Ideia | Controle típico |
|--------|--------|-----------------|
| Stuffing | Senha vazada em outro site | MFA, bloqueio e consulta ética a base de vazamento no cadastro |
| Spraying | Poucas senhas, muitos usuários | MFA, bloqueio inteligente e detecção |
| Força bruta | Muitas senhas, um alvo | Limite de taxa, MFA e senha longa |
| Phishing de credencial | O usuário entrega o segredo | FIDO2, orientação e DMARC |
| Replay e roubo de sessão | Cookie ou token | Rotação, vínculo ao cliente e tempo de vida curto |
| Segredo no código | Chave no repositório | Varredura, cofre e rotação |

Este repositório **não** ensina a executar stuffing ou spraying contra sistema real. Hydra e ferramentas semelhantes na coleção de pentest são para **laboratório autorizado**.

## Kerberos, NTLM e OAuth (mapa)

São três contextos: empresa Windows, protocolo legado e SaaS na internet. A mistura (ADFS, Entra ID) cria relação de confiança. Se esse for o seu contexto, estude o diagrama oficial do laboratório (Entra Connect, por exemplo).

## Contorno de MFA por lógica e por canal

Lógica: a redefinição de senha não exige o segundo fator, ou o cookie de "lembrar deste dispositivo" não expira.  
Canal: interceptar SMS. Isso fica fora do escopo ético usual e, em muitos casos, é ilegal.

Concentre o estudo na **lógica da aplicação e do IAM**.

## Segredo de máquina

Conta gMSA, função IAM e identidade de workload (Kubernetes). O erro clássico é copiar a mesma chave em dezenas de jobs. Veja [CI/CD](../nuvem/cicd-e-supply-chain.md).

## Leitura seguinte

- [APIs](../web/apis-e-auth.md)
- [AD](active-directory-conceitos.md)
- NIST SP 800-63B (*digital identity guidelines*) — <https://pages.nist.gov/800-63-3/>
