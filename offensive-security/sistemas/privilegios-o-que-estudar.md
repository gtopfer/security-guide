# Privilégios: o que estudar (sem receita de escalada)

*Privilege escalation* é o nome da classe: um processo ou um usuário com pouco poder passa a ter mais. No relatório, o impacto é o que o atacante, **já na máquina**, consegue no modelo de ameaça. Este documento cobre **por que a classe existe** e **o que ler**. Não cobre como executar.

## Por que existe

Sistemas reais misturam:

- Software que precisa de poder (agente, driver, atualizador)
- Configuração humana (sudo amplo, pasta gravável no caminho de um serviço)
- Defeito (validação, condição de corrida, kernel)

A defesa é privilégio mínimo, correção e telemetria. Não é ocultar o kernel.

## Eixos de estudo

1. **Identidade errada** — o serviço executa como SYSTEM ou root porque "assim funciona".
2. **Controle de acesso quebrado** — arquivo, share, API local, named pipe e socket Unix.
3. **Fronteira de confiança** — contêiner para host, máquina virtual para hypervisor, userland para kernel, aplicativo para plugin.
4. **Atualização** — atualizador que aceita pacote sem assinatura (integridade).
5. **Credencial ao alcance** — arquivo de configuração, variável de ambiente e histórico. Isto é higiene, não um mecanismo oculto.

## Linux, Windows, macOS e nuvem

O nome muda: sudoers, token, TCC, permissão IAM `iam:PassRole`. O padrão é o mesmo: **quem pode influenciar um componente mais poderoso**.

Na nuvem, "escalar" muitas vezes é **permissão IAM excessiva**, não kernel. Veja [nuvem](../nuvem/cloud-superficie.md).

## Como estudar sem virar uma lista de exploit

- Leia o modelo oficial de permissão (`man sudoers`, documentação Microsoft de privilégios, avaliação de IAM na AWS).
- No laboratório, use conta **sem privilégio de administrador** e observe o que o sistema recusa. A recusa ensina o modelo.
- Mapeie o achado para CWE (por exemplo, 250 Execution with Unnecessary Privileges e 269 Improper Privilege Management).
- Purple team: quais eventos deveriam existir se alguém elevasse o privilégio (4624 e 4672 no Windows, sudo no Linux).

## Relatório

"Há caminhos de escalada conhecidos nesta versão" é uma frase fraca. Prefira: **pré-condição** (já é usuário local), **impacto** (domínio, dado, persistência) e **correção** (remover administrador local, aplicar correção, endurecer o serviço). Não anexe exploit.

## Leitura seguinte

- [Linux](linux-superficie.md)
- [Windows](windows-superficie.md)
- [ATT&CK Privilege Escalation](https://attack.mitre.org/tactics/TA0004/) — leia a descrição e a mitigação
