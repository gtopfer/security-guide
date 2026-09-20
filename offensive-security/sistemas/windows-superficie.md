# Superfície Windows (estudo)

Windows em empresa quase sempre vem **junto de identidade** (AD). Isolar “a caixa” sem o domínio perde o desenho real. Ainda assim, o SO tem um modelo próprio.

## Contas e privilégios

- Usuário padrão vs Administrators vs SYSTEM.
- UAC: *não* é sandbox perfeita; é atrito e consentimento. Entenda o que ele tenta evitar (elevação casual).
- Tokens de acesso: o processo carrega SIDs e privilégios. Impersonation existe como *modelo* de API — estude o vocabulário (primary vs impersonation) em docs Microsoft, sem receitas.

## Autenticação local

- SAM, LSA. Senhas não ficam “em texto” no desenho moderno; hashes e DPAPI são temas de *forense e defesa* tanto quanto de ofensiva.
- Credential Guard / isolamento de LSA: mitigações que o blue deve conhecer pelo nome.

## Serviços e persistência (classe)

Serviços Windows, tarefas agendadas, Run keys, WMI subscriptions: a ATT&CK lista táticas de persistência. Para estudo ofensivo ético: saiba **o que um IR procura** e como um admin endurece GPO. Não monte backdoor.

## SMB, WinRM, RDP

Admin remoto. Superfície: quem pode logar de onde, NLA, restrição de rede. Ver [protocolos](../redes/protocolos-comuns.md).

## Patch e GPO

A maior “técnica” em Windows corporativo ainda é **sistema desatualizado + usuário local admin**. Estude WSUS/Intune como controle.

## Documentação boa (oficial)

- Microsoft Learn: identidade, Kerberos overview, Windows security.
- ATT&CK matriz Windows: <https://attack.mitre.org/matrices/enterprise/windows/>

## Labs

VMs Windows **suas** ou labs de plataforma (HTB/THM) com ToS. Não ative servidor pirata nem ataque o AD da empresa.

## Leitura seguinte

- [Active Directory](../identidade/active-directory-conceitos.md)
- [Privilégios](privilegios-o-que-estudar.md)
