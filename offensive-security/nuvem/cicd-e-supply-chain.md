# CI/CD e supply chain

Se o pipeline publica produção, **comprometer o pipeline é comprometer o produto**. Os casos SolarWinds, actions maliciosas e dependências em npm e PyPI mostraram esse caminho ao mercado.

## Cadeia

Código, revisão, build, artefato, deploy e tempo de execução.

A pergunta do estudo ofensivo, em cada seta, é: **quem pode inserir bits** e **quem verifica a integridade**.

## Superfícies comuns (classes)

- Segredo no repositório ou em variável de CI registrada em texto claro.
- Runner self-hosted com privilégio excessivo (acesso à rede interna ou a chave de nuvem).
- Proteção de branch fraca e opção de ignorar as verificações.
- Dependência com nome parecido (typosquat) e lockfile sem revisão.
- GitHub Action de terceiro com `pull_request_target` mal entendido. A própria GitHub documenta essa classe de risco.
- Registry de imagem sem assinatura. Cosign e Sigstore são a ideia de controle.
- Dependabot ou Renovate desligados, e imagem base antiga.

## SBOM e CVE

A lista de componentes não é ofensiva. É o mapa. A pergunta ética em AppSec é: esta biblioteca tem CVE explorável neste contexto? Em muitos casos, não, porque o código não é alcançável.

## O que estudar

- Framework SLSA (nível de integridade de build): <https://slsa.dev/>
- Visão geral do Sigstore
- NIST SSDF, como referência de processo
- ATT&CK: Supply Chain Compromise

Prática: leia o YAML de um pipeline **seu**. Marque onde um pull request malicioso, vindo de um fork, ganharia poder. Corrija. Isso é estudo ofensivo responsável.

## Leitura seguinte

- [Integridade no Top 10](../web/owasp-top-10.md)
- [Relatório](../defesa/relatorio-e-comunicacao.md)
