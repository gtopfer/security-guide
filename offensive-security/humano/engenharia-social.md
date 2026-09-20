# Engenharia social (estudo de classe de risco)

O humano é interface. Ofensiva real combina pretexto + canal (e-mail, telefone, presencial) + um pedaço técnico (página falsa, USB, “TI pediu o código”). Este guia trata **reconhecimento do risco e defesa**. Não ensina a montar golpe contra pessoas.

## Pretexto

História plausível: RH, suporte, fornecedor, urgência. Urgência e medo são os aceleradores — o [for-noobs](../../for-noobs/README.md) já descreve isso para o usuário comum.

## Canais

- E-mail (phishing, BEC — *business email compromise*)
- Mensageria / SMS (smishing)
- Voz (vishing, SIM swap *como ameaça*)
- Presencial / crachá / “segurou a porta”
- Deepfake de voz/vídeo (classe emergente)

## O que um red team *contratado* combina

Escopo **explícito** de social: quem pode ser alvo (não o CEO internado, não clientes), o que é proibido (não pedir dinheiro, não assustar família), como consentir depois (debrief). Sem isso, não faça.

## Defesa que realmente escala

- FIDO2 / chaves: phishing de senha perde valor.
- Processos: tesouraria confirma fora de banda.
- DMARC/SPF/DKIM + marcação de e-mail externo.
- Least privilege: estagiário não reseta senha de DA.
- Cultura sem humilhar quem reporta o clique.

## OSINT e pessoas

Sherlock, dumps, organogramas: no pentest, servem para **mostrar exposição da org**. Usar para assediar indivíduo é abuso e pode ser crime. Ver ética.

## Leitura seguinte

- [Ética](../fundamentos/etica-e-lei.md)
- [for-noobs: phishing](../../for-noobs/README.md)
