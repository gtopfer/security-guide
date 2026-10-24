# Mapeamento de superfície de ataque

A superfície de ataque é o conjunto de **pontos em que um ator externo ou interno pode interagir** com o sistema. Se um controle falha nesse ponto, há impacto. Mapear é registrar o ponto com dono, exposição e criticidade.

## Não é só porta aberta

A superfície inclui:

- Aplicação web e API, inclusive versão antiga esquecida, como `/v1`
- VPN, webmail, Citrix e painel de nuvem
- Repositório, pipeline e registry de contêiner
- Identidade: SSO, usuário de serviço e chave de API no CI
- Dependência: biblioteca, imagem Docker e GitHub Action
- Pessoa: service desk e processo de redefinição de senha. Veja [engenharia social](../humano/engenharia-social.md)
- Acesso físico e rede sem fio, se o escopo incluir o escritório

## Modelo simples de inventário

Para cada ativo no escopo, anote:

| Campo | Por quê |
|-------|---------|
| Nome, URL ou IP | Identidade do ativo |
| Dono (time) | Quem corrige depois |
| Exposição | Internet, parceiro, somente VPN ou somente LAN |
| Autenticação | Anônimo, usuário, administrador ou máquina a máquina |
| Dado | Público, interno, pessoal ou segredo |
| Confiança | Produção, homologação ou ambiente criado em conta pessoal |

Esta tabela já é entregável de um pentest. Muitos clientes não a possuem.

## Priorização (estudo)

Heurística comum, não uma regra fixa:

1. Exposto à internet, com autenticação frágil e com dado sensível.
2. Identidade (provedor de identidade, AD, IAM). O comprometimento se espalha.
3. CI/CD e supply chain. O comprometimento alcança os deploys seguintes.
4. Homologação que fala com produção ou que replica dado real.
5. Site de marketing isolado. Ainda pode servir de página de phishing da marca.

## Shadow IT

SaaS criado por um time com cartão corporativo, bucket de teste e domínio expirado que ainda resolve. Reconhecimento de **certificado e de DNS** encontra esse ativo com mais frequência do que o CMDB oficial.

## Superfície assumida e superfície real

O diagrama de arquitetura omite componentes. O mapa real sai de:

- Tráfego, se o cliente entregar a captura.
- Inventário de nuvem, se o cliente entregar leitura de IAM.
- Reconhecimento combinado com entrevista (purple team ou reunião de início).

Em red team, o mapa às vezes é o objetivo, por exemplo chegar ao SAP. Em pentest de conformidade, o mapa é o escopo fechado no contrato.

## Leitura seguinte

- [Nuvem](../nuvem/cloud-superficie.md)
- [CI/CD](../nuvem/cicd-e-supply-chain.md)
- [Relatório](../defesa/relatorio-e-comunicacao.md)
