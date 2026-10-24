# TCP/IP e serviços: o que um scan indica

Antes de qualquer ferramenta de porta, fixe quatro ideias: **endereço, porta, estado e protocolo de aplicação**. Sem isso, "open" é lido como "invadido".

## Quatro camadas úteis

1. **Enlace** — Ethernet e Wi-Fi; ARP na LAN. A ofensiva física e sem fio vive aqui. Na internet, você quase não escolhe o enlace.
2. **Rede (IP)** — roteamento, ICMP e fragmentação. Um ping não prova que o host está ausente. O ICMP pode estar filtrado.
3. **Transporte** — TCP (conexão e handshake) e UDP (datagrama; o estado "aberto" é mais ambíguo).
4. **Aplicação** — HTTP, SSH, DNS. É o conteúdo que o serviço entende.

Estude o handshake de três vias do TCP, a diferença entre RST, timeout e filtered, e a diferença entre host desligado e descarte por política.

Um livro clássico de redes (Tanenbaum, Kurose, ou o espírito de *TCP/IP Illustrated*) dura mais do que um tutorial de scanner.

## Porta e serviço

- A porta é um **número** no transporte. "22" não significa "SSH seguro". Significa que alguém escuta em 22/tcp.
- Banner e fingerprint sugerem o produto. Eles podem estar errados (honeypot, CDN, reuso de porta).
- UDP: DNS, SNMP e IKE. O estado "open|filtered" é normal. Não conclua além da evidência.

## O que estudar na enumeração

- Inventário: o que deveria estar exposto e o que está.
- Versão: para **gestão de correção**, não para procurar exploit neste guia.
- Segmentação: um host na DMZ que fala SMB com o AD interno é um achado de arquitetura.

## Ruído e ética

A varredura ampla é visível. Ela pode degradar equipamento frágil (IoT, sistema industrial). É o primeiro item que as regras de engajamento restringem. No laboratório, observe o que o seu IDS vê. O purple team começa aqui.

## IPv6 e nomes

Um inventário só IPv4 perde host. DNS e dual-stack fazem parte do mapa de superfície.

## Leitura seguinte

- [Protocolos comuns](protocolos-comuns.md)
- [Reconhecimento ativo](../reconhecimento/passivo-vs-ativo.md)
