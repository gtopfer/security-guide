# Mapeamento de superfície de ataque

Superfície de ataque é o conjunto de **pontos onde um ator externo ou interno pode interagir** com o sistema e, se algo falhar, causar impacto. Mapear é desenhar isso com dono, exposição e criticidade.

## Não é só “portas abertas”

Inclui:

- Apps web e APIs (incluindo versões antigas `/v1` esquecidas)
- VPNs, webmail, Citrix, painéis de nuvem
- Repositórios, pipelines, registry de containers
- Identidade: SSO, usuários de serviço, chaves de API no CI
- Dependências (biblioteca, imagem Docker, GitHub Action)
- Pessoas (helpdesk, processos de reset de senha) — ver [engenharia social](../humano/engenharia-social.md)
- Físico e wireless, se o escopo incluir escritório

## Modelo simples de inventário

Para cada ativo in-scope, anote:

| Campo | Por quê |
|-------|---------|
| Nome / URL / IP | Identidade |
| Dono (time) | Correção depois |
| Exposição | Internet, parceiro, só VPN, só LAN |
| Auth | Anônimo, usuário, admin, m2m |
| Dado | Público, interno, pessoal, segredo |
| Confiança | Produção vs staging vs “alguém subiu na AWS pessoal” |

Isso já é entregável de pentest mediano — muitos clientes não têm essa tabela.

## Priorização (estudo)

Heurística comum, não lei:

1. Internet-facing + autenticação frágil + dado sensível
2. Identidade (IdP, AD, IAM) — compromisso escala
3. CI/CD e supply chain — compromisso vira *todos* os deploys
4. Staging que fala com produção ou replica dados reais
5. Marketing sites isolados (ainda podem ser ponta de phishing da marca)

## Shadow IT

SaaS que um time criou com cartão corporativo, bucket de “teste”, domínio expirado que ainda aponta. Recon de **certificados e DNS** costuma achar isso melhor que o CMDB oficial.

## Superfície *assumida* vs *real*

Diagramas de arquitetura mentem por omissão. O mapa real sai de:

- Tráfego (se o cliente der)
- Inventário de nuvem (se o cliente der leitura IAM)
- Recon combinado com entrevistas (purple / kickoff)

Em red team, às vezes o mapa *é* o objetivo (“chegar no SAP”). Em pentest de conformidade, o mapa *é* o escopo fechado no contrato.

## Leitura seguinte

- [Cloud](../nuvem/cloud-superficie.md)
- [CI/CD](../nuvem/cicd-e-supply-chain.md)
- [Relatório](../defesa/relatorio-e-comunicacao.md)
