# HTTP, cookies e sessão

Quase toda AppSec ofensiva começa em **como o protocolo trata estado e identidade**. Sem isso, “vulnerabilidade web” vira palavra mágica.

## Request / response

HTTP é mensagem: método, path, headers, corpo. O servidor decide; o cliente (browser ou `curl`) só propõe. Qualquer controle *só no JavaScript* é dica, não segurança.

Conceitos para estudar até ficar entediado:

- Métodos: GET idempotente na teoria; POST/PUT/PATCH/DELETE mudam estado.
- Códigos: 2xx sucesso, 3xx redirect (open redirect vive aqui), 4xx cliente, 5xx servidor.
- Headers de segurança: `Content-Security-Policy`, `Set-Cookie` (atributos), `Authorization`, CORS (`Access-Control-*`).
- HTTP/2 e HTTP/3 mudam transporte; a semântica de app continua sendo recurso + authz.

Material: RFC 9110 (HTTP Semantics) — pesado, mas é a fonte. MDN é mais digerível: <https://developer.mozilla.org/en-US/docs/Web/HTTP>

## Cookies e atributos

Cookie é armazenamento que o browser **anexa** depois, segundo regras de domínio/path.

Estude o significado de:

- **HttpOnly** — JS não lê (mitiga *roubo* via XSS, não a existência do XSS).
- **Secure** — só HTTPS.
- **SameSite** — reduz CSRF clássico; não é absoluto (exceções, browsers velhos, top-level).
- **Domain / Path** — escopo demais = cookie viaja para apps que não deveriam.

Sessão no servidor (ID opaco) vs JWT no cliente são **modelos diferentes** de confiança. Um JWT “assinado” ainda pode ser um problema de **authz** (você é quem o token diz? o *endpoint* checa?).

## Same-origin policy (SOP)

Origem ≈ esquema + host + porta. JS de `https://a.exemplo` não lê o DOM de `https://b.exemplo` à toa. Muita da “magia” de XSS/CSRF/CORS é sobre **quem consegue fazer o browser enviar credenciais para onde**.

CORS é o servidor *relaxando* SOP de forma explícita. `Access-Control-Allow-Origin: *` com credenciais é combinação que você deve *entender*, não copiar.

## Sessão e autenticação

Perguntas de estudo (responda por escrito num app que você use):

1. Onde vive a identidade após o login?
2. Como o servidor associa pedido à identidade?
3. Como encerra (logout, expiração, rotação)?
4. O que acontece se eu reenviar o mesmo cookie/token de outro IP/UA?
5. Reset de senha: o token é de uso único? Expira? Vaza no Referer?

## TLS

TLS protege o **trânsito**, não a lógica da app. Certificado inválido, mTLS, HSTS são temas de superfície e de phishing (usuário clicando em aviso). Para ofensiva de estudo: o que um MITM *na rede local* ainda vê se houver TLS bem feito (quase nada do HTTP) vs se houver HTTP puro.

## O que não está neste documento

Nada de lista de payloads, bypass de WAF ou receitas de session fixation. Entenda o modelo; pratique em [labs legais](../pratica/labs-legais.md) (Juice Shop, PortSwigger Academy).

## Leitura seguinte

- [Client-side](client-side.md)
- [APIs e auth](apis-e-auth.md)
- [OWASP Top 10](owasp-top-10.md)
