# Engenharia social (classe de risco)

A pessoa é uma interface do sistema. O ataque real combina pretexto, canal (e-mail, telefone, presença) e um componente técnico (página falsa, USB ou um pedido em nome da TI). Este guia trata o **reconhecimento do risco e a defesa**. Não ensina a montar golpe contra pessoas.

## Pretexto

O pretexto é uma história plausível: RH, suporte, fornecedor, urgência. Urgência e medo aceleram a decisão. O guia [para iniciantes](../../for-noobs/README.md) descreve isso para o usuário comum.

## Canais

- E-mail (phishing e comprometimento de e-mail corporativo, ou BEC)
- Mensagem e SMS (smishing)
- Voz (vishing e troca de chip como ameaça)
- Presença física, crachá e acesso por acompanhar outra pessoa na porta
- Deepfake de voz ou de vídeo (classe em crescimento)

## O que um red team contratado combina antes

O escopo de engenharia social é **explícito**. Ele define quem pode ser alvo. Não inclui pessoa em situação de saúde grave nem cliente. Define o que é proibido: não pedir dinheiro e não assustar a família. Define o debrief depois do exercício. Sem esse acordo, não execute o teste.

## Defesa que escala

- FIDO2 e chave de segurança: o phishing de senha perde valor.
- Processo: a tesouraria confirma o pagamento por um canal separado.
- DMARC, SPF e DKIM, mais a marcação de e-mail externo.
- Privilégio mínimo: um estagiário não redefine a senha de Domain Admin.
- Cultura que não humilha quem reporta o clique.

## OSINT e pessoas

Sherlock, dump e organograma, no pentest, mostram a **exposição da organização**. Usar esse material para assediar uma pessoa é abuso e pode ser crime. Veja a página de ética.

## Leitura seguinte

- [Ética](../fundamentos/etica-e-lei.md)
- [Phishing no guia para iniciantes](../../for-noobs/README.md)
