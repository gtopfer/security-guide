# Playbook: Lateral Movement

## Escopo
Avaliar capacidade de detecção/containment para movimentos laterais em ambientes Windows/Hybrid.

## Hipóteses
- Reuso de credenciais locais com PSExec/SMB.
- Abuse de WinRM/WSMan mediante tokens delegados.
- Uso de certificados ADCS para persistência (ESC1).

## Passos
1. Inventariar hosts e contas com privilégios (BloodHound/SharpHound).
2. Explorar caminhos viáveis (Kerberoasting, pass-the-hash, overpass-the-hash).
3. Estabelecer beacons em cada salto mantendo logs detalhados.
4. Limpar indicadores somente após encerrar o exercício.

## Mitigações sugeridas
- Harden de credenciais locais (LSA Protection, LAPS).
- Segmentação de administração (Tiering model).
- Monitoramento de eventos 4624/4625 + WinRM/PS remoting.
