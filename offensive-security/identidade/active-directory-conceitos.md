# Active Directory — conceitos para ofensiva e defesa

AD é o **sistema de identidade** da maior parte das empresas Windows: quem é quem, o que pode, qual máquina é de confiança. Comprometer o *modelo* (contas, grupos, GPOs, trusts) costuma valer mais que uma CVE isolada num IIS.

Este texto é vocabulário e desenho. Não é guia de ataque a domínio.

## Peças

- **Domínio / floresta / trust** — fronteiras de identidade. Trust demais = superfície.
- **DC (Domain Controller)** — a fonte da verdade; LDAP + Kerberos + DNS muitas vezes juntos.
- **Objetos** — usuários, computadores, grupos, OUs.
- **SID** — identificador; o nome pode mudar, o SID não.
- **GPO** — política empurrada; misconfig vira persistência *legítima*.
- **Kerberos** — tickets (TGT, TGS), tempo, SPN. Estude o *fluxo feliz* na documentação Microsoft antes de qualquer ferramenta.
- **NTLM** — legado; ainda aparece; é um ímã de relay *como classe de risco de protocolo* em redes planas.

## Grupos que o analista deve saber o *significado*

Domain Admins, Enterprise Admins, Schema Admins, Account Operators, Backup Operators, Server Operators, Print Operators (histórico de privilégio), Domain Computers, Domain Users.

Não memorize SID; entenda **por que Backup Operators é poderoso** (acesso a dado).

## Autenticação na prática (ideia)

Estação junta ao domínio, usuário loga, recebe TGT, pede ticket para serviço (CIFS, HTTP, LDAP). Delegação (unconstrained/constrained/resource-based) é *confiança entre serviços* — tema avançado para ler em Learn.microsoft.com, não para reproduzir aqui.

## Superfície típica (o que inventariar em pentest *autorizado*)

- Quantos DCs, se há DC na internet (não deveria).
- Política de senha e MFA na *borda* vs no domínio.
- Contas de serviço com senha em GPO/script antigo (classe: secret sprawl).
- ACL em objetos (quem pode resetar senha de quem) — isso é o coração de muita pesquisa de AD; use lab.

## BloodHound e similares (como pensar)

Ferramentas de **grafo** mostram caminhos de permissão. Em engajamento autorizado, servem para evidenciar “este helpdesk consegue chegar naquele grupo”. Fora de escopo, são arma. A coleção de pentest não substitui contrato.

## O que estudar

1. Curso/docs Microsoft: Kerberos explained, AD DS fundamentals.
2. ATT&CK: Credential Access, Lateral Movement — **mitigações**.
3. Lab: AD **seu** (VMs) ou labs de plataforma. Nunca o domínio de produção “porque sou estagiário”.

## Leitura seguinte

- [Credenciais](autenticacao-e-credenciais.md)
- [Windows](../sistemas/windows-superficie.md)
