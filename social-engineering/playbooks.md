# Playbooks de defesa

Cada procedimento começa pela condição. Execute os passos na ordem.

> Se o exercício usa pessoa real, obtenha autorização por escrito antes. Não colete senha real. Não publique alvo, resultado, modelo de mensagem nem prova de cliente. Acesso sem autorização pode violar a [Lei 12.737/2012](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm). Dado pessoal cai na [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Este texto não é aconselhamento jurídico.

## Reportar uma tentativa

Faça isto quando uma mensagem, uma ligação, um SMS ou uma visita pede dado, dinheiro, código ou acesso.

1. Pare. Não clique. Não abra anexo. Não responda. Não ligue para o número que veio na mensagem.
2. Se você precisa saber se o assunto é real, confira por um canal que você já tinha. Digite o endereço conhecido ou use a agenda. Não use o contato que a tentativa ofereceu.
3. Reporte no canal oficial da organização. Use o botão de reporte do cliente de e-mail, se existir. O botão envia o caso ao time sem espalhar o anexo.
4. Se não há canal interno, reporte ao [CERT.br](https://www.cert.br/contato/). Se houve prejuízo, avise também a autoridade policial competente.
5. Registre horário, canal, remetente e o que você fez. O modelo mínimo está em [sinais de alerta](sinais-de-alerta.md#o-que-registrar-na-hora).
6. Se você já clicou, já informou dado, já aprovou um aviso ou já pagou, siga a contenção. Não espere o fim do expediente.

Não encaminhe o anexo para caixas pessoais "para pedir opinião".

## Conter uma conta

Faça isto quando a senha, o código, a sessão ou a caixa pode estar com outra pessoa. Faça isto também quando a pessoa instalou um programa a pedido do contato.

1. Isole o dispositivo da rede se houve anexo aberto ou programa instalado a pedido.
2. Troque a senha em um dispositivo que você ainda confia.
3. Encerre as sessões ativas dessa conta.
4. Confira e-mail de recuperação, telefone, aplicativo autenticador e chaves. Remova o que você não reconhece.
5. Confira regras da caixa, encaminhamento, delegação e aplicativos conectados. Remova o que você não reconhece.
6. Confira itens enviados recentes. Avise os contatos se a conta enviou tentativa de golpe. Não reenvie o anexo.
7. Se houve pagamento ou dado bancário, avise o banco e peça o bloqueio do que ainda for possível.
8. Registre o caso e entregue o registro ao time de resposta. Não publique senha, código nem dado de cliente.

A versão para conta pessoal, com a mesma ordem de contenção, está no [guia para iniciantes](../for-noobs/README.md#10-resposta-a-comprometimento).

## Service desk

Faça isto quando o pedido é redefinição de senha, dado interno ou acesso, e o pedido chegou por ligação ou mensagem.

1. Pare quando o pedido exige sigilo ou foge do processo escrito.
2. Confira a identidade por um canal já registrado. O dado que a pessoa acabou de informar não prova quem ela é.
3. Não leia código de MFA para quem ligou.
4. Não instale acesso remoto por causa dessa ligação.
5. Não troque a senha enquanto a conferência não fechar.
6. Reporte o pedido ao time de segurança. Registre horário e número. Não acrescente dado além do que a política pede.

## Pagamento e BEC

Faça isto quando o pedido muda conta bancária, pede pagamento urgente ou pede vale-presente.

1. Pare o pagamento. Não responda com comprovante.
2. Confira com o fornecedor ou com a chefia por telefone ou canal que o contrato já tinha. Não use o contato da mensagem.
3. Exija o segundo aprovador, se o processo já o exige.
4. Reporte o pedido, mesmo quando você recusou.
5. Se o pagamento já saiu, avise o banco e o time financeiro. Registre horário e valor. Não publique o comprovante fora do processo.

## Autenticação de e-mail

Esta seção é conceitual. Não publique aqui um registro DNS de produção. Leia a norma e a política da organização antes de alterar DNS.

| Controle | Função | Limite |
|----------|--------|--------|
| SPF | Publica quais servidores podem enviar em nome do domínio | Não prova quem escreveu o texto |
| DKIM | Assina a mensagem. A assinatura liga a mensagem a um domínio | Um encaminhamento pode quebrar a assinatura |
| DMARC | Diz o que fazer quando SPF ou DKIM não alinha com o domínio visível | Não pega isca enviada de um domínio parecido |
| Alinhamento | O domínio visível e o domínio autenticado precisam concordar | Conta legítima comprometida continua alinhada |
| Marca de remetente externo | Mostra que a mensagem veio de fora | Não aparece no remetente interno comprometido |
| Filtro de anexo e de link | Segura arquivo e endereço suspeitos antes da caixa | Não substitui o reporte da pessoa |
| Fator resistente a phishing | FIDO2 ou equivalente não entrega a senha para uma página falsa | Não impede pagamento autorizado por engano |

Política DMARC, em linguagem de operação: monitorar, quarentena ou rejeição. Rejeição no domínio que você controla reduz imitação **desse** domínio. Ela não cobre um domínio visualmente parecido.

Fonte primária: [RFC 7208](https://www.rfc-editor.org/rfc/rfc7208) (SPF), [RFC 6376](https://www.rfc-editor.org/rfc/rfc6376) (DKIM), [RFC 7489](https://www.rfc-editor.org/rfc/rfc7489) (DMARC) e [NIST SP 800-177 Rev. 1](https://csrc.nist.gov/pubs/sp/800/177/r1/final).

## Treino de conscientização

Treine o reporte. Não treine o medo.

1. Publique um canal de reporte e mostre o botão no cliente de e-mail.
2. Repita sessões curtas. Um evento anual não basta.
3. Use material pronto do [CERT.br](https://cartilha.cert.br/fasciculos/#golpes) e da [CISA](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing). Não escreva isca nova neste repositório.
4. Não humilhe quem reportou. Não humilhe quem clicou. Acolha o reporte.
5. Meça o tempo até o reporte. Não publique ranking de "quem caiu".
6. Se houver exercício com pessoa real, obtenha autorização por escrito antes. Defina quem está fora do exercício. Não inclua dado de saúde, família nem cliente.
7. Não colete senha real no exercício. Não guarde dado pessoal além do necessário. Apague o dado no prazo definido.
8. Não publique resultado, alvo nem modelo neste repositório.

A norma de programa de aprendizado é a [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final). A mitigação de treino no ATT&CK é a [M1017](https://attack.mitre.org/mitigations/M1017/). A mitigação de MFA é a [M1032](https://attack.mitre.org/mitigations/M1032/).

## Leitura seguinte

- [Referências](referencias.md)
- [Detecção e logs](../offensive-security/defesa/deteccao-e-logs.md)
