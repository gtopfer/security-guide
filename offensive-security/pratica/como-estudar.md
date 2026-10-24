# Como estudar segurança ofensiva

Não há trilha de certificação neste guia. O objetivo é **vocabulário, modelo mental e prática em laboratório legal**.

## Ordem sugerida (temas, não prazo de marketing)

1. Ética e lei — [etica-e-lei](../fundamentos/etica-e-lei.md)
2. Redes, até o TCP fazer sentido — [redes](../redes/modelo-tcpip-e-servicos.md)
3. Linux do dia a dia (usuário, permissão, journal) e HTTP, até o cookie fazer sentido
4. OWASP Top 10 como índice, mais PortSwigger Academy ou Juice Shop
5. Identidade: sessão, visão geral de OAuth e, se for o seu contexto, Active Directory
6. Nuvem de um provedor, na sua conta
7. Relatório: escreva um achado de laboratório como se o leitor fosse o cliente
8. Purple team: ligue um log e observe o que o seu próprio teste gerou

Se você omitir o passo 7, o estudo para em coletar flag.

## Anotação

Para cada tema, use uma página:

- Definição em uma frase
- Premissa que falha
- Controle preventivo e controle detectivo
- Link oficial (RFC, Microsoft, OWASP)
- Laboratório em que você praticou (nome da plataforma, não um writeup de exploit copiado)

## O que não fazer

- Acumular 200 ferramentas sem concluir um laboratório inicial.
- Seguir um writeup automático sem explicar o modelo.
- Testar a rede da família, da faculdade ou da empresa sem autorização por escrito.
- Tratar CTF como se fosse pentest.

## Ligação com este repositório

- Proteção pessoal: `for-noobs/`
- OSINT (reconhecimento): `osint-tools-collection/`
- Ferramentas ofensivas de software livre: `pentest-tools-collection/`
- Mapa de tema para Git: [mapa-ferramentas.md](../biblioteca/mapa-ferramentas.md)
- Conceitos: esta pasta

## Leitura seguinte

- [Laboratórios legais](labs-legais.md)
- [Cursos gratuitos](../biblioteca/cursos-gratuitos.md)
