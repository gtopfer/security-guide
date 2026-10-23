# Ética, escopo e lei

Segurança ofensiva sem autorização não é “estudo”: é risco jurídico para você e para quem hospeda o alvo. Este texto não é aconselhamento jurídico; é o mínimo que o guia assume.

## Autorização por escrito

Antes de qualquer teste em sistema que não seja 100% seu:

- Quem autoriza (empresa, dono do domínio, programa de bounty).
- **Escopo**: hosts, apps, APIs, contas, janela de horário, regiões.
- **Fora de escopo**: DoS, engenharia social, acesso físico, terceiros (SaaS do cliente), exfiltração de dados reais.
- **Regras de engajamento (ROE)**: o que fazer se achar ransomware, dado pessoal, ou se o sistema cair.
- Canal de emergência (telefone/Slack) se o teste afetar produção.

Print de “pode testar” no chat não substitui um e-mail ou contrato com data e lista de alvos.

## Distinções úteis

| Situação | Em geral |
|----------|----------|
| Lab local (Juice Shop no seu Docker) | OK |
| CTF / HTB / TryHackMe com ToS | OK dentro da plataforma |
| Bug bounty, *in scope* | OK se seguir as regras do programa |
| Servidor da empresa sem ticket | Não |
| “O site está na internet, então é fair game” | Não |
| Escanear a rede da escola/vizinho “para aprender” | Não |
| Usar dorks no Google sobre *você mesmo* | OK (pegada digital) |
| Abrir Drive/pasta de terceiro que apareceu no Google | Cuidado: indexado ≠ autorizado a copiar/usar |

## Brasil (visão de estudo)

Leia as fontes oficiais; não memorize “jeitinho”:

- **Lei 12.737/2012** (Carolina Dieckmann) — invasão de dispositivo, interrupção, dados.
- **Marco Civil da Internet** (Lei 12.965/2014) — guarda de logs, privacidade, responsabilidade.
- **LGPD** (Lei 13.709/2018) — dado pessoal no relatório de pentest precisa de base legal e minimização.
- Contratos e CLT: testar o empregador sem mandato da área de segurança também pode ser falta grave.

Jurisdição do *alvo* importa: um SaaS nos EUA tem CFAA; um programa de bounty descreve *safe harbor* só para o que está no escopo.

## Disclosure

**Responsável:** avisar o dono com prazo razoável, sem publicar exploit enquanto a correção é possível.

**Coordenado:** CERT.br, PSIRT do vendor, ou plataforma de bounty.

**Full disclosure imediato** de falha grave em sistema de terceiro, sem aviso, costuma prejudicar usuários e pode ser ilegal dependendo do conteúdo publicado.

Não venda acesso, não ameace (“paga ou eu divulgo”) — isso sai de pesquisa e entra em extorsão.

## Conduta no lab e no relatório

- Minimize dados: hashes e IDs no relatório, não planilha de CPF de produção.
- Não mantenha shells, contas nem backdoors depois do engajamento.
- Não use o lab do cliente como proxy para atacar outra rede.
- Ferramentas de força bruta e scanners ruidosos só se o ROE permitir — e com rate limit.

## Código de conduta deste repositório

O [CONTRIBUTING.md](../../CONTRIBUTING.md) recusa conteúdo que ensine atividade ilegal. Contribuições nesta pasta devem permanecer **conceituais** ou apontar para labs oficiais — sem PoC de exploit, sem payload, sem passo a passo de invasão.

## Leitura seguinte

- [Mentalidade e método](mentalidade-e-metodo.md)
- [Labs legais](../pratica/labs-legais.md)
