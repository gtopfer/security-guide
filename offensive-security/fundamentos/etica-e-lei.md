# Ética, escopo e lei

Segurança ofensiva sem autorização não é estudo. É risco jurídico para você e para quem hospeda o alvo. Este texto não é aconselhamento jurídico. É o mínimo que este guia assume.

## Autorização por escrito

Antes de qualquer teste em sistema que não seja inteiramente seu, registre:

- Quem autoriza (empresa, dono do domínio ou programa de bug bounty).
- O **escopo**: host, aplicação, API, conta, janela de horário e região.
- O que está **fora de escopo**: negação de serviço, engenharia social, acesso físico, terceiro (SaaS do cliente) e exfiltração de dado real.
- As **regras de engajamento**: o que fazer se você encontrar ransomware, dado pessoal, ou se o sistema cair.
- O canal de emergência (telefone ou chat) se o teste afetar produção.

Uma mensagem de "pode testar" no chat não substitui e-mail ou contrato com data e lista de alvos.

## Situações comuns

| Situação | Em geral |
|----------|----------|
| Laboratório local (Juice Shop no seu Docker) | Permitido |
| CTF, Hack The Box ou TryHackMe, dentro dos termos de uso | Permitido na plataforma |
| Bug bounty, dentro do escopo | Permitido se você seguir as regras do programa |
| Servidor da empresa sem chamado autorizado | Não permitido |
| "O site está na internet, então o teste é livre" | Não permitido |
| Escanear a rede da escola ou do vizinho para aprender | Não permitido |
| Usar dork no Google sobre você mesmo | Permitido (pegada digital) |
| Abrir arquivo de terceiro que apareceu no Google | Cuidado: indexado não significa autorizado a copiar ou a usar |

## Brasil (visão de estudo)

Leia a fonte oficial. Não substitua o texto da lei por um resumo informal.

- **Lei 12.737/2012**: invasão de dispositivo, interrupção de serviço e dado.
- **Marco Civil da Internet** (Lei 12.965/2014): guarda de log, privacidade e responsabilidade.
- **LGPD** (Lei 13.709/2018): dado pessoal no relatório de pentest exige base legal e minimização.
- Contrato e vínculo de trabalho: testar o empregador sem mandato da área de segurança pode ser falta grave.

A jurisdição do **alvo** importa. Um SaaS nos Estados Unidos pode cair sob o CFAA. Um programa de bug bounty descreve proteção legal somente para o que está no escopo.

## Disclosure

**Responsável:** avise o dono com prazo razoável. Não publique o exploit enquanto a correção ainda é possível.

**Coordenado:** use o CERT.br, o PSIRT do fornecedor ou a plataforma de bug bounty.

**Divulgação imediata** de falha grave em sistema de terceiro, sem aviso prévio, prejudica usuários. Dependendo do conteúdo publicado, pode ser ilegal.

Não venda acesso. Não ameace com a frase "paga ou eu divulgo". Isso deixa de ser pesquisa e passa a ser extorsão.

## Conduta no laboratório e no relatório

- Minimize o dado: use hash e identificador no relatório. Não anexe planilha de CPF de produção.
- Não mantenha shell, conta nem backdoor depois do trabalho.
- Não use o laboratório do cliente como proxy para atacar outra rede.
- Use força bruta e scanner ruidoso somente se as regras de engajamento permitirem, e com limite de taxa.

## Código de conduta deste repositório

O [CONTRIBUTING.md](../../CONTRIBUTING.md) recusa conteúdo que ensine atividade ilegal. Uma contribuição nesta pasta permanece **conceitual** ou aponta para laboratório oficial. Sem prova de conceito de exploit, sem payload e sem passo a passo de invasão.

## Leitura seguinte

- [Mentalidade e método](mentalidade-e-metodo.md)
- [Laboratórios legais](../pratica/labs-legais.md)
