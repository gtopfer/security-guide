# Threat modeling (modelagem de ameaças)

Threat model responde: **quem** pode querer o quê, **por qual caminho**, e **o que já mitiga**. Ofensiva sem isso vira scanner. Defesa sem isso vira checklist CIS copiado.

## Perguntas STRIDE (Microsoft, clássico)

Use como *brainstorm*, não como verdade:

| Letra | Classe | Pergunta |
|-------|--------|----------|
| S | Spoofing | Posso fingir identidade? |
| T | Tampering | Posso alterar dado em trânsito ou em repo? |
| R | Repudiation | Dá para negar que fez? (falta de log) |
| I | Information disclosure | Dado vaza? |
| D | Denial of service | Consigo derrubar? (muitas vezes fora de ROE) |
| E | Elevation of privilege | Consigo mais poder? |

## Outros óculos

- **LINDDUN** — privacidade.
- **Attack trees** — objetivo na raiz, caminhos nas folhas.
- **Pastas PASTA / OCTAVE** — mais processo de empresa; saiba que existem.

## Como praticar em uma tarde

Pegue um sistema que você use (o próprio Security Guide publicado no GitHub, um Juice Shop, um bot de Discord):

1. Liste ativos e atores (usuário anônimo, admin, CI, dependabot).
2. Para cada fronteira (internet→app, app→banco, CI→prod), uma hipótese STRIDE.
3. Marque o que *já* é controle e o que é só esperança.
4. Compare com um pentest: o teste só vale nas hipóteses in-scope.

## Relação com ATT&CK

ATT&CK entra *depois*: “se o ator for ransomware humano, quais técnicas são plausíveis *nesta* rede?”. Não comece o modelo pela matriz inteira.

## Leitura

- Microsoft Threat Modeling: <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool>
- OWASP Threat Dragon (FOSS): <https://owasp.org/www-project-threat-dragon/>
