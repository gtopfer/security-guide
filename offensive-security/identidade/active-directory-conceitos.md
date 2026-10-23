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

## Kerberos no fluxo feliz (o que memorizar)

1. Cliente pede TGT ao **KDC** (AS-REQ / AS-REP). Pré-auth (timestamp cifrado com a chave do usuário) existe para dificultar certas classes de ataque offline — política importa.
2. Com o TGT, pede **TGS** para um SPN (HTTP/sql/cifs/…).
3. Apresenta o ticket ao serviço. O serviço confia no KDC, não “conhece a senha do usuário”.

Consequências de estudo (sem receita):

- Relógio (skew) quebra Kerberos.
- SPN em conta de usuário com senha fraca é classe de risco (Kerberoasting *como nome de problema*, não como tutorial).
- Delegação larga = um serviço comprometido finge ser o usuário em muitos outros.
- NTLM fallback em rede plana = outra classe (relay), mitigada com signing, EPA, desligar NTLM onde der.

## ACL: o grafo que o BloodHound desenha

No AD, permissão não é só “é admin”. Objetos têm DACL: *GenericAll*, *WriteDacl*, *ForceChangePassword*, *AddMember*, *DCSync* (replicação)… são **direitos**. O grafo pergunta: a partir da conta de lab, que cadeia de direitos chega num grupo privilegiado?

Estude: herança, AdminSDHolder, protected groups. Lab: GOAD. Ferramenta: BloodHound CE.

## AD CS (certificados)

AD Certificate Services emite certificados. Templates mal definidos (enrollee supply SAN, auth EKUs) são a pesquisa “ESC1…” — leia os whitepapers de SpecterOps / posts de ly4k **como ameaça e mitigação**. Ferramenta de lab: Certipy. Não é o primeiro tópico; é o que diferencia estudo raso de profundo em 2024+.

## Entra ID / Azure AD

Não é o mesmo AD. Tokens Graph, app registrations, CA policies, sync (Entra Connect). Git: ROADtools, GraphRunner, Stormspotter — só tenant **seu**.

## Git para aprofundar (lab)

Ver tabela longa em [Windows, AD e movimento interno](../../pentest-tools-collection/README.md#windows-ad-e-movimento-interno) e o [mapa](../biblioteca/mapa-ferramentas.md).

Mínimo: GOAD + Impacket docs + BloodHound + InternalAllTheThings + Microsoft Kerberos overview.

## O que estudar

1. Docs Microsoft: Kerberos explained, AD DS fundamentals, Authentication mechanisms.
2. ATT&CK: Credential Access, Lateral Movement — **mitigações**.
3. Lab: AD **seu**. Nunca o domínio de produção “porque sou estagiário”.

## Leitura seguinte

- [Credenciais](autenticacao-e-credenciais.md)
- [Windows](../sistemas/windows-superficie.md)
