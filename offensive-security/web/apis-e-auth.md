# APIs e autorização

API é aplicação sem HTML. Os defeitos mais caros da última década em SaaS foram **autorização** (objeto de outro inquilino) e **excesso de dado** no JSON, não XSS.

## Estilos

- **REST** — recurso, verbo HTTP e código. A autenticação costuma ser Bearer.
- **GraphQL** — um endpoint e consulta flexível. O risco é enumerar o schema e pedir campo demais (introspecção em produção).
- **RPC e gRPC** — contrato. A autorização ainda precisa existir por operação.
- **Webhook** — o servidor chama você. Autenticar a origem (assinatura HMAC) é o tema ofensivo e defensivo.

OWASP API Security: <https://api-security.owasp.org/>

## Autenticação e autorização

- **Autenticação:** quem é (token válido).
- **Autorização:** o que pode (este `GET /faturas/881` é desta pessoa?).

BOLA (*Broken Object Level Authorization*) e IDOR: o token é válido, e o **identificador do objeto** não é conferido com o dono. Estudar isso vale mais do que memorizar dezenas de CVE de framework.

BFLA (*Broken Function Level Authorization*): o usuário chama operação de administrador porque a rota existe e o gateway só verificou se havia login.

## Tokens

Estude, em conceito:

- **Bearer opaco** — a sessão fica no servidor. A revogação é direta.
- **JWT** — auto-contido. A revogação é difícil. O algoritmo `none` e a confusão de chave são classes históricas. Entenda o modelo de confiança: quem assina e quem guarda a chave.
- **OAuth 2 e OIDC** — papéis: resource owner, client, authorization server e resource server. Authorization code com PKCE, e o fluxo implicit como legado. Escopo não é a autorização fina da API de negócio.
- **mTLS e chave de API** — identidade de máquina. Chave no frontend é pública.

## Atribuição em massa e excesso de campo

O cliente envia JSON com `"role":"admin"` e o backend aceita. Ou a API devolve campo interno (`is_admin`, hash). O contrato OpenAPI mostra o que deveria existir. Compare com o que o laboratório devolve de fato.

## Limite de taxa, paginação e exportação

A falta de limite vira enumeração de identificador, stuffing e custo (negação de serviço financeira). A exportação "CSV de tudo" é superfície de exfiltração interna.

## Como estudar

1. Leia um OpenAPI público de um produto. Muitos fornecedores publicam o contrato.
2. Marque a operação que aceita **identificador** e pergunte onde o servidor liga o identificador a quem chama.
3. No Juice Shop ou em API de laboratório, use **duas contas** e troque somente o identificador. A ideia do teste fica no ambiente autorizado.
4. Em GraphQL, leia sobre limite de profundidade e lista de consultas permitidas em produção.

## Leitura seguinte

- [HTTP e sessão](modelo-http-e-sessao.md)
- [Credenciais](../identidade/autenticacao-e-credenciais.md)
