# Reconhecimento passivo e ativo

A diferença não é "ético" contra "antiético". Os dois modos exigem autorização quando o alvo não é seu. A diferença é **quem recebe o seu tráfego** e **quanto ruído você gera**.

## Passivo

Você consome dado que **já foi publicado**, ou que um terceiro coletou, sem enviar pacote ao alvo:

- WHOIS e RDAP
- Certificate Transparency
- Arquivo (Wayback, Common Crawl)
- DNS de resolvedor público e conjunto passivo, quando a fonte é de terceiro
- Código público, documentação, vaga e loja de aplicativo
- Índice já coletado por Shodan ou Censys (a consulta em si não é um scan seu; o uso no cliente ainda precisa estar nas regras de engajamento)

**Vantagem:** pouco rastro no alvo. Serve ao início do trabalho e à inteligência de ameaça.  
**Limite:** o dado fica desatualizado. Ele não prova que o serviço ainda está no ar. Ele não substitui a validação.

## Ativo

Você **envia tráfego** ao sistema no escopo: resolução direta, TCP ou UDP, HTTP, rastreador e autenticação com conta de teste.

**Vantagem:** descreve o estado atual.  
**Risco:** log, IDS, quebra de termo de uso e efeito colateral (impressora, sistema industrial, volume). Algumas regras de engajamento proíbem varredura ampla de porta ou restringem o horário.

## Comparação

| Pergunta | Passivo | Ativo |
|----------|---------|--------|
| O domínio aparece no Certificate Transparency? | Sim | — |
| O host responde na porta 443 agora? | Não prova | Sim |
| Qual software escuta a porta 22? | Às vezes um banner antigo em base de terceiro | A conexão, se permitida |
| O SOC vê a atividade? | Quase não | Quase sempre |

## Regras práticas de estudo

1. Treine primeiro o reconhecimento passivo em alvo público de exemplo (`example.com` é de documentação; ainda assim, não abuse) e na sua organização, se você tiver permissão.
2. Reconhecimento ativo: somente laboratório ou escopo. Entenda o que um SYN scan é (modelo TCP) antes de executar uma varredura de todas as portas.
3. Não misture a lista de um programa de bug bounty com uma varredura de um ASN inteiro. Os programas costumam proibir isso.

## Ferramentas neste repositório

A coleção OSINT lista enumerador de subdomínio, httpx, gau e outras ferramentas. A coleção de pentest lista scanner. **Instalar a ferramenta não autoriza apontá-la para a internet.** Leia o aviso de cada README.

## Leitura seguinte

- [Mapeamento de superfície](mapeamento-de-superficie.md)
- [Ética](../fundamentos/etica-e-lei.md)
