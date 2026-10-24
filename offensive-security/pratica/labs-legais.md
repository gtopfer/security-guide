# Laboratórios legais (onde praticar)

Treine somente onde a autorização está no termo de uso ou no contrato. A lista abaixo é um **ponto de partida**, não um ranking.

## Na sua máquina

| Laboratório | Notas |
|-----|--------|
| [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) | Aplicação web moderna. Docker. Também está na coleção de pentest |
| [Mutillidae II](https://github.com/webpwnized/mutillidae) | Laboratório clássico da OWASP |
| [DVWA](https://github.com/digininja/DVWA) | Didático. Isole em máquina virtual ou em contêiner |
| [WebGoat](https://github.com/WebGoat/WebGoat) | OWASP, com lição guiada |
| [crAPI](https://github.com/OWASP/crAPI) | Segurança de API |
| [Juice Shop e o seu proxy HTTP](https://www.zaproxy.org/) | O ZAP é software livre para inspecionar HTTP no laboratório |

Subir o laboratório não autoriza atacar a LAN. Use rede isolada ou a bridge do Docker.

Lista maior (GOAD, Vulhub, CloudGoat, Kubernetes Goat, mobile, GraphQL): [Laboratórios na coleção de pentest](../../pentest-tools-collection/README.md#labs-e-ambientes-vulneráveis).

## Plataformas (conta e regras)

- **PortSwigger Academy** — <https://portswigger.net/web-security> — laboratório web gratuito, com explicação clara.
- **TryHackMe** e **Hack The Box** — máquina e sala. O tráfego fica na VPN da plataforma.
- **PentesterLab** — trilha web, parte gratuita e parte paga.
- **OverTheWire** — <https://overthewire.org/> — jogo de Linux. Não é pentest corporativo. Ensina Unix.
- **Nível gratuito de AWS, Azure ou GCP** — use a **sua** conta, ative alarme de cobrança e apague o recurso. Não use a organização do trabalho.

## Conjunto de dados e defesa

- Log público de treino (conjunto educacional de DFIR): use para SOC. Não use para atacar a origem real.
- Sigma e um SIEM de laboratório (Wazuh, por exemplo).

## Bug bounty

Comece somente depois dos laboratórios. Leia o escopo duas vezes. Sem negação de serviço, sem dado de usuário real e sem a justificativa "está fora do escopo, mas achei grave, então continuei".

## O que este repositório não indica

Lista de host vulnerável na internet, dump de exame e ferramenta de comprometimento automático.

## Leitura seguinte

- [Coleção de pentest](../../pentest-tools-collection/README.md)
- [Ética](../fundamentos/etica-e-lei.md)
