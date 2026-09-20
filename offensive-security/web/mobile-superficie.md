# Mobile (Android / iOS) — superfície para estudo

O celular concentra sessão de banco, MFA e e-mail. Ofensiva mobile ética é **AppSec + plataforma**, não “clonar WhatsApp da vítima”.

## Modelo

- App = binário + dados locais + IPC + backend (a API ainda é [web/API](../web/apis-e-auth.md)).
- Store (Play/App Store) reduz, não elimina, malware e apps abusivos.
- Root/jailbreak no aparelho do dia a dia remove mitigação — o [for-noobs](../../for-noobs/README.md) já recomenda não fazer isso no telefone pessoal.

## Android (conceitos)

- UID por app, permissões, intents, backup, armazenamento interno vs externo.
- WebView: XSS vira bridge para o app.
- Certificate pinning *como ideia* (trust no TLS); pinning mal feito quebra interceptação *legítima* de lab.

## iOS (conceitos)

- Sandbox mais rígido; Keychain; ATS (App Transport Security).
- Enterprise sideload e perfis de MDM — superfície corporativa.

## OWASP MASVS / MASTG

Padrão de estudo: <https://mas.owasp.org/> — requisitos e testes. Execute testes só no **seu** app ou lab.

## O que não fazer

Interceptar tráfego de app de terceiro na rede alheia, implantar spyware, bypass de biometria em aparelho que não é seu.

## Leitura seguinte

- [APIs](../web/apis-e-auth.md)
- [for-noobs: mobile](../../for-noobs/README.md)
