# MITRE ATT&CK Mapping

| Fase | Tática | Técnicas | Observações |
|------|--------|----------|-------------|
| Recon | TA0043 | T1595, T1592 | Coleta inicial de infraestrutura/credenciais. |
| Initial Access | TA0001 | T1566.001, T1190 | Phishing spear, exploração de aplicativo exposto. |
| Execution | TA0002 | T1059, T1203 | Execução de payloads PowerShell e exploits client-side. |
| Persistence | TA0003 | T1547.001, T1136.002 | Autoruns & criação de contas cloud. |
| Privilege Escalation | TA0004 | T1068, T1484.001 | Exploração de privilégios locais e domínio. |
| Defense Evasion | TA0005 | T1070, T1562 | Limpeza de logs, desabilitar EDR. |
| Credential Access | TA0006 | T1003.006, T1552 | Dump LSASS, harvesting secrets cloud. |
| Discovery | TA0007 | T1087, T1018 | Enumeração de usuários e redes. |
| Lateral Movement | TA0008 | T1021.002, T1550.002 | SMB/WinRM e tokens reutilizados. |
| Collection | TA0009 | T1114, T1056 | Emails e keylogging. |
| Command & Control | TA0011 | T1071.001, T1095 | HTTPS C2 e canais custom. |
| Exfiltration | TA0010 | T1041, T1567.002 | Transferência HTTPS + Storage cloud. |
