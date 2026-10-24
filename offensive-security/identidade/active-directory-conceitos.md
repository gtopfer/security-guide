# Active Directory: conceitos para ofensiva e defesa

O AD é o **sistema de identidade** da maior parte das empresas Windows. Ele define quem é quem, o que a conta pode fazer e qual máquina é confiável. Comprometer o modelo (conta, grupo, GPO, relação de confiança) costuma ter mais impacto do que uma CVE isolada em um IIS.

Este texto é vocabulário e desenho. Não é um guia de ataque a domínio.

## Peças

- **Domínio, floresta e trust** — fronteira de identidade. Trust em excesso aumenta a superfície.
- **DC (controlador de domínio)** — a fonte da verdade. LDAP, Kerberos e DNS costumam estar juntos.
- **Objetos** — usuário, computador, grupo e OU.
- **SID** — identificador. O nome pode mudar. O SID não muda.
- **GPO** — política aplicada aos objetos. Uma configuração incorreta vira persistência que parece legítima.
- **Kerberos** — ticket (TGT e TGS), tempo e SPN. Estude o fluxo esperado na documentação da Microsoft antes de qualquer ferramenta.
- **NTLM** — protocolo legado. Ainda aparece. Em rede plana, é uma classe de risco de relay.

## Grupos cujo significado o analista precisa conhecer

Domain Admins, Enterprise Admins, Schema Admins, Account Operators, Backup Operators, Server Operators, Print Operators (privilégio histórico), Domain Computers e Domain Users.

Não memorize o SID. Entenda **por que Backup Operators é poderoso**: o grupo acessa dado.

## Autenticação na prática (ideia)

A estação ingressa no domínio. O usuário entra. Recebe um TGT. Pede um ticket para o serviço (CIFS, HTTP, LDAP). A delegação (unconstrained, constrained ou baseada em recurso) é confiança entre serviços. É um tema avançado para ler em Learn.microsoft.com, não para reproduzir aqui.

## Superfície típica (o que inventariar em pentest autorizado)

- Quantos controladores existem e se algum está na internet. Não deveria estar.
- Política de senha e MFA na borda, em comparação com o domínio.
- Conta de serviço com senha em GPO ou em script antigo (classe: segredo espalhado).
- ACL em objeto (quem pode redefinir a senha de quem). Esta é a base de muita pesquisa de AD. Use laboratório.

## BloodHound e ferramentas semelhantes

A ferramenta de **grafo** mostra caminho de permissão. Em trabalho autorizado, ela evidencia que o service desk alcança determinado grupo. Fora do escopo, ela é uma arma. A coleção de pentest não substitui o contrato.

## Kerberos no fluxo esperado

1. O cliente pede um TGT ao **KDC** (AS-REQ e AS-REP). A pré-autenticação (carimbo de tempo cifrado com a chave do usuário) dificulta certas classes de ataque offline. A política importa.
2. Com o TGT, o cliente pede um **TGS** para um SPN (HTTP, SQL, CIFS).
3. O cliente apresenta o ticket ao serviço. O serviço confia no KDC. Ele não conhece a senha do usuário.

Consequências de estudo, sem receita:

- Diferença de relógio quebra o Kerberos.
- SPN em conta de usuário com senha fraca é uma classe de risco. Kerberoasting é o nome do problema, não um tutorial.
- Delegação ampla permite que um serviço comprometido aja como o usuário em muitos outros serviços.
- O fallback para NTLM em rede plana é outra classe (relay). Mitigue com assinatura, EPA e desativação do NTLM onde for possível.

## ACL: o grafo que o BloodHound desenha

No AD, permissão não é só "é administrador". O objeto tem DACL. *GenericAll*, *WriteDacl*, *ForceChangePassword*, *AddMember* e *DCSync* (replicação) são **direitos**. O grafo pergunta: a partir da conta de laboratório, qual cadeia de direitos chega a um grupo privilegiado?

Estude herança, AdminSDHolder e grupos protegidos. Laboratório: GOAD. Ferramenta: BloodHound CE.

## AD CS (certificados)

O AD Certificate Services emite certificado. Um template mal definido (o solicitante informa o SAN, ou o EKU de autenticação é amplo) é a pesquisa conhecida pela série "ESC". Leia os whitepapers da SpecterOps e os textos de ly4k como ameaça e como mitigação. Ferramenta de laboratório: Certipy. Não é o primeiro tópico. É o que separa um estudo superficial de um estudo profundo a partir de 2024.

## Entra ID (Azure AD)

Não é o mesmo AD. Há token do Microsoft Graph, registro de aplicativo, política de acesso condicional e sincronização (Entra Connect). Repositórios: ROADtools, GraphRunner e Stormspotter. Use somente no tenant **seu**.

## Repositórios para aprofundar (laboratório)

Veja a tabela em [Windows, AD e movimento interno](../../pentest-tools-collection/README.md#windows-ad-e-movimento-interno) e o [mapa](../biblioteca/mapa-ferramentas.md).

Mínimo: GOAD, documentação do Impacket, BloodHound, InternalAllTheThings e a visão geral de Kerberos da Microsoft.

## O que estudar

1. Documentação Microsoft: *Kerberos explained*, fundamentos de AD DS e mecanismos de autenticação.
2. ATT&CK: Credential Access e Lateral Movement, com foco nas mitigações.
3. Laboratório: um AD **seu**. Nunca o domínio de produção, mesmo com a justificativa de ser estagiário.

## Leitura seguinte

- [Credenciais](autenticacao-e-credenciais.md)
- [Windows](../sistemas/windows-superficie.md)
