# Containers e Kubernetes — superfície

Container não é VM. É **isolamento de processo** com namespaces e cgroups. Kubernetes é um **API server** poderoso: quem autentica nele orquestra o cluster.

## Classes de risco

- Imagem com CVE + processo como root + volume da máquina.
- Socket Docker (`/var/run/docker.sock`) montado no pod = quase o host.
- Secrets em env var e no `kubectl get secret` amplo demais.
- Dashboard ou API na internet.
- RBAC: service account de um pod que cria pods privilegiados.
- Supply chain: imagem `latest` de registry duvidoso.
- NetworkPolicy ausente: pod da frente fala com o banco direto.

## O que estudar

- Docker: user namespace, read-only rootfs, capabilities drop — docs oficiais.
- Kubernetes: Pod Security Standards, RBAC, etcd, ingress.
- CIS Docker / CIS Kubernetes.
- OWASP Kubernetes Security Cheat Sheet.

Breakout de container é tópico avançado; este guia não descreve exploits. Em lab, use Kind/minikube **local**.

## Git para aprofundar

[Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat), [Trivy](https://github.com/aquasecurity/trivy), [kube-hunter](https://github.com/aquasecurity/kube-hunter), [peirates](https://github.com/inguardians/peirates) (lab), [falco](https://github.com/falcosecurity/falco), [checkov](https://github.com/bridgecrewio/checkov). [Tabela K8s](../../pentest-tools-collection/README.md#containers-e-kubernetes).

## Leitura seguinte

- [Linux](../sistemas/linux-superficie.md)
- [CI/CD](../nuvem/cicd-e-supply-chain.md)
- [Cloud](../nuvem/cloud-superficie.md)
