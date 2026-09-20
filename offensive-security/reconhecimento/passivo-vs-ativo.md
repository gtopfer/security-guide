# Recon passivo vs ativo

A diferença não é “ético vs antiético”. Os dois exigem autorização quando o alvo não é seu. A diferença é **quem você toca** e **quanto ruído gera**.

## Passivo

Você consome dados que **já foram publicados** ou que um terceiro coletou sem você enviar pacote ao alvo:

- WHOIS, RDAP
- Certificate Transparency
- Arquivos (Wayback, Common Crawl)
- DNS de resolvedores públicos / conjuntos passivos (quando a fonte é de terceiros)
- Código público, docs, vagas, App Stores
- Shodan/Censys *já indexados* (a consulta em si não é um scan seu — ainda assim o uso no cliente precisa estar no ROE)

**Vantagem:** pouco rastro no alvo, bom para kickoff e threat intel.  
**Limite:** desatualiza; não prova que o serviço *ainda* está lá; não substitui validação.

## Ativo

Você **envia tráfego** ao sistema no escopo: resolução direta, TCP/UDP, HTTP, crawlers, autenticação com conta de teste.

**Vantagem:** verdade do momento.  
**Riscos:** logs, IDS, quebra de ToS, efeito colateral (impressora, ICS, volume). Alguns ROEs proíbem scan de porta amplo ou restringem horário.

## Tabela mental

| Pergunta | Passivo | Ativo |
|----------|---------|--------|
| O domínio existe na CT? | Sim | — |
| O host responde 443 agora? | Não prova | Sim |
| Qual software na porta 22? | Às vezes um banner antigo em DB | Conexão (se permitido) |
| Visível para o SOC? | Quase não | Quase sempre |

## Regras práticas de estudo

1. Treine **primeiro** recon passivo em alvos públicos de exemplo (`example.com` é de documentação; ainda assim não abuse) e na *sua* org se tiver permissão.
2. Recon ativo: só lab ou escopo. Comece entendendo o que um SYN scan *é* (modelo TCP) antes de sair clicando em “full port”.
3. Nunca misture lista de bug bounty com “vou masscan a ASN inteira” — programas costumam vetar isso.

## Ferramentas neste repo

A coleção OSINT lista enumeradores de subdomínio, httpx, gau, etc. A coleção de pentest lista scanners. **Instalar ≠ apontar para a internet.** Leia o aviso de cada README.

## Leitura seguinte

- [Mapeamento de superfície](mapeamento-de-superficie.md)
- [Ética](../fundamentos/etica-e-lei.md)
