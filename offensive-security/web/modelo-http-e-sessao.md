# HTTP, cookies e sessão

Quase toda segurança ofensiva de aplicação começa em **como o protocolo trata estado e identidade**. Sem isso, "vulnerabilidade web" não tem definição operacional.

## Pedido e resposta

HTTP é uma mensagem: método, caminho, cabeçalho e corpo. O servidor decide. O cliente (navegador ou `curl`) apenas propõe. Um controle que existe **somente no JavaScript** é uma indicação para a interface. Não é segurança.

Conceitos para estudar até ficarem estáveis:

- Métodos: GET é idempotente na teoria. POST, PUT, PATCH e DELETE mudam estado.
- Códigos: 2xx é sucesso, 3xx é redirecionamento (open redirect vive aqui), 4xx é cliente e 5xx é servidor.
- Cabeçalhos de segurança: `Content-Security-Policy`, `Set-Cookie` (atributos), `Authorization` e CORS (`Access-Control-*`).
- HTTP/2 e HTTP/3 mudam o transporte. A semântica da aplicação continua sendo recurso e autorização.

Material: RFC 9110 (HTTP Semantics) é densa, e é a fonte. O MDN é mais direto: <https://developer.mozilla.org/en-US/docs/Web/HTTP>

## Cookies e atributos

O cookie é armazenamento que o navegador **anexa depois**, segundo regras de domínio e de caminho.

Estude o significado de:

- **HttpOnly** — o JavaScript não lê o cookie. Isso reduz o roubo via XSS. Não elimina o XSS.
- **Secure** — o cookie segue somente por HTTPS.
- **SameSite** — reduz o CSRF clássico. Não é absoluto: há exceção, navegador antigo e navegação de nível superior.
- **Domain e Path** — escopo amplo faz o cookie viajar para aplicativos que não deveriam recebê-lo.

Sessão no servidor (identificador opaco) e JWT no cliente são **modelos diferentes** de confiança. Um JWT assinado ainda pode ser um problema de **autorização**: o endpoint verifica se você é a identidade que o token declara?

## Same-origin policy (SOP)

A origem é, de forma aproximada, esquema mais host mais porta. O JavaScript de `https://a.exemplo` não lê o DOM de `https://b.exemplo` por padrão. Grande parte de XSS, CSRF e CORS trata de **quem consegue fazer o navegador enviar credencial para onde**.

CORS é o servidor relaxando a SOP de forma explícita. Entenda a combinação `Access-Control-Allow-Origin: *` com credencial. Não copie essa combinação.

## Sessão e autenticação

Responda por escrito, em um aplicativo que você usa:

1. Onde a identidade fica depois do login?
2. Como o servidor associa o pedido à identidade?
3. Como a sessão termina (logout, expiração, rotação)?
4. O que ocorre se o mesmo cookie ou token for reenviado de outro endereço IP ou de outro user-agent?
5. Na redefinição de senha: o token é de uso único? Ele expira? Ele vaza no cabeçalho Referer?

## TLS

O TLS protege o **trânsito**, não a lógica da aplicação. Certificado inválido, mTLS e HSTS são temas de superfície e de phishing (a pessoa aceita o aviso). Para estudo ofensivo: com TLS bem feito, um intermediário na rede local vê quase nada do HTTP. Com HTTP puro, vê o conteúdo.

## O que não está neste documento

Não há lista de payload, contorno de WAF nem receita de fixação de sessão. Entenda o modelo. Pratique em [laboratórios legais](../pratica/labs-legais.md) (Juice Shop e PortSwigger Academy).

## Leitura seguinte

- [Cliente](client-side.md)
- [APIs e autenticação](apis-e-auth.md)
- [OWASP Top 10](owasp-top-10.md)
