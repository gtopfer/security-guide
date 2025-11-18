# Standard Operating Environment (SOE)

| Item | Versão | Observações |
|------|--------|------------|
| Sistema Operacional | Ubuntu LTS / Windows Server 2022 | Imagens hardenizadas com CIS Benchmarks. |
| Ferramentas essenciais | Sysmon, osquery, Zeek, Wazuh agent | Instalados via automação. |
| Linguagens suportadas | Python 3.11, PowerShell 7, Go 1.21 | Manter virtualenv/pyenv padronizados. |
| Artefatos obrigatórios | `~/scripts`, `~/playbooks`, `/var/log/blue-team` | Estrutura versionada. |
| Segurança | MFA obrigatório, secrets em Vault, sem admins permanentes | Seguir política de PAM. |
