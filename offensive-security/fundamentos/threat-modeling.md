# Threat modeling (modelagem de ameaças)

O modelo de ameaça responde três perguntas. **Quem** pode querer o quê. **Por qual caminho**. **O que já mitiga** esse caminho. Ofensiva sem esse modelo vira execução de scanner. Defesa sem esse modelo vira cópia de checklist.

## Perguntas STRIDE (Microsoft)

Use a tabela como lista de perguntas, não como conclusão automática.

| Letra | Classe | Pergunta |
|-------|--------|----------|
| S | Spoofing | Posso me passar por outra identidade? |
| T | Tampering | Posso alterar dado em trânsito ou no repositório? |
| R | Repudiation | A pessoa pode negar a ação por falta de log? |
| I | Information disclosure | O dado vaza? |
| D | Denial of service | Consigo tornar o serviço indisponível? Em geral, isto fica fora das regras de engajamento. |
| E | Elevation of privilege | Consigo obter mais privilégio? |

## Outros modelos

- **LINDDUN** — privacidade.
- **Árvore de ataque** — o objetivo fica na raiz e os caminhos ficam nas folhas.
- **PASTA e OCTAVE** — processos de empresa. Saiba que existem.

## Como praticar em uma sessão

Escolha um sistema que você usa: este Security Guide no GitHub, um Juice Shop ou um bot de Discord.

1. Liste ativo e ator (usuário anônimo, administrador, CI, Dependabot).
2. Para cada fronteira (internet para aplicação, aplicação para banco, CI para produção), escreva uma hipótese STRIDE.
3. Marque o que já é controle e o que é apenas expectativa.
4. Compare com um pentest: o teste só vale para a hipótese que está no escopo.

## Relação com o ATT&CK

O ATT&CK entra depois. A pergunta é: se o ator for um operador de ransomware, quais técnicas são plausíveis nesta rede? Não comece o modelo pela matriz inteira.

## Leitura

- Microsoft Threat Modeling: <https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool>
- OWASP Threat Dragon (software livre): <https://owasp.org/www-project-threat-dragon/>
