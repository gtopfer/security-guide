# Glossário (ofensiva e defesa)

Definição curta para a leitura dos outros documentos. Estas linhas não são norma.

**ACL** — lista de quem pode o quê em um objeto (arquivo, bucket, objeto do AD).

**AD / Active Directory** — serviço de identidade Windows em empresas.

**ATT&CK** — catálogo de tática e de técnica de adversário (MITRE).

**Authn / Authz** — autenticação (quem é) e autorização (o que pode).

**Banner** — texto que um serviço mostra ao conectar. É indício, não prova.

**BOLA / IDOR** — acesso ao objeto de outro usuário pela troca do identificador.

**Bug bounty** — recompensa por achado dentro de regra publicada.

**C2** — *command and control*; canal de comando de malware. Estude pelo lado da resposta a incidente. Não monte o seu contra terceiro.

**CAPEC** — padrão de ataque (MITRE).

**CI/CD** — integração e entrega contínuas; o pipeline.

**CWE** — classe de fraqueza em software.

**CVE** — identificador de vulnerabilidade pública.

**CVSS** — pontuação de gravidade. Exige contexto.

**Credential stuffing** — reuso de senha vazada em outro serviço.

**CSP** — Content-Security-Policy. Reduz parte do impacto de XSS.

**CSRF** — pedido forçado no navegador da vítima autenticada.

**CT logs** — registro público de certificado.

**DC** — controlador de domínio.

**Disclosure** — forma de avisar uma falha.

**DMZ** — segmento de rede mais exposto.

**DoS** — tornar o serviço indisponível. Em geral, fica fora do escopo.

**EDR** — agente de detecção no endpoint.

**Escopo / ROE** — o que você pode testar e de que forma. ROE são as regras de engajamento.

**Exploit** — código ou condição que usa uma falha. Este repositório não publica prova de conceito.

**Flag (CTF)** — prova de um desafio. Não é pentest.

**GPO** — Group Policy Object no AD.

**Hash** — função de resumo. Senha deve usar uma função lenta de derivação de chave, não um MD5 de exercício.

**IAM** — gestão de identidade e de acesso, sobretudo em nuvem.

**IMDS** — serviço de metadado da instância em nuvem.

**IOC** — indicador de comprometimento (hash, IP, domínio).

**Kerberos** — protocolo de ticket no AD.

**Kill chain** — modelo linear de intrusão.

**Lateral movement** — passagem de um host ou de uma conta para outro.

**Least privilege** — somente a permissão necessária.

**MFA / 2FA** — segundo fator.

**Misconfig** — o sistema é o previsto, mas o ajuste está errado (padrão ou exposição).

**MITM** — intermediário no tráfego.

**NTLM** — autenticação Windows legada.

**OSINT** — inteligência de fonte aberta.

**OWASP** — comunidade de segurança de aplicação.

**Payload** — dado que dispara um comportamento. Este glossário não lista payload.

**Pentest** — teste de invasão contratado, com relatório.

**Phishing** — engenharia social por mensagem.

**Priv-esc** — aumento de privilégio.

**Purple team** — ataque e defesa no mesmo exercício.

**RCE** — execução remota de código (classe de impacto).

**Red team** — exercício de objetivo, com mais discrição.

**Recon** — reconhecimento de superfície.

**Root / SYSTEM** — privilégio local máximo típico.

**SIEM** — correlação de log.

**SOP** — same-origin policy no navegador.

**SSRF** — o servidor busca uma URL controlável. O risco alcança rede interna e IMDS.

**SSO / IdP** — um login para vários aplicativos. IdP é o provedor de identidade.

**Supply chain** — comprometimento de dependência ou de build.

**TGT / TGS** — tickets Kerberos.

**Threat model** — quem ataca, o que quer e o que quebra.

**WAF** — filtro na frente do HTTP. É um controle. Não cobre toda falha de aplicação.

**WSTG** — guia de teste web da OWASP.

**XSS** — script no contexto da origem da aplicação.

**0-day** — falha sem correção pública conhecida. A pesquisa tem disclosure. O uso contra terceiro é uma questão legal distinta.
