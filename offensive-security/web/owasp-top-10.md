# OWASP Top 10: classes de risco para estudar

O Top 10 é um **índice de estudo e de comunicação**. Não é um padrão de teste completo. As versões mudam. As classes continuam úteis. Consulte sempre a lista vigente: <https://owasp.org/www-project-top-ten/>

Abaixo, o que cada classe significa e o que estudar. Sem exemplo de exploit.

## Broken access control

O servidor não confirma se este usuário pode este objeto ou esta ação. Inclui IDOR e BOLA, elevação de usuário para administrador, contorno de caminho e CORS permissivo que vaza dado.

**Estude:** autorização no backend, por recurso; teste com duas contas de laboratório; falha fechada (negar quando a regra não decide).

## Cryptographic failures

Dado sensível em trânsito ou em repouso sem proteção adequada, hash de senha fraco e segredo no repositório.

**Estude:** TLS, criptografia em repouso, KMS, Argon2 ou bcrypt como ideia, e o que não deve ir para o log.

## Injection

A aplicação mistura **dado** com **comando** (SQL, LDAP, sistema operacional, template). A defesa conceitual é parametrizar, usar API segura e não concatenar.

**Estude:** a fronteira entre dado e código, e por que "escapar aspas" falha como estratégia única. Pratique somente em aplicativo vulnerável oficial.

## Insecure design

Não é defeito de implementação. O fluxo é perigoso: redefinição de senha previsível, falta de limite de taxa no OTP, inquilino sem isolamento.

**Estude:** modelagem de ameaça, ASVS e caso de abuso.

## Security misconfiguration

Padrão de fábrica, listagem de diretório, painel na internet, cabeçalho ausente, ACL pública na nuvem e modo de depuração ligado.

**Estude:** lista de hardening, CIS, inventário e reconhecimento de superfície.

## Vulnerable and outdated components

Biblioteca, plugin, JDK e imagem base de contêiner. Aqui a ofensiva é gestão de SBOM tanto quanto CVE.

**Estude:** OSV, NVD e processo de correção. Não acumule exploit.

## Identification and authentication failures

Senha, sessão e contorno de MFA por lógica da aplicação, não por interceptação do SMS da vítima. Credential stuffing é a classe do reuso de senha.

**Estude:** [credenciais](../identidade/autenticacao-e-credenciais.md) e o espírito do NIST SP 800-63B.

## Software and data integrity failures

Atualização sem assinatura, CI que publica qualquer tag e desserialização insegura (o objeto vira código).

**Estude:** [supply chain](../nuvem/cicd-e-supply-chain.md) e assinatura de artefato.

## Security logging and monitoring failures

O ataque ocorreu e ninguém viu. Para a ofensiva ética, isso vira recomendação. Para o purple team, vira exercício.

**Estude:** [detecção](../defesa/deteccao-e-logs.md).

## Server-Side Request Forgery (SSRF)

O servidor busca uma URL que o usuário influencia e alcança a rede interna ou o metadado de nuvem.

**Estude:** lista de permissão, bloqueio de faixa link-local e IMDS na nuvem. Este repositório não traz laboratório de contorno.

## Como usar o Top 10 no estudo

Para cada item, escreva:

1. A premissa que quebrou (o controle que deveria existir).
2. O impacto de negócio em um sistema que você conhece (banco, saúde, SaaS).
3. Um controle preventivo e um controle detectivo (log).

Depois, aprofunde no [WSTG](https://owasp.org/www-project-web-security-testing-guide/) e no [ASVS](https://owasp.org/www-project-application-security-verification-standard/). Leia o objetivo do teste. Execute somente em laboratório autorizado.

## Repositórios para aprofundar

A fonte das listas está na [coleção de pentest](../../pentest-tools-collection/README.md). Recorte web:

| Classe (estudo) | Repositórios |
|-----------------|--------|
| Proxy e HTTP | [ZAP](https://github.com/zaproxy/zaproxy), [mitmproxy](https://github.com/mitmproxy/mitmproxy) |
| Controle de acesso | duas sessões no ZAP; laboratório Juice Shop ou crAPI; [OFFAT](https://github.com/OWASP/OFFAT) |
| Criptografia e TLS | [testssl.sh](https://github.com/drwetter/testssl.sh), [sslyze](https://github.com/nabla-c0d3/sslyze) |
| Injeção | [sqlmap](https://github.com/sqlmapproject/sqlmap), [commix](https://github.com/commixproject/commix), [SSTImap](https://github.com/vladko312/SSTImap), somente em DVWA ou WebGoat |
| XSS | [dalfox](https://github.com/hahwul/dalfox); PortSwigger Academy |
| Configuração incorreta e CVE conhecida | [nuclei](https://github.com/projectdiscovery/nuclei) e templates; [nikto](https://github.com/sullo/nikto) |
| Componentes | [Trivy](https://github.com/aquasecurity/trivy), [osv-scanner](https://github.com/google/osv-scanner) |
| Segredos | Gitleaks e TruffleHog (coleção OSINT) |
| Folhas de referência | [WSTG](https://github.com/OWASP/wstg), [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries), [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings), [HackTricks](https://github.com/HackTricks-wiki/hacktricks) |

Mapa completo: [mapa-ferramentas.md](../biblioteca/mapa-ferramentas.md).

## Leitura seguinte

- [APIs](apis-e-auth.md)
- [Laboratórios](../pratica/labs-legais.md)
