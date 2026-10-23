# Superfície Linux (estudo)

Linux em pentest aparece como servidor, container, WSL, appliance e CI runner. O objetivo de estudo é **entender o modelo de usuário, processo e pacote** — não uma lista de “kernel exploits”.

## Modelo de usuário

- UID 0 é root. O resto é contrato (sudo, grupos, polkit).
- `/etc/passwd` vs `/etc/shadow`: um é mapa, o outro é segredo (permissão).
- Serviço com usuário dedicado vs tudo como root: impacto de um RCE na app muda completamente.

## Sistema de arquivos e permissões

- bits rwx, diretórios, sticky bit em `/tmp`.
- SUID/SGID: *ideia* — binário que corre com dono elevado. Inventário e patch; binários custom SUID são red flag de admin.
- Capabilities (libcap): recorte mais fino que SUID; mesmo tema de “mais poder que o usuário”.
- Mounts: NFS/CIFS com root squash ou sem; containers com volume da máquina.

## Processos e serviços

- systemd units, timers, cron, at.
- Portas escutando em `0.0.0.0` vs localhost (Redis só em 127.0.0.1 é um desenho).
- Containers: escape é classe avançada — estude *isolamento* (namespaces, cgroups, seccomp) antes de “breakout”.

## Pacotes e supply chain

- Distro velha sem update = superfície CVE.
- Pip/npm global como root.
- Imagens Docker `latest` sem pin.

## Logs e artefatos (para purple)

auth.log/journal, sudo logs, auditd, bash history (frágil). Ver [detecção](../defesa/deteccao-e-logs.md).

## O que estudar, com segurança

- Como um processo herda UID/GID.
- Como o sudoers *deveria* ser mínimo.
- Hardening: sshd_config, unattended-upgrades, firewall (nftables/ufw) em conceito.
- Labs: máquina Linux propositalmente vulnerável **oficial** (ex.: imagens de treino, não servidor aleatório).

Este guia não documenta enumeração ofensiva passo a passo nem exploits de kernel/sudo.

## Git para aprofundar

[PEASS-ng](https://github.com/peass-ng/PEASS-ng) (LinPEAS), [pspy](https://github.com/DominicBreuker/pspy), [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io), [lynis](https://github.com/CISOfy/lynis), [osquery](https://github.com/osquery/osquery). Wiki: HackTricks Linux. Tabela: [coleção pentest — Linux](../../pentest-tools-collection/README.md#linux-enum-e-referência-de-binários).

## Leitura seguinte

- [Privilégios](privilegios-o-que-estudar.md)
- [Windows](windows-superficie.md)
