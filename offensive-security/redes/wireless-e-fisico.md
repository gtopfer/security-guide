# Wireless e físico (visão de risco)

Red team completo às vezes inclui o prédio. A maior parte dos leitores deste guia **não** tem esse escopo — e não deve improvisar.

## Wireless

Wi-Fi é rede com fronteira radio. Classes de risco: senha fraca, WPS legado, guest mal isolado, rogue AP (usuário liga no SSID homônimo). Estude o **modelo** (associação, 802.1X corporativo vs PSK) em material de administração de rede.

Ataque a Wi-Fi de vizinho, cafeteria “para treinar” ou empresa sem ROE escrito é ilegal. Labs: seu AP, ou exercícios de curso com kit próprio.

## Físico

Crachá, recepção, USB “perdido”, impressora, sala de servidor aberta, lockpicking de filme. Em exercício profissional: atores combinados, seguro, e debrief. Fora disso: não.

## Cabo e “físico de data center”

Console, iLO/iDRAC na VLAN de usuários, rack sem câmara. Inventário. Mesma ética.

## Defesa que o ofensivo deve recomendar

Segmentar guest, 802.1X, NAC se o madurez permitir, USB boot desligado por GPO, mesa limpa, *privacy screen* em open office se o threat model incluir ombro.

## Leitura seguinte

- [Ética](../fundamentos/etica-e-lei.md)
- [Engenharia social](../humano/engenharia-social.md)
