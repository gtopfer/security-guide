# Metodologia de Threat Intelligence

## 1. Preparação e escopo

- Defina a pergunta de inteligência (tático, operacional, estratégico) e os stakeholders responsáveis por decisions.
- Estabeleça janelas de coleta, sensibilidade dos dados e controles legais (LGPD, acordos com fornecedores).
- Mapeie fontes internas disponíveis (EDR, SIEM, fluxo de incidentes) e dependências externas (ISAC, parceiros, feeds comerciais).

## 2. Coleta e enriquecimento

- Combine fontes abertas, comerciais e dados proprietários; catalogue formatos (STIX/TAXII, JSON, CSV) e limites de uso.
- Automatize a ingestão com conectores (TAXII, APIs REST, S3 buckets) e salve logs das execuções.
- Enriqueca IOCs com metadados (timestamp, primeiro/último avistamento, TTPs MITRE ATT&CK) antes de consolidar.

## 3. Normalização e scoring

- Normalize os campos (tipo de IOC, confiança, fonte) para suportar correlação; descarte duplicados.
- Calcule score composto usando peso por fonte + relevância para o seu ambiente.
- Estruture os dados para consumo downstream (SIEM, playbooks SOAR, dashboards) e mantenha versionamento.

## 4. Correlação e hipóteses

- Aplique regras de associação (mesmo cluster de infraestrutura, sobreposição de TTPs) para conectar eventos.
- Busque sinais de cadeia de ataque completa (initial access → execution → persistence) e valide contra linha de base.
- Documente hipóteses, falsos positivos e lacunas que precisam de coleta adicional.

## 5. Disseminação e feedback

- Produza produtos orientados ao público correto: alertas rápidos para SOC, relatórios executivos ou packs para Red Team.
- Defina ações recomendadas (bloqueio, regra SIEM / EDR, awareness) e responsável pela validação.
- Ao fechar o ciclo, colete feedback dos consumidores e atualize requisitos da próxima iteração.

## Checklist rápido

- [ ] Escopo, janela de coleta e controles legais documentados.
- [ ] Fontes catalogadas (owner, SLA, formato, custo).
- [ ] Regras de normalização + score publicadas.
- [ ] Processos de disseminação e confidencialidade definidos.
- [ ] Métricas de qualidade (tempo médio, taxa de ação aplicada) acompanhadas.

## Referências úteis

- [MITRE ATT&CK](https://attack.mitre.org/)
- [ENISA Threat Landscape](https://www.enisa.europa.eu/topics/threat-risk-management/threats-and-trends)
- [FIRST CTI SIG](https://www.first.org/global/sigs/cti)
