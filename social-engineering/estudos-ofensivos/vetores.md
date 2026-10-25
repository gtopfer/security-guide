# Vetores (conceito)

O vetor é o meio do contato. A trilha de defesa usa a palavra canal para o mesmo meio. Leia o que a pessoa vê em [Canais](../canais.md). Esta página não repete o playbook.

O escopo nomeia o vetor antes do exercício. Um vetor fora da lista fica fora do exercício.

> Não contate pessoa real sem autorização por escrito. Acesso sem autorização pode violar a [Lei 12.737/2012](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm). Privacidade e registro de acesso estão no [Marco Civil](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm). Dado pessoal está na [LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Este texto não é aconselhamento jurídico. O registro está em [Quando o estudo é permitido](autorizacao.md).

Cada seção abaixo diz o que o vetor é. A seção diz o item que o escopo registra. A seção não traz texto de isca.

No ATT&CK, leia detecção e mitigação. Não use a página da técnica como roteiro.

## E-mail

O vetor de e-mail é a mensagem que imita um remetente confiável. A defesa separa phishing em massa, spear phishing e whaling em [Phishing](../canais.md#phishing). A diferença é o grau de especificidade da história.

A classe no ATT&CK é a [T1566](https://attack.mitre.org/techniques/T1566/). Phishing para obter informação é a [T1598](https://attack.mitre.org/techniques/T1598/).

O escopo registra se a mensagem está permitida, qual grupo pode recebê-la e qual é a janela. Este texto não traz assunto, corpo, página nem anexo.

Fraude de e-mail corporativo (BEC) é a classe em que o pedido muda um pagamento. A defesa está em [BEC](../canais.md#fraude-de-e-mail-corporativo-bec).

## Voz

O vetor de voz é a ligação ou o áudio que imita um papel confiável. A defesa descreve o que a pessoa ouve em [Vishing](../canais.md#vishing). Áudio parecido com uma voz conhecida não confirma identidade.

A classe de voz no ATT&CK inclui a [T1566.004](https://attack.mitre.org/techniques/T1566/004/).

O escopo registra se a voz está permitida e se áudio gravado está fora. Este texto não traz fala pronta.

## Mensagem curta

O vetor de mensagem curta é o SMS ou o aplicativo de mensagem. A defesa descreve o smishing em [notas curtas](../canais.md#smishing).

O escopo registra se esse meio está permitido. Este texto não traz o texto da mensagem nem o endereço.

## Presença

O vetor de presença é o contato no prédio ou em um local combinado. O papel falso faz parte do pretexto. A classe de personificação no ATT&CK inclui a [T1656](https://attack.mitre.org/techniques/T1656/).

O escopo registra o local, a janela e quem fica fora. Sem esse registro, não entre no local. O limite de prédio e de rede sem fio está em [rede sem fio e acesso físico](../../offensive-security/redes/wireless-e-fisico.md).

## Isca

Isca é um objeto ou um arquivo oferecido como útil, perdido ou grátis. A definição de defesa está em [Isca](../canais.md#isca-baiting).

O escopo registra se o objeto está permitido. Este texto não descreve o objeto. Este texto não descreve o arquivo.

## Áudio ou vídeo sintético

O vetor sintético imita a voz ou a imagem de uma pessoa. A ponte ofensiva cita a classe em [engenharia social](../../offensive-security/humano/engenharia-social.md). Semelhança com a pessoa não confirma identidade. A defesa de voz está em [Vishing](../canais.md#vishing).

O padrão deste guia é deixar áudio e vídeo sintéticos fora do escopo. O contrato registra a exclusão. Este texto não descreve como produzir o áudio nem o vídeo.

## Conta já confiável

Uma caixa legítima comprometida muda o remetente. O pedido ainda pode ser falso. A defesa chama esse caso de phishing interno. A classe no ATT&CK inclui a [T1534](https://attack.mitre.org/techniques/T1534/).

Não comprometa uma caixa real para estudar essa classe. A contenção da conta está no [playbook](../playbooks.md#conter-uma-conta).

## Meios que a defesa já nomeia

Estes meios seguem a mesma regra. O escopo os nomeia, ou eles ficam fora. A descrição para quem recebe está na defesa.

| Meio | Onde a defesa descreve o que a pessoa vê |
|------|------------------------------------------|
| Código QR | [Código QR](../canais.md#código-qr) |
| Mídia removível | [Isca](../canais.md#isca-baiting) |
| Pedido de pagamento | [BEC](../canais.md#fraude-de-e-mail-corporativo-bec) |

## O que o escopo responde para qualquer vetor

Registre a mesma lista para cada vetor permitido:

1. O meio.
2. O grupo de pessoas.
3. A janela.
4. A ação proibida.
5. O canal de interrupção.

Não registre modelo de mensagem, página, script nem configuração de envio neste repositório.

## Leitura seguinte

- [Ética e limite do reporte](etica-e-reporte.md)
- [Canais (defesa)](../canais.md)
- [Sinais de alerta](../sinais-de-alerta.md)
