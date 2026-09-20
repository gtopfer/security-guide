# Labs legais (onde praticar)

Só treine onde a autorização está no ToS ou no contrato. Abaixo são **pontos de partida**, não ranking.

## Na sua máquina

| Lab | Notas |
|-----|--------|
| [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) | Web moderna; Docker. Já na coleção de pentest |
| [Mutillidae II](https://github.com/webpwnized/mutillidae) | Clássico OWASP |
| [DVWA](https://github.com/digininja/DVWA) | Didático; isole em VM/container |
| [WebGoat](https://github.com/WebGoat/WebGoat) | OWASP, lições guiadas |
| [crAPI](https://github.com/OWASP/crAPI) | API Security |
| [Juice Shop + seu proxy HTTP](https://owasp.org/www-community/Zed_Attack_Proxy) | ZAP é FOSS para *inspecionar* HTTP no lab |

Subir lab ≠ atacar a LAN: use rede isolada / Docker bridge.

## Plataformas (conta + regras)

- **PortSwigger Academy** — <https://portswigger.net/web-security> — labs web gratuitos, excelente didática.
- **TryHackMe** / **Hack The Box** — máquinas e rooms; tráfego só na VPN deles.
- **PentesterLab** — trilhas web pagas/gratuitas parciais.
- **OverTheWire** — <https://overthewire.org/> — jogos de Linux, não é pentest corporativo mas ensina Unix.
- **AWS/Azure/GCP Free tier** — **sua** conta, alarme de billing, apague recurso. Não use organização do trabalho.

## Datasets e defesa

- Logs públicos de treino (ex.: conjuntos de DFIR educacionais) — use para SOC, não para atacar origens reais.
- Sigma + um SIEM de lab (Wazuh FOSS, etc.).

## Bug bounty

Só depois de labs. Leia o *scope* duas vezes. Sem DoS, sem dados de usuário real, sem “out of scope mas achei grave então fui”.

## O que este repo não aponta

Lista de hosts vulneráveis na internet, dumps de exame, “auto-pwn”.

## Leitura seguinte

- [Coleção pentest](../../pentest-tools-collection/README.md)
- [Ética](../fundamentos/etica-e-lei.md)
