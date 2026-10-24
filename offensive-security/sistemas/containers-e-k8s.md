# Contêineres e Kubernetes: superfície

Contêiner não é máquina virtual. É **isolamento de processo** com namespace e cgroup. O Kubernetes é um **API server** com muito poder: quem autentica nele orquestra o cluster.

## Classes de risco

- Imagem com CVE, processo como root e volume da máquina.
- Socket do Docker (`/var/run/docker.sock`) montado no pod. Isso equivale, na prática, ao host.
- Segredo em variável de ambiente e em `kubectl get secret` amplo demais.
- Dashboard ou API na internet.
- RBAC: a service account de um pod cria pod privilegiado.
- Supply chain: imagem `latest` de registry sem controle.
- NetworkPolicy ausente: o pod da borda fala direto com o banco.

## O que estudar

- Docker: user namespace, sistema de arquivos raiz somente leitura e remoção de capability. Use a documentação oficial.
- Kubernetes: Pod Security Standards, RBAC, etcd e ingress.
- CIS Docker e CIS Kubernetes.
- OWASP Kubernetes Security Cheat Sheet.

Escape de contêiner é tópico avançado. Este guia não descreve exploit. No laboratório, use kind ou minikube **local**.

## Repositórios para aprofundar

[Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat), [Trivy](https://github.com/aquasecurity/trivy), [kube-hunter](https://github.com/aquasecurity/kube-hunter), [peirates](https://github.com/inguardians/peirates) (laboratório), [falco](https://github.com/falcosecurity/falco), [checkov](https://github.com/bridgecrewio/checkov). [Tabela de Kubernetes](../../pentest-tools-collection/README.md#containers-e-kubernetes).

## Leitura seguinte

- [Linux](../sistemas/linux-superficie.md)
- [CI/CD](../nuvem/cicd-e-supply-chain.md)
- [Nuvem](../nuvem/cloud-superficie.md)
