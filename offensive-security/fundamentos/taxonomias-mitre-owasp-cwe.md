# Taxonomias: ATT&CK, OWASP, CWE, CVSS, CAPEC

Sem um vocabulário comum, cada um chama a mesma falha de um nome. Taxonomias não substituem entendimento — evitam relatório de 40 páginas que não dá para priorizar.

## MITRE ATT&CK

- **O quê:** base de conhecimento de *táticas* (objetivo: persistência, movimento lateral…) e *técnicas* (como, em alto nível).
- **Para ofensiva de estudo:** ver o que existe no mundo real; montar *coverage* com o blue team.
- **Para não fazer:** tratar ATT&CK como lista de missões para executar na internet.

Comece pelas matrizes **Enterprise** (Windows, Linux, nuvem) e leia a página da técnica: detecções, mitigações, exemplos. Site: <https://attack.mitre.org/>

**ATT&CK ≠ CVE.** CVE é falha em produto. Técnica é comportamento (muitas vezes sem CVE nenhum — conta válida, GPO fraca).

## CAPEC

*Common Attack Pattern Enumeration and Classification*: padrões de ataque mais “história” que ATT&CK (ex.: “forçar um caminho de diretório”). Útil para desenhar testes e ameaças em AppSec. <https://capec.mitre.org/>

## CWE

*Common Weakness Enumeration*: fraqueza no *software* (validação, authz, crypto). Relatórios de bug bounty e SAST falam CWE. <https://cwe.mitre.org/>

Relação típica: **CWE** (a classe no código) → **CVE** (instância numa versão) → às vezes um **padrão CAPEC** / técnica ATT&CK quando explorada.

## CVE e NVD

- **CVE:** identificador público de uma vulnerabilidade divulgada.
- **NVD / CVSS:** tentativa de pontuar gravidade. CVSS alto não significa explorável *no seu* contexto (sem rede, com MFA, com WAF).

No relatório: cite CVE se houver, mas **contextualize** (precondições, autenticado ou não, dado alcançável).

## OWASP

- **Top 10:** lista periódica das classes mais vistas em apps web — ótimo índice de estudo, péssimo como “só isso existe”.
- **ASVS:** requisitos verificáveis (níveis 1–3) para *construir* e auditar.
- **WSTG:** *Web Security Testing Guide* — o que *testar* em cada área (ainda assim: execute só em alvo autorizado; este repo não copia os procedimentos).
- **MASVS / MASTG:** mobile.
- **API Security Top 10:** APIs (BOLA, quebra de auth, etc.).

Portais: <https://owasp.org/> · Top 10: <https://owasp.org/www-project-top-ten/> · WSTG: <https://owasp.org/www-project-web-security-testing-guide/>

Documento nosso: [OWASP Top 10](../web/owasp-top-10.md).

## CVSS na prática ofensiva/defensiva

Use CVSS como **linguagem com o GRC**, não como verdade absoluta.

Perguntas que o score não responde:

- Tem exploit público estável?
- O ativo é internet-facing?
- O dado é LGPD / segredo industrial?
- A correção quebra o negócio neste trimestre?

Um achado “médio” em AD com caminho até Domain Admin pode valer mais que um “crítico” em blog WordPress isolado.

## Como usar isso nos estudos

1. Pegue um incidente público (ransomware, breach) e mapeie 5 técnicas ATT&CK *em retrospecto*.
2. Pegue um CWE (ex.: 284, 287, 89 em conceito) e escreva **como defender** (validação, authz no servidor, least privilege).
3. Leia o Top 10 atual e anote *uma* pergunta de teste por classe — sem gravar payload.

## Leitura seguinte

- [OWASP Top 10](../web/owasp-top-10.md)
- [Detecção e logs](../defesa/deteccao-e-logs.md)
