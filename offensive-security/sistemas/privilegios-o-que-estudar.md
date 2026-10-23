# Privilégios: o que estudar (sem receita de escalada)

*Privilege escalation* é o nome da classe: processo ou usuário com pouco poder passa a ter mais. Em relatório, o impacto é “o que o atacante *já na caixa* consegue no modelo de ameaça”. Este documento cobre **por que existe** e **o que ler**. Não cobre como fazer.

## Por que existe

Sistemas reais misturam:

- Software que precisa de poder (agente, driver, updater)
- Configuração humana (sudo demais, pasta gravável em path de serviço)
- Bugs (validação, race, kernel)

A defesa é least privilege + patch + telemetria, não “esconder o kernel”.

## Eixos de estudo (conceituais)

1. **Identidade errada** — serviço como SYSTEM/root porque “assim funciona”.
2. **Controle de acesso quebrado** — arquivo, share, API local, named pipe, socket Unix.
3. **Trust boundary** — container → host, VM → hypervisor, userland → kernel, app → plugin.
4. **Atualização** — updater que aceita pacote não assinado (integridade).
5. **Credencial ao alcance** — config, variável de ambiente, histórico; isso é *higiene*, não magia.

## Linux vs Windows vs macOS vs cloud

O *nome* muda (sudoers, token, TCC, IAM `iam:PassRole`). O padrão é o mesmo: **quem pode influenciar um componente mais poderoso?**

Cloud: “escalar” muitas vezes é **permissão IAM excessiva**, não kernel. Ver [cloud](../nuvem/cloud-superficie.md).

## Como estudar sem virar “lista de exploits”

- Leia o modelo de permissão oficial (man sudoers, Microsoft docs on privileges, AWS IAM evaluation).
- No lab, use contas **não-admin de propósito** e veja o que o SO *recusa*. A recusa ensina o modelo.
- Mapeie achados para CWE (ex.: 250 Execution with Unnecessary Privileges, 269 Improper Privilege Management).
- Purple: quais eventos (4624/4672 no Windows, sudo no Linux) deveriam existir se alguém elevasse.

## Relatório

“Há caminhos de escalada conhecidos nesta versão” é fraco. Melhor: **precondição** (já é usuário local), **impacto** (domínio, dado, persistência), **correção** (tirar admin local, patch, service hardening). Sem anexar exploit.

## Leitura seguinte

- [Linux](linux-superficie.md)
- [Windows](windows-superficie.md)
- [ATT&CK Privilege Escalation](https://attack.mitre.org/tactics/TA0004/) — leia descrições e mitigações
