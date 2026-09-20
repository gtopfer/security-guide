# Cliente: XSS, CSRF e confiança no browser

O browser é um SO de documentos: executa JS de várias origens com regras. Ofensiva de *client-side* é sobre **abusar da confiança que o usuário tem no site**.

## XSS (Cross-Site Scripting) — classe

A aplicação inclui na página dado que o browser interpreta como **script** (ou HTML perigoso), em vez de texto.

Famílias que você deve saber *nomear*:

- **Refletido** — vai e volta no mesmo request (link, busca).
- **Armazenado** — persiste (comentário, perfil) e atinge outros.
- **DOM-based** — o JS do próprio site lê `location`/`innerHTML` de forma insegura.

Impacto conceitual: sessão, ações em nome da vítima, defacement, pivô para phishing interno. **HttpOnly** reduz roubo de cookie, não o XSS.

Defesa conceitual: encoding de contexto (HTML vs attr vs JS vs URL), CSP como *camada extra*, sanitização bem definida, frameworks que escapam por padrão.

Estude CSP em <https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP> — o que cada diretiva *pretende*, não como furá-la.

## CSRF (Cross-Site Request Forgery)

O browser **já autenticado** em A é induzido por um site B a mandar um pedido para A (cookie vai junto, conforme SameSite).

Defesa conceitual: token anti-CSRF, SameSite, não usar GET para mudar estado, Preferência por Authorization header (não cookie) em APIs.

SameSite não mata o tema: apps legado, cookies None+Secure para SSO, e fluxos top-level.

## Clickjacking e UI redress

Iframe transparente sobre botão. Defesa: `frame-ancestors` (CSP) / X-Frame-Options. Entenda o problema de *confirmar ação* sem contexto visual.

## Prototype pollution, postMessage, extensões

Temas avançados de JS: objetos globais, `postMessage` sem checar `origin`, extensões de browser com permissões largas. Estude o **modelo de mensagem**, não PoCs.

## Cadeia típica (para threat model)

XSS em painel admin + falta de HttpOnly + sessão longa = impacto de conta. O relatório deve contar a **cadeia**, não um alerta isolado do scanner.

## Prática

PortSwigger Web Security Academy (XSS, CSRF) é o padrão de ouro gratuito, em labs isolados: <https://portswigger.net/web-security>

OWASP Juice Shop no seu Docker: ver [labs legais](../pratica/labs-legais.md).

## Leitura seguinte

- [HTTP](modelo-http-e-sessao.md)
- [OWASP Top 10](owasp-top-10.md)
