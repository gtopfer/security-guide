# APIs e autorização

API é aplicação sem HTML. Os bugs mais caros da última década em SaaS foram **autorização** (objeto de outro tenant) e **excesso de dado** no JSON, não XSS bonito.

## Estilos

- **REST** — recursos, verbos HTTP, códigos. Auth frequentemente Bearer.
- **GraphQL** — um endpoint, consultas flexíveis; risco de enumerar o *schema* e pedir campos demais (introspection em produção).
- **RPC / gRPC** — contratos; authz ainda precisa existir *por RPC*.
- **Webhooks** — o servidor *chama* você; autenticar a origem (assinatura HMAC) é o tema ofensivo/defensivo.

OWASP API Security: <https://owasp.org/www-project-api-security/>

## Autenticação vs autorização

- **Authentication:** quem é (token válido).
- **Authorization:** o que pode (este `GET /faturas/881` é *dele*?).

BOLA (*Broken Object Level Authorization*) / IDOR: o token é válido, o **ID do objeto** não é checado contra o dono. Estudar isso vale mais que memorizar 50 CVEs de framework.

BFLA (*Broken Function Level*): usuário chama operação de admin porque a rota existe e o gateway só olhou “está logado”.

## Tokens

Estude, em conceito:

- **Bearer opaco** — sessão no servidor; revogação fácil.
- **JWT** — auto-contido; revogação difícil; algoritmo `none` e chave confusa são *classes* históricas — entenda o modelo de confiança (quem assina, quem guarda a chave).
- **OAuth2 / OIDC** — papéis: resource owner, client, authorization server, resource server. Authorization code + PKCE vs implicit (legado). Escopos ≠ authz fina da API de negócio.
- **mTLS e API keys** — identidade de *máquina*; keys no frontend = públicas.

## Mass assignment e oversharing

O cliente manda JSON com `"role":"admin"` e o backend aceita. Ou a API devolve campos internos (`is_admin`, hash). Contratos OpenAPI ajudam a ver o que *deveria* existir; compare com o que o lab realmente devolve.

## Rate limit, paginação, export

Falta de limite vira enumeração de IDs, stuffing, custo (DoS financeiro). Export “CSV de tudo” é superfície de exfiltração interna.

## Como estudar

1. Leia um OpenAPI público de um produto (muitos vendors publicam).
2. Marque operações que aceitam **ID** e pergunte: “onde o servidor liga ID ↔ caller?”
3. No Juice Shop / APIs de lab, use **duas contas** e troque só o identificador — ideia do teste, ambiente autorizado.
4. GraphQL: leia sobre depth limiting e allowlist de queries em produção.

## Leitura seguinte

- [HTTP e sessão](modelo-http-e-sessao.md)
- [Credenciais](../identidade/autenticacao-e-credenciais.md)
