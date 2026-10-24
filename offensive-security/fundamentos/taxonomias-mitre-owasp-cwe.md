# Taxonomias: ATT&CK, OWASP, CWE, CVSS e CAPEC

Sem um vocabulário comum, a mesma falha recebe nomes diferentes. A taxonomia não substitui o entendimento. Ela evita um relatório longo que ninguém consegue priorizar.

## MITRE ATT&CK

- **O que é:** base de conhecimento de *táticas* (objetivo: persistência, movimento lateral) e de *técnicas* (como, em alto nível).
- **No estudo ofensivo:** ver o que existe no incidente real e montar cobertura com o blue team.
- **O que não fazer:** tratar o ATT&CK como lista de missão para executar na internet.

Comece pelas matrizes **Enterprise** (Windows, Linux e nuvem). Leia a página da técnica: detecção, mitigação e exemplo. Site: <https://attack.mitre.org/>

**ATT&CK não é CVE.** O CVE identifica falha em produto. A técnica descreve comportamento. Muitas técnicas não têm CVE: conta válida e GPO fraca são exemplos.

## CAPEC

*Common Attack Pattern Enumeration and Classification*: padrão de ataque descrito como cenário, mais do que o ATT&CK (exemplo: forçar um caminho de diretório). Útil para desenhar teste e ameaça em AppSec. <https://capec.mitre.org/>

## CWE

*Common Weakness Enumeration*: fraqueza no *software* (validação, autorização, criptografia). Relatório de bug bounty e ferramenta de SAST usam CWE. <https://cwe.mitre.org/>

Relação típica: **CWE** (a classe no código), **CVE** (a instância em uma versão) e, quando explorada, um **padrão CAPEC** ou uma técnica ATT&CK.

## CVE e NVD

- **CVE:** identificador público de uma vulnerabilidade divulgada.
- **NVD e CVSS:** tentativa de pontuar a gravidade. Um CVSS alto não significa que a falha é explorável no seu contexto (sem rede, com MFA ou com WAF).

No relatório, cite o CVE se ele existir. **Contextualize**: pré-condição, se exige autenticação e qual dado é alcançável.

## OWASP

- **Top 10:** lista periódica das classes mais vistas em aplicação web. É um índice de estudo. Não é a lista completa do que existe.
- **ASVS:** requisito verificável (níveis 1 a 3) para construir e auditar.
- **WSTG:** *Web Security Testing Guide*. Descreve o que testar em cada área. Execute somente em alvo autorizado. Este repositório não copia os procedimentos.
- **MASVS e MASTG:** mobile.
- **API Security Top 10:** API (BOLA, quebra de autenticação e outras classes).

Portais: <https://owasp.org/> · Top 10: <https://owasp.org/www-project-top-ten/> · WSTG: <https://owasp.org/www-project-web-security-testing-guide/>

Documento deste guia: [OWASP Top 10](../web/owasp-top-10.md).

## CVSS na prática

Use o CVSS como **linguagem com a área de GRC**, não como verdade absoluta.

O score não responde a estas perguntas:

- Existe exploit público estável?
- O ativo está exposto à internet?
- O dado cai na LGPD ou é segredo industrial?
- A correção interrompe o negócio neste trimestre?

Um achado de severidade média no AD, com caminho até Domain Admin, pode valer mais que um achado crítico em um blog WordPress isolado.

## Como usar isto no estudo

1. Pegue um incidente público (ransomware ou vazamento) e mapeie 5 técnicas ATT&CK em retrospecto.
2. Pegue um CWE (por exemplo 284, 287 ou 89, em conceito) e escreva **como defender**: validação, autorização no servidor e privilégio mínimo.
3. Leia o Top 10 atual e anote uma pergunta de teste por classe. Não grave payload.

## Leitura seguinte

- [OWASP Top 10](../web/owasp-top-10.md)
- [Detecção e logs](../defesa/deteccao-e-logs.md)
