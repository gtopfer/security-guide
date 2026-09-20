# Reconhecimento: visão geral

Reconhecimento (*recon*) é descobrir **o que existe e o que merece tempo**, dentro do escopo. Não é “escanear o IPv4”. É inventário + contexto.

## Por que existe

Sem recon você testa o que o marketing mostrou (o site bonito) e ignora o que o atacante real ama: painel de CI, VPN antiga, ambiente `staging.`, e-mail no WHOIS, repositório público com `.env` de exemplo que não era exemplo.

No ciclo ofensivo, recon alimenta:

- **Threat modeling** — o que um adversário usaria como porta.
- **Priorização** — 200 hosts; 8 importam.
- **Relatório** — “superfície internet-facing” é um entregável, mesmo sem “exploit”.

## Camadas típicas

1. **Org e pessoas** — nomes, e-mails de padrão, vagas (stack), fornecedores. OSINT; veja a [coleção OSINT](../../osint-tools-collection/README.md).
2. **Domínios e certificados** — nomes, SANs, CT logs, subdomínios.
3. **Endereços e serviços** — o que responde, em quais portas, com quais produtos (quando o banner não mente).
4. **Aplicações** — rotas, parâmetros, painéis, APIs versionadas.
5. **Identidade** — IdP, federação, Realm AD exposto por engano, MFA na borda.

Cada camada tem modo **passivo** (só fontes públicas) e **ativo** (você toca o alvo). Detalhe em [passivo vs ativo](passivo-vs-ativo.md).

## Qualidade vs quantidade

Scanner que gera 40 mil linhas sem dono de ativo é lixo. Prefira:

- Lista curta de **ativos in-scope** com evidência (print, header, cert).
- Nota de **incerteza** (“parece Cloudflare; origem desconhecida”).
- Separar **terceiros** (CDN, e-mail SaaS) — muitas vezes *fora* do escopo legal.

## OSINT no pentest

Dorks, GitHub, pastebins, vagas, PDF com metadados: tudo isso é recon se o ROE permitir uso de informação pública. O [guia de Google Dorks](../../osint-tools-collection/docs/google-search/README.md) do repo serve para exposição *autorizada* / pegada da própria org, não para vasculhar Drive de pessoa aleatória.

## O que estudar (conceitos)

- DNS: A, AAAA, MX, TXT, NS, zona mal transferível (ideia: vazamento de mapa).
- Certificados: CT como fonte de nomes.
- HTTP: host headers, vhosts, redirecionamentos.
- Rate limiting e WAF: recon agressivo *é visível* e pode ser DoS acidental.

## Leitura seguinte

- [Passivo vs ativo](passivo-vs-ativo.md)
- [Mapeamento de superfície](mapeamento-de-superficie.md)
- [TCP/IP e serviços](../redes/modelo-tcpip-e-servicos.md)
