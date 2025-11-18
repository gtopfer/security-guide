# 🔵 Blue Team Guide

Coletânea de práticas defensivas, engenharia de detecções e automações de resposta incidentes.

## Objetivos
- Documentar arquiteturas de monitoração (SIEM/EDR) e guias de hardening.
- Versionar playbooks de resposta e runbooks de contenção.
- Disponibilizar scripts para correlação, caça defensiva e automação de alertas.

## Estrutura sugerida
```
Blue-Team-Guide/
├── README.md
├── docs/
│   ├── arquitetura.md
│   └── soe.md
├── playbooks/
│   ├── incident-response/
│   └── identity-hardening/
├── scripts/
│   ├── detections/
│   └── automations/
└── metrics/
    └── kpis.csv
```

## Próximos passos
1. Criar documentação inicial em `docs/arquitetura.md` descrevendo camadas defensivas.
2. Adicionar primeiros playbooks (e.g., ransomware, phishing).
3. Popular `scripts/` com queries Sigma/KQL/SPL e automações (Python, PowerShell).
