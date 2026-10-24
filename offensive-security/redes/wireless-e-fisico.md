# Rede sem fio e acesso físico

Um red team completo às vezes inclui o prédio. A maior parte dos leitores deste guia **não** tem esse escopo. Não improvise.

## Rede sem fio

O Wi-Fi é uma rede cuja fronteira é o rádio. Classes de risco: senha fraca, WPS legado, rede de visitante mal isolada e ponto de acesso falso (a pessoa se conecta a um SSID com o mesmo nome). Estude o modelo (associação, 802.1X corporativo e PSK) em material de administração de rede.

Atacar o Wi-Fi do vizinho, de uma cafeteria "para treinar" ou de uma empresa sem regras de engajamento escritas é ilegal. Laboratório: o seu ponto de acesso, ou um exercício de curso com equipamento próprio.

## Acesso físico

Crachá, recepção, USB deixado de propósito, impressora e sala de servidor aberta. Em exercício profissional: atores combinados, seguro e debrief. Fora disso, não execute.

## Cabo e data center

Console, iLO ou iDRAC na VLAN de usuários, e rack sem controle de acesso. Isto é inventário. A ética é a mesma.

## Defesa que o estudo ofensivo deve recomendar

Segmente a rede de visitante. Use 802.1X. Use NAC quando a maturidade permitir. Desative o boot por USB via GPO. Adote mesa limpa. Use filtro de privacidade em escritório aberto se o modelo de ameaça incluir observação por cima do ombro.

## Leitura seguinte

- [Ética](../fundamentos/etica-e-lei.md)
- [Engenharia social](../humano/engenharia-social.md)
