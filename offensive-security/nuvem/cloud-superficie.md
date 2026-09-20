# Superfície em nuvem (AWS, Azure, GCP — ideias comuns)

Nuvem não é “servidor em data center alheio”. É **API de controle** (IAM) + **planos de dados** (storage, compute, DB). A ofensiva moderna muitas vezes é *permission gap*, não RCE.

## Modelo compartilhado

O provedor segura o hypervisor e a API global; você segura **conta, identidade, config, dado**. Misconfig sua (bucket público, security group 0.0.0.0/0, chave de acesso no Git) é a história típica de breach.

## IAM como AD da nuvem

- Identidade humana vs workload (role, service principal, attached role em VM).
- Política: allow/deny, herança, *privilege escalation* via permissões que passam roles ou criam keys.
- Federação: SSO corporativo entra na nuvem; um IdP frágil vira todas as contas.

Estude a **documentação de evaluation de política** do provedor que você usa (um só, fundo, em vez de três superficiais).

## Storage

Objetos (S3, Blob, GCS): ACL pública, política de bucket, versionamento, logs de acesso. Dorks e CT às vezes acham nomes; **acessar dado de terceiro não é OSINT inocente**.

## Metadados de instância (IMDS)

VMs perguntam “quem sou eu / qual role?” a um endereço link-local. SSRF ou malware na VM que alcança IMDS vira **credencial de nuvem**. Defesa: IMDSv2 (hop limit), firewall de metadata, least privilege na role.

## Rede

VPC/VNet, peering, endpoints privados, security groups vs NACLs. Superfície: RDS com IP público, Kubernetes API 443 na internet.

## Logs ofensivos/defensivos

CloudTrail / Activity Log / Cloud Audit: a verdade do control plane. Purple team em nuvem começa por “esse AssumeRole apareceria?”.

## O que estudar

- CIS Benchmarks do provedor (leitura de controle).
- OWASP Cloud / CSA guidance (visão).
- Labs oficiais: accounts **suas** com billing alarme; never a conta do empregador sem mandato.

## Leitura seguinte

- [CI/CD](cicd-e-supply-chain.md)
- [SSRF no Top 10](../web/owasp-top-10.md)
