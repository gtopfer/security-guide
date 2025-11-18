# 🛡️ Red Team Guide

Repositório dedicado a planejamento e execução de operações Red Team/Purple Team com foco em TTPs MITRE ATT&CK, emulações adversárias e automação de laboratórios.

## Objetivos
- Centralizar playbooks ofensivos, cenários de emulação e documentação de infraestrutura.
- Reunir scripts e ferramentas customizadas (ANSI/Python/Go) para facilitar campanhas.
- Manter laboratórios reproduzíveis (Terraform, Ansible, Docker) para treinos internos.

## Estrutura sugerida
```
Red-Team-Guide/
├── README.md
├── docs/
│   ├── metodologia.md
│   └── mitre-mapping.md
├── scripts/
│   ├── automation/
│   └── tradecraft/
├── labs/
│   ├── adversary-emulation/
│   └── detection-bypass/
└── playbooks/
    ├── phishing-chain/
    └── lateral-movement/
```

## Próximos passos
1. Adicionar guia de metodologia em `docs/metodologia.md`.
2. Popular `labs/` com ambientes replicáveis (Azure, AWS, On-Prem).
3. Incluir checklists de ROE, comunicação e métricas.
