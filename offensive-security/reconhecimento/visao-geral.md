# Reconhecimento: visão geral

Reconhecimento (*recon*) descobre **o que existe e o que merece tempo**, dentro do escopo. Não é varrer o espaço IPv4. É inventário com contexto.

## Por que esta fase existe

Sem reconhecimento, o teste cobre o site que o marketing mostra e ignora o que o atacante real procura: painel de CI, VPN antiga, ambiente `staging.`, e-mail no WHOIS e repositório público com um `.env` que não era exemplo.

No ciclo ofensivo, o reconhecimento alimenta:

- **Modelagem de ameaça** — qual porta um adversário usaria.
- **Priorização** — de 200 hosts, poucos importam.
- **Relatório** — a superfície exposta à internet é um entregável, mesmo sem exploit.

## Camadas típicas

1. **Organização e pessoas** — nome, padrão de e-mail, vaga (stack) e fornecedor. Isto é OSINT. Veja a [coleção OSINT](../../osint-tools-collection/README.md).
2. **Domínio e certificado** — nome, SAN, log de Certificate Transparency e subdomínio.
3. **Endereço e serviço** — o que responde, em qual porta e com qual produto, quando o banner é confiável.
4. **Aplicação** — rota, parâmetro, painel e API versionada.
5. **Identidade** — provedor de identidade, federação, realm de AD exposto por engano e MFA na borda.

Cada camada tem modo **passivo** (somente fonte pública) e modo **ativo** (você envia tráfego ao alvo). O detalhe está em [passivo e ativo](passivo-vs-ativo.md).

## Qualidade e quantidade

Um scanner que gera 40 mil linhas sem dono de ativo não serve ao relatório. Prefira:

- Uma lista curta de **ativos no escopo**, com evidência (captura, cabeçalho, certificado).
- Uma nota de **incerteza** ("parece Cloudflare; a origem é desconhecida").
- A separação de **terceiros** (CDN, e-mail SaaS). Em muitos contratos, o terceiro está fora do escopo legal.

## OSINT no pentest

Dork, GitHub, pastebin, vaga e PDF com metadado são reconhecimento se as regras de engajamento permitirem o uso de informação pública. O [guia de Google Dorks](../../osint-tools-collection/docs/google-search/README.md) serve à exposição autorizada e à pegada da própria organização. Não serve para vasculhar arquivo de pessoa sem relação com o escopo.

## O que estudar

- DNS: A, AAAA, MX, TXT, NS e a ideia de transferência de zona que vaza o mapa.
- Certificado: Certificate Transparency como fonte de nome.
- HTTP: cabeçalho Host, virtual host e redirecionamento.
- Limite de taxa e WAF: reconhecimento agressivo é visível e pode causar negação de serviço acidental.

## Repositórios para aprofundar

- Passivo, subdomínio, httpx e nmap: [coleção OSINT](../../osint-tools-collection/README.md)
- Pipeline e host de laboratório: [AutoRecon](https://github.com/Tib3rius/AutoRecon), [reconftw](https://github.com/six2dez/reconftw)
- Template: [nuclei](https://github.com/projectdiscovery/nuclei)
- TLS: [testssl.sh](https://github.com/drwetter/testssl.sh)
- Wiki: [HackTricks](https://github.com/HackTricks-wiki/hacktricks)

Mapa: [mapa-ferramentas.md](../biblioteca/mapa-ferramentas.md)

## Leitura seguinte

- [Passivo e ativo](passivo-vs-ativo.md)
- [Mapeamento de superfície](mapeamento-de-superficie.md)
- [TCP/IP e serviços](../redes/modelo-tcpip-e-servicos.md)
