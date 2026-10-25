# Canais

O canal é o meio. O pretexto é a história. A mesma história muda de meio. Leia o pedido, não só o meio.

Cada seção diz o que a pessoa **vê**. A ação está nos [sinais](sinais-de-alerta.md) e nos [playbooks](playbooks.md).

## Phishing

Phishing é uma mensagem que imita um remetente confiável. O pedido costuma ser um clique, um anexo, uma senha ou um código.

Nomes úteis, sem receita:

| Nome | O que muda para quem recebe |
|------|-----------------------------|
| Phishing em massa | A história serve para muita gente. O tema é genérico. |
| Spear phishing | A história cita a pessoa, o cargo ou um fato interno. |
| Whaling | O alvo aparente é chefia ou área financeira. |
| Anexo ou link | O arquivo ou o endereço pede abertura ou login. |
| Consentimento de aplicativo | A página pede permissão para ler caixa de e-mail ou arquivo. |

O nome de exibição pode ser conhecido. O endereço pode ser outro. No computador, passe o ponteiro sobre o link e leia o destino. Não clique para descobrir o destino. No celular, não há essa conferência. Não toque no link. O destino visível ainda pode imitar a marca. Na dúvida, pare.

Uma conta legítima comprometida envia phishing com endereço verdadeiro. SPF, DKIM e DMARC não provam a intenção de quem escreveu. Veja [autenticação de e-mail](playbooks.md#autenticação-de-e-mail).

A técnica correspondente no ATT&CK é a [T1566](https://attack.mitre.org/techniques/T1566/). Leia as seções de detecção e de mitigação. Não use a página como roteiro.

## Vishing

Vishing é phishing por voz. A ligação imita banco, suporte, entregador, autoridade ou chefia.

O pedido típico é um código de verificação, uma senha, uma transferência ou a instalação de acesso remoto. A voz pode parecer conhecida. Voz parecida não confirma identidade. Áudio sintético existe. A defesa não depende de "reconhecer a voz".

Se a ligação exige ação, encerre a ligação. Confira por um número que você já tinha. Não use o número que a ligação ditou.

A técnica de voz no ATT&CK inclui [T1566.004](https://attack.mitre.org/techniques/T1566/004/).

## Pretexting

Pretexting é o uso de um papel falso e de uma história falsa. O papel pode ser suporte, RH, auditor, fornecedor ou colega.

A história pede uma exceção. A exceção pode ser senha temporária, dado de cliente, crachá, porta aberta ou silêncio. A pressa e o cargo substituem o processo.

Confira a identidade por um canal já registrado. O dado que a pessoa acabou de ditar não prova a identidade. No prédio, não segure a porta e não empreste o crachá fora do processo.

A classe de personificação no ATT&CK inclui [T1656](https://attack.mitre.org/techniques/T1656/).

## Notas curtas

### Smishing

Smishing é phishing por SMS ou por aplicativo de mensagem. O texto é curto. O link é curto. O tema costuma ser entrega, banco, pedágio ou código.

Não abra o link. Confira o aplicativo oficial ou o número que já estava salvo. Não devolva um pagamento para uma conta que a mensagem indicou.

### Fraude de e-mail corporativo (BEC)

BEC (*business e-mail compromise*) é a fraude que usa uma caixa de e-mail ou uma imitação dela. O pedido muda conta de fornecedor, pede pagamento urgente ou pede vale-presente. O nome "fraude do CEO" é o caso em que o papel é a chefia.

A mensagem pode vir de uma conta real já comprometida. Por isso a autenticação do domínio não basta.

Pare o pagamento. Confira com a outra parte por um telefone ou um canal que o contrato já tinha. Exija o segundo aprovador quando o processo o exige. Reporte mesmo se você recusou o pedido.

### Isca (baiting)

Isca é um objeto ou um arquivo que se oferece como útil, perdido ou grátis. O caso físico comum é a mídia removível achada. O caso digital é o download que você não pediu.

Não conecte mídia desconhecida. Não execute arquivo inesperado. Entregue a mídia ao processo da organização, se existir.

### Código QR

O código QR esconde o endereço. A pessoa vê um desenho, não o domínio.

Não leia um QR de mensagem, de cartaz ou de carta inesperada. Digite o endereço que você já conhece.

### Phishing interno

Depois que uma caixa cai, a tentativa segue para colegas. O remetente é interno. O pedido ainda pode ser falso.

Trate o pedido interno com o mesmo processo do pedido externo. A técnica [T1534](https://attack.mitre.org/techniques/T1534/) descreve essa classe. A contenção da caixa está no [playbook](playbooks.md#conter-uma-conta).

## Leitura seguinte

- [Sinais de alerta](sinais-de-alerta.md)
- [Playbooks](playbooks.md)
