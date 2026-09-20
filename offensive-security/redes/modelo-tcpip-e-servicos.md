# TCP/IP e serviços — o que um scan significa

Antes de qualquer ferramenta de porta, precisa ficar sólido: **endereço, porta, estado, protocolo de aplicação**. Caso contrário você interpreta “open” como “invadi”.

## Modelo em quatro camadas úteis

1. **Link** — Ethernet/Wi-Fi; ARP na LAN. Ofensiva física/wireless vive aqui; na internet você quase não escolhe o link.
2. **Rede (IP)** — roteamento, ICMP, fragmentação. “Pingar” não prova que não há host (ICMP filtrado).
3. **Transporte** — TCP (conexão, handshake) vs UDP (datagrama, mais ambíguo de “aberto”).
4. **Aplicação** — HTTP, SSH, DNS… o *payload* que o serviço entende.

Estude: três vias do TCP, RST vs timeout vs filtered, diferença entre host down e policy drop.

Livros clássicos de redes (Tanenbaum, Kurose, ou o *TCP/IP Illustrated* em espírito) valem mais no longo prazo que tutorial de scanner.

## Porta e serviço

- Porta é um **número** no transporte. “22” não é “SSH seguro”; é “alguém escutou 22/tcp”.
- Banner e fingerprint *sugerem* produto; mentem (honeypot, CDN, port reuse).
- UDP: DNS, SNMP, IKE — “open|filtered” é normal; não conclua demais.

## O que estudar em enumeração (conceito)

- Inventário: o que *deveria* estar exposto vs o que está.
- Versão: para **gestão de patch**, não para caçar exploit neste guia.
- Segmentação: host na DMZ que fala SMB com AD interno é achado de *arquitetura*.

## Ruído e ética

Varredura ampla é visível, pode degradar equipamento frágil (IoT, ICS) e é o primeiro item que ROE restringe. Em lab, observe o que o *seu* IDS vê — purple começa aqui.

## IPv6 e nomes

Inventário só IPv4 perde hosts. DNS e dual-stack fazem parte do mapa de superfície.

## Leitura seguinte

- [Protocolos comuns](protocolos-comuns.md)
- [Recon ativo](../reconhecimento/passivo-vs-ativo.md)
