# Superfície em nuvem (AWS, Azure e GCP)

Nuvem não é "um servidor no data center de outra empresa". É uma **API de controle** (IAM) mais **planos de dados** (armazenamento, computação, banco). A ofensiva atual, com frequência, é uma lacuna de permissão, não uma execução remota de código.

## Modelo compartilhado

O provedor protege o hypervisor e a API global. Você protege **conta, identidade, configuração e dado**. A configuração sua (bucket público, security group `0.0.0.0/0`, chave de acesso no Git) é o caminho típico de vazamento.

## IAM como o diretório da nuvem

- Identidade humana e identidade de workload (função, service principal, função anexada à máquina virtual).
- Política: permitir e negar, herança, e aumento de privilégio por permissão que passa função ou cria chave.
- Federação: o SSO corporativo entra na nuvem. Um provedor de identidade frágil alcança todas as contas.

Estude a **documentação de avaliação de política** do provedor que você usa. Um provedor em profundidade vale mais do que três em superfície.

## Armazenamento

Objeto (S3, Blob, GCS): ACL pública, política do bucket, versionamento e log de acesso. Dork e Certificate Transparency às vezes revelam o nome. **Acessar dado de terceiro não é OSINT inofensivo.**

## Metadado de instância (IMDS)

A máquina virtual pergunta "quem sou eu" e "qual é a minha função" a um endereço link-local. SSRF, ou malware na máquina que alcança o IMDS, obtém **credencial de nuvem**. Defesa: IMDSv2 (limite de salto), firewall de metadado e privilégio mínimo na função.

## Rede

VPC ou VNet, peering, endpoint privado, security group e NACL. Superfície: banco com IP público e API do Kubernetes na porta 443 da internet.

## Log ofensivo e defensivo

CloudTrail, Activity Log e Cloud Audit Logs são o registro do plano de controle. O purple team em nuvem começa pela pergunta: este AssumeRole apareceria?

## O que estudar

- CIS Benchmarks do provedor (leitura de controle).
- OWASP e CSA para a visão de nuvem.
- Laboratório oficial: conta **sua**, com alarme de cobrança. Não use a conta do empregador sem mandato.

## Repositórios para aprofundar

Wiki: [HackTricks Cloud](https://github.com/HackTricks-wiki/hacktricks-cloud). Auditoria: [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite). Laboratório AWS: [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat). Enumeração com credencial de laboratório: [CloudFox](https://github.com/BishopFox/cloudfox), [Pacu](https://github.com/RhinoSecurityLabs/pacu). Grafo de IAM: [PMapper](https://github.com/nccgroup/PMapper). Entra: [ROADtools](https://github.com/dirkjanm/ROADtools). Purple team na conta: [Stratus](https://github.com/DataDog/stratus-red-team).

Tabela completa: [coleção de pentest — nuvem](../../pentest-tools-collection/README.md#nuvem).

## Leitura seguinte

- [CI/CD](cicd-e-supply-chain.md)
- [SSRF no Top 10](../web/owasp-top-10.md)
