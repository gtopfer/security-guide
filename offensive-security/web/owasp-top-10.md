# OWASP Top 10 — classes de risco para estudar

O Top 10 é um **índice pedagógico e de comunicação**, não um padrão de teste completo. Versões mudam; as *classes* permanecem úteis. Consulte sempre a lista vigente: <https://owasp.org/www-project-top-ten/>

Abaixo: o que cada classe *significa* e o que estudar. Sem exemplos de exploit.

## Broken access control

O servidor não confirma se *este* usuário pode *este* objeto/ação. Inclui IDOR/BOLA, vertical (user→admin), bypass de path, CORS permissivo que vaza.

**Estude:** autorização no *backend* por recurso; testes com duas contas de lab; princípio de fail-closed.

## Cryptographic failures

Dado sensível em trânsito ou em repouso sem proteção adequada; hash de senha fraco; secrets no repositório.

**Estude:** TLS, at-rest, KMS, Argon2/bcrypt *como ideia*, o que não vai para log.

## Injection (visão ampla)

A aplicação mistura **dado** com **comando** (SQL, LDAP, OS, template). A defesa conceitual é parametrizar / API segura / não concatenar.

**Estude:** a fronteira dado vs código; por que “escapar aspas” falha como estratégia única. Pratique só em apps vulneráveis oficiais.

## Insecure design

Não é bug de implementação: o *fluxo* é perigoso (reset de senha previsível, falta de rate limit no OTP, tenant sem isolamento).

**Estude:** threat modeling, ASVS, “abuse cases”.

## Security misconfiguration

Default, diretório listado, painel na internet, headers ausentes, cloud ACL pública, debug ligado.

**Estude:** hardening checklists, CIS, inventário; recon de superfície.

## Vulnerable and outdated components

Biblioteca, WordPress plugin, JDK, container base. Ofensiva aqui é *gestão de SBOM* tanto quanto CVE.

**Estude:** OSV, NVD, processo de patch; não colecionar exploits.

## Identification and authentication failures

Senha, sessão, MFA bypass *de lógica* (não “furar SMS da vítima”). Credential stuffing como *classe* (reuso de senha).

**Estude:** [credenciais](../identidade/autenticacao-e-credenciais.md), NIST SP 800-63b em espírito.

## Software and data integrity failures

Update sem assinatura, CI que publica qualquer tag, desserialização insegura (objeto vira código).

**Estude:** [supply chain](../nuvem/cicd-e-supply-chain.md), assinatura de artefato.

## Security logging and monitoring failures

Ataque aconteceu e ninguém viu. Para ofensiva ética, isso vira recomendação; para purple, vira exercício.

**Estude:** [detecção](../defesa/deteccao-e-logs.md).

## Server-Side Request Forgery (SSRF) — frequentemente em destaque

O servidor busca URL que o usuário influencia e alcança rede interna / metadados de nuvem.

**Estude:** allowlist, bloqueio de ranges link-local, IMDS na cloud. Sem laboratório de bypass neste repo.

## Como usar o Top 10 nos estudos

Para cada item, escreva:

1. Premissa que quebrou (controle que deveria existir).
2. Impacto de negócio em um sistema que você conheça (banco, saúde, SaaS).
3. Controle preventivo e um detetive (log).

Depois aprofunde no [WSTG](https://owasp.org/www-project-web-security-testing-guide/) e no [ASVS](https://owasp.org/www-project-application-security-verification-standard/) — leia objetivos de teste; execute só em lab autorizado.

## Git para aprofundar

Fonte das listas: [coleção de pentest](../../pentest-tools-collection/README.md). Recorte web:

| Classe (estudo) | Repos |
|-----------------|--------|
| Proxy / HTTP | [ZAP](https://github.com/zaproxy/zaproxy), [mitmproxy](https://github.com/mitmproxy/mitmproxy) |
| Access control | duas sessões no ZAP; lab Juice Shop / crAPI; [OFFAT](https://github.com/OWASP/OFFAT) |
| Crypto / TLS | [testssl.sh](https://github.com/drwetter/testssl.sh), [sslyze](https://github.com/nabla-c0d3/sslyze) |
| Injection | [sqlmap](https://github.com/sqlmapproject/sqlmap), [commix](https://github.com/commixproject/commix), [SSTImap](https://github.com/vladko312/SSTImap) **só em DVWA/WebGoat** |
| XSS | [dalfox](https://github.com/hahwul/dalfox); PortSwigger Academy |
| Misconfig / CVE conhecida | [nuclei](https://github.com/projectdiscovery/nuclei) + templates; [nikto](https://github.com/sullo/nikto) |
| Componentes | [Trivy](https://github.com/aquasecurity/trivy), [osv-scanner](https://github.com/google/osv-scanner) |
| Secrets | Gitleaks / TruffleHog (coleção OSINT) |
| Cheatsheets | [WSTG](https://github.com/OWASP/wstg), [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries), [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings), [HackTricks](https://github.com/HackTricks-wiki/hacktricks) |

Mapa completo: [mapa-ferramentas.md](../biblioteca/mapa-ferramentas.md).

## Leitura seguinte

- [APIs](apis-e-auth.md)
- [Labs](../pratica/labs-legais.md)
