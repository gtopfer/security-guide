# Superfície Windows (estudo)

Em empresa, o Windows quase sempre vem **junto da identidade** (AD). Isolar a máquina sem o domínio perde o desenho real. Ainda assim, o sistema tem um modelo próprio.

## Contas e privilégios

- Usuário padrão, grupo Administrators e SYSTEM.
- O UAC não é um sandbox completo. É atrito e consentimento. Entenda o que ele tenta evitar: elevação casual.
- O token de acesso carrega SID e privilégio no processo. A personificação existe como modelo de API. Estude o vocabulário (primary e impersonation) na documentação da Microsoft, sem receita.

## Autenticação local

- SAM e LSA. No desenho moderno, a senha não fica em texto claro. Hash e DPAPI são temas de forense e de defesa, tanto quanto de ofensiva.
- Credential Guard e isolamento da LSA: mitigações que a defesa deve conhecer pelo nome.

## Serviços e persistência (classe)

Serviço do Windows, tarefa agendada, chave Run e assinatura WMI: o ATT&CK lista táticas de persistência. Para estudo ofensivo ético, saiba **o que a resposta a incidente procura** e como um administrador endurece a GPO. Não monte backdoor.

## SMB, WinRM e RDP

Administração remota. Superfície: quem pode entrar, de onde, com NLA e com restrição de rede. Veja [protocolos](../redes/protocolos-comuns.md).

## Correção e GPO

A condição mais comum em Windows corporativo ainda é **sistema desatualizado com usuário local administrador**. Estude WSUS e Intune como controle.

## Documentação oficial

- Microsoft Learn: identidade, visão geral de Kerberos e segurança do Windows.
- Matriz ATT&CK para Windows: <https://attack.mitre.org/matrices/enterprise/windows/>

## Laboratórios

Use máquina virtual Windows **sua** ou laboratório de plataforma (Hack The Box, TryHackMe) dentro do termo de uso. Não ative servidor irregular e não ataque o AD da empresa.

## Repositórios para aprofundar

[x64dbg](https://github.com/x64dbg/x64dbg), [Seatbelt](https://github.com/GhostPack/Seatbelt), [WinPEAS](https://github.com/peass-ng/PEASS-ng), [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS), [WES-NG](https://github.com/bitsadmin/wesng). AD: [conceitos de AD](../identidade/active-directory-conceitos.md). Catálogo: [Windows e AD na coleção](../../pentest-tools-collection/README.md#windows-ad-e-movimento-interno).

## Leitura seguinte

- [Active Directory](../identidade/active-directory-conceitos.md)
- [Privilégios](privilegios-o-que-estudar.md)
