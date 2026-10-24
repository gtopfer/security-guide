# Cliente: XSS, CSRF e confiança no navegador

O navegador executa JavaScript de várias origens, com regras. A ofensiva do lado do cliente **abusa da confiança que a pessoa tem no site**.

## XSS (Cross-Site Scripting)

A aplicação inclui na página um dado que o navegador interpreta como **script** ou como HTML perigoso, em vez de texto.

Famílias que você deve saber nomear:

- **Refletido** — vai e volta no mesmo pedido (link, busca).
- **Armazenado** — persiste (comentário, perfil) e atinge outras pessoas.
- **Baseado no DOM** — o JavaScript do próprio site lê `location` ou `innerHTML` de forma insegura.

Impacto conceitual: sessão, ação em nome da vítima, alteração visível da página e pivô para phishing interno. **HttpOnly** reduz o roubo de cookie. Não elimina o XSS.

Defesa conceitual: codificação conforme o contexto (HTML, atributo, JavaScript, URL), CSP como camada extra, sanitização definida e framework que escapa por padrão.

Estude CSP em <https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP>. Leia o que cada diretiva pretende. Este texto não descreve como contorná-la.

## CSRF (Cross-Site Request Forgery)

O navegador **já autenticado** no site A é induzido pelo site B a enviar um pedido para A. O cookie segue junto, conforme SameSite.

Defesa conceitual: token anti-CSRF, SameSite, não usar GET para mudar estado e preferir o cabeçalho Authorization (não o cookie) em API.

SameSite não encerra o tema: aplicativo legado, cookie `None` com `Secure` para SSO e fluxo de nível superior.

## Clickjacking e sobreposição de interface

Um iframe transparente fica sobre o botão. Defesa: `frame-ancestors` (CSP) ou X-Frame-Options. Entenda o problema de confirmar uma ação sem o contexto visual.

## Prototype pollution, postMessage e extensão

Temas avançados de JavaScript: objeto global, `postMessage` sem verificar `origin` e extensão de navegador com permissão ampla. Estude o **modelo de mensagem**. Não estude prova de conceito aqui.

## Cadeia típica (modelo de ameaça)

XSS no painel de administração, cookie sem HttpOnly e sessão longa formam impacto de conta. O relatório deve contar a **cadeia**, não um alerta isolado do scanner.

## Prática

A PortSwigger Web Security Academy (XSS e CSRF) é a referência gratuita, em laboratório isolado: <https://portswigger.net/web-security>

OWASP Juice Shop no seu Docker: veja [laboratórios legais](../pratica/labs-legais.md).

## Repositórios para aprofundar

[ZAP](https://github.com/zaproxy/zaproxy), [dalfox](https://github.com/hahwul/dalfox), [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) (seção XSS, para estudo), [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) (prevenção de XSS).

## Leitura seguinte

- [HTTP](modelo-http-e-sessao.md)
- [OWASP Top 10](owasp-top-10.md)
