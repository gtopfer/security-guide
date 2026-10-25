# Sinais de alerta

Use esta página como lista de conferência. Um sinal basta para parar. Você não precisa fechar uma lista inteira.

A ação curta está na coluna da direita. O procedimento completo está nos [playbooks](playbooks.md).

## Para quem recebe

| Sinal | Ação |
|-------|------|
| Urgência, ameaça de bloqueio ou prazo de minutos | Pare. Reporte. |
| Pedido de sigilo ("não conte a ninguém") | Pare. Reporte. |
| Pedido de senha, código de uso único ou chave de recuperação | Pare. Não informe o dado. Reporte. |
| Pedido para aprovar vários avisos de login | Recuse todos. Reporte. |
| Pedido de pagamento, vale ou mudança de conta bancária | Pare. Confira por um canal já registrado. |
| Pedido para instalar acesso remoto | Recuse. Reporte. |
| Nome de exibição conhecido e endereço desconhecido | Pare. Confira o endereço. Não responda. |
| Link cujo destino não é o texto visível | Não clique. Reporte. |
| Anexo que você não pediu | Não abra. Reporte. |
| Código QR inesperado | Não leia o código. Digite o endereço conhecido, se precisar. |
| Ligação que dita o número de retorno | Encerre. Use um número que você já tinha. |
| Mídia removível achada ou brinde digital | Não conecte. Não execute. |
| Página que pede permissão ampla a um aplicativo | Não aceite. Reporte. |

## Para service desk e SOC

| Sinal | Ação |
|-------|------|
| Vários reportes com o mesmo assunto, domínio ou número | Registre um caso só. Confira o volume. |
| Login novo logo após um reporte de phishing | Isole a conta. Siga a [contenção](playbooks.md#conter-uma-conta). |
| Regra nova de encaminhamento, exclusão ou delegação | Remova a regra. Isole a conta. |
| Aplicativo novo com acesso à caixa ou a arquivo | Remova o acesso que ninguém pediu. Isole a conta. |
| Muitos pedidos de MFA em sequência | Oriente a recusa. Isole a conta se houve aprovação. |
| Pedido de redefinição com urgência, cargo ou sigilo | Não troque a senha. Confira a identidade por canal já registrado. Reporte. |
| Pedido para ler um código ou instalar acesso remoto | Recuse. Reporte. |
| Mudança de dado bancário fora do processo | Pare o pagamento. Confira pelo contato do contrato. |
| Pico de falha de DMARC no domínio da organização | Registre. Confira se o domínio visível está sendo imitado. |
| Mensagem interna que espalha link ou anexo inesperado | Isole a caixa de origem. Avise o grupo afetado sem reencaminhar o anexo. |

## O que não inocenta a mensagem

Estes fatos **não** fecham o caso como legítimo.

- A gramática está correta. Mensagem bem escrita também é golpe.
- SPF, DKIM ou DMARC passou. Conta legítima comprometida também passa.
- O nome de exibição é de um colega. O nome de exibição não é o endereço.
- A pessoa cita um dado interno. Dado interno vaza e também é público.
- A voz parece familiar. Voz parecida não confirma identidade.

## O que registrar na hora

Registre só o necessário.

- Data, hora e fuso.
- Canal.
- Remetente visível e endereço ou número, se existir.
- Pedido, em uma frase.
- O que a pessoa já fez (nada, clique, dado, pagamento, programa).
- Conta ou processo afetado.

Não grave senha, código de uso único nem documento completo. Não publique esse registro. A [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) se aplica ao dado pessoal.

## Leitura seguinte

- [Playbooks](playbooks.md)
- [Phishing no guia para iniciantes](../for-noobs/README.md#7-phishing-e-engenharia-social)
- [Estudos ofensivos (somente conceito)](estudos-ofensivos/README.md)
