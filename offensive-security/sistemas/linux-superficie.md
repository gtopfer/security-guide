# Superfície Linux (estudo)

No pentest, o Linux aparece como servidor, contêiner, WSL, appliance e runner de CI. O objetivo de estudo é **entender o modelo de usuário, de processo e de pacote**. Não é uma lista de exploit de kernel.

## Modelo de usuário

- O UID 0 é root. O restante é contrato: sudo, grupo e polkit.
- `/etc/passwd` é o mapa. `/etc/shadow` é o segredo. A permissão separa os dois.
- Um serviço com usuário dedicado muda o impacto de uma execução remota na aplicação. Tudo como root muda esse impacto por completo.

## Sistema de arquivos e permissões

- Bits rwx, diretório e sticky bit em `/tmp`.
- SUID e SGID: o binário executa com o dono elevado. Faça inventário e aplique correção. Binário próprio com SUID é um sinal de administração arriscada.
- Capabilities (libcap): recorte mais fino que o SUID. O tema é o mesmo: mais poder do que o usuário deveria ter.
- Montagem: NFS ou CIFS com ou sem root squash, e contêiner com volume da máquina.

## Processos e serviços

- Unidades systemd, timer, cron e at.
- Porta escutando em `0.0.0.0` ou em localhost. Redis somente em `127.0.0.1` é uma decisão de desenho.
- Contêiner: escape é classe avançada. Estude o isolamento (namespace, cgroup, seccomp) antes de qualquer breakout.

## Pacotes e supply chain

- Distribuição antiga, sem atualização, é superfície de CVE.
- `pip` ou `npm` global como root aumenta o impacto.
- Imagem Docker com tag `latest`, sem versão fixa, impede repetir o build.

## Logs e artefatos (purple team)

`auth.log` ou journal, log de sudo, auditd e histórico do bash (frágil). Veja [detecção](../defesa/deteccao-e-logs.md).

## O que estudar, com segurança

- Como um processo herda UID e GID.
- Como o sudoers deve ser mínimo.
- Hardening em conceito: `sshd_config`, atualização automática e firewall (nftables ou ufw).
- Laboratório: máquina Linux vulnerável de propósito, de fonte oficial. Não um servidor aleatório.

Este guia não documenta enumeração ofensiva passo a passo nem exploit de kernel ou de sudo.

## Repositórios para aprofundar

[PEASS-ng](https://github.com/peass-ng/PEASS-ng) (LinPEAS), [pspy](https://github.com/DominicBreuker/pspy), [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io), [lynis](https://github.com/CISOfy/lynis), [osquery](https://github.com/osquery/osquery). Wiki: HackTricks Linux. Tabela: [coleção de pentest — Linux](../../pentest-tools-collection/README.md#linux-enum-e-referência-de-binários).

## Leitura seguinte

- [Privilégios](privilegios-o-que-estudar.md)
- [Windows](windows-superficie.md)
