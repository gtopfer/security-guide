# Ferramentas essenciais para Threat Intelligence em Linux

## Ambiente base

1. **Sistema:** Ubuntu 22.04 LTS ou distro equivalente com kernel atualizado e suporte a containers.
2. **Python:** versão 3.10+ com `pyenv` ou `asdf` para gerenciar múltiplos runtimes.
3. **Containers:** Docker/Podman + Compose para subir stacks de feeds locais ou instâncias OpenCTI.

## Pacotes obrigatórios

| Categoria | Pacotes/Projetos | Observações |
|-----------|------------------|-------------|
| STIX/TAXII | `cti-toolkit`, `stix2`, `cabby` | Conversão e publicação de coleções STIX 2.1. |
| Enriquecimento | `ioc-fanger`, `urlscan`, `ipwhois`, `shodan` | Scripts CLI rápidos para contexto adicional. |
| Data wrangling | `pandas`, `duckdb`, `jq`, `miller` | Tratamento de grandes volumes de IOCs. |
| Visualização | `kibana`, `grafana`, `maltiverse`, `maltego` | Exploração gráfica de indicadores e relacionamentos. |
| Automação | `poetry`, `make`, `pre-commit`, `invoke` | Padroniza execução e empacotamento. |

## Boas práticas de hardening

- Use usuários dedicados para serviços (OpenCTI, MISP, redis) e isole secrets em Vault ou Pass.
- Configure `ufw`/`nftables` minimizando portas expostas dos feeds internos.
- Habilite registro detalhado (`auditd`, `journald`) para rastrear acesso a dados sensíveis.
- Utilize `pipx` para instalar CLIs de terceiros e evitar poluir ambientes do projeto.

## Dicas operacionais

- Automatize atualizações de taxonomias (ex.: MITRE, CAPEC) via `cron` ou GitHub Actions.
- Para notebooks colaborativos, utilize VS Code Remote ou JupyterLab com autenticação SSO.
- Registre sempre a origem e o contrato associado ao feed para facilitar auditoria e renovação.
