# Glossário (ofensiva e defesa)

Definições curtas para leitura dos outros documentos. Não são normas.

**ACL** — lista de quem pode o quê em objeto (arquivo, bucket, objeto AD).

**AD / Active Directory** — serviço de identidade Windows em empresas.

**ATT&CK** — catálogo de táticas e técnicas adversárias (MITRE).

**Authn / Authz** — autenticação (quem é) vs autorização (o que pode).

**Banner** — texto que um serviço mostra ao conectar; indício, não prova.

**BOLA / IDOR** — acesso a objeto de outro usuário mudando o identificador.

**Bug bounty** — recompensa por achados dentro de regras publicadas.

**C2** — *command and control*; canal de comando de malware. Estude pelo lado IR, não monte o seu.

**CAPEC** — padrões de ataque (MITRE).

**CI/CD** — integração e entrega contínuas; pipeline.

**CWE** — classe de fraqueza em software.

**CVE** — identificador de vulnerabilidade pública.

**CVSS** — score de gravidade; precisa de contexto.

**Credential stuffing** — reuso de senha vazada em outro serviço.

**CSP** — Content-Security-Policy; mitiga parte de XSS.

**CSRF** — pedido forçado no browser da vítima autenticada.

**CT logs** — registros públicos de certificados.

**DC** — domain controller.

**Disclosure** — como se avisa uma falha.

**DMZ** — segmento de rede mais exposto.

**DoS** — tornar serviço indisponível; em geral fora de escopo.

**EDR** — agente de detecção em endpoint.

**Escopo / ROE** — o que pode testar e como.

**Exploit** — código/condição que usa uma falha. Este repo não publica PoCs.

**Flag (CTF)** — prova de desafio; ≠ pentest.

**GPO** — Group Policy Object no AD.

**Hash** — função de resumo; senhas devem usar KDF lento, não “MD5 de estudo”.

**IAM** — gestão de identidade e acesso (sobretudo nuvem).

**IMDS** — serviço de metadados da instância em cloud.

**IOC** — indicador de compromisso (hash, IP, domínio).

**Kerberos** — protocolo de tickets em AD.

**Kill chain** — modelo linear de intrusão.

**Lateral movement** — de um host/conta para outro.

**Least privilege** — só a permissão necessária.

**MFA / 2FA** — segundo fator.

**Misconfig** — sistema certo, ajuste errado (default, exposição).

**MITM** — intermediário no tráfego.

**NTLM** — autenticação Windows legado.

**OSINT** — inteligência de fontes abertas.

**OWASP** — comunidade de AppSec.

**Payload** — dado que dispara comportamento. Não listamos aqui.

**Pentest** — teste de invasão contratado, com relatório.

**Phishing** — engenharia social por mensagem.

**Priv-esc** — aumentar privilégio.

**Purple team** — ataque e defesa juntos.

**RCE** — execução remota de código (classe de impacto).

**Red team** — exercício de objetivo, mais stealth.

**Recon** — reconhecimento de superfície.

**Root / SYSTEM** — máximo privilégio local típico.

**SIEM** — correlação de logs.

**SOP** — same-origin policy no browser.

**SSRF** — servidor busca URL controlável; risco a rede interna/IMDS.

**SSO / IdP** — um login para vários apps.

**Supply chain** — comprometer dependência ou build.

**TGT / TGS** — tickets Kerberos.

**Threat model** — quem ataca, o que quer, o que quebra.

**WAF** — filtro na frente de HTTP; controle, não milagre.

**WSTG** — guia de teste web OWASP.

**XSS** — script no contexto da origem da app.

**0-day** — falha sem patch público conhecido. Pesquisa tem disclosure; uso contra terceiro é outra conversa legal.
