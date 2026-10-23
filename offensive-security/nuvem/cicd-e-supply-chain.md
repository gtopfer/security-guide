# CI/CD e supply chain

Se o pipeline publica produção, **comprometer o pipeline é comprometer o produto**. SolarWinds, actions maliciosas e dependências npm/PyPI ensinaram o mercado na marra.

## Cadeia

Código → review → build → artefato → deploy → runtime.

Ofensiva de estudo pergunta: em cada seta, **quem pode inserir bits** e **quem verifica integridade?**

## Superfícies comuns (classes)

- Segredo no repo ou na variável do CI logada em texto.
- Runner self-hosted poderoso demais (acesso à rede interna / cloud keys).
- Branch protection fraca; botão “skip checks”.
- Dependência com typosquat; lockfile não revisto.
- GitHub Action de terceiro com `pull_request_target` mal entendido (classe de risco documentada pela própria GitHub).
- Registry de imagem sem assinatura (cosign/sigstore como *ideia* de controle).
- Dependabot/renovate desligado; imagem base de 2019.

## SBOM e CVE

Lista de componentes não é ofensiva; é o mapa. Ofensiva ética em AppSec: “este lib tem CVE explorável *neste* contexto?” — muitas vezes não (não alcançável).

## O que estudar

- SLSA framework (níveis de integridade de build): <https://slsa.dev/>
- Sigstore overview
- NIST SSDF (em espírito)
- ATT&CK: Supply Chain Compromise

Pratique: leia o YAML de um pipeline **seu** e marque onde um PR malicioso (de fork) ganharia poder. Corrija. Isso é estudo ofensivo responsável.

## Leitura seguinte

- [Integrity no Top 10](../web/owasp-top-10.md)
- [Relatório](../defesa/relatorio-e-comunicacao.md)
