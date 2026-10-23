# Mapa: tema de estudo → Git e ferramentas

A coleção OSINT cobre **recon/passivo**. A [coleção de pentest](../../pentest-tools-collection/README.md) agora é o equivalente ofensivo: wikis, labs, proxy, web, AD, nuvem, RE, purple, C2 de lab.

Use este mapa para **aprofundar um tema** sem se perder em 200 repos. Clone só o que você vai ler ou rodar nesta semana.

## Fundamentos e método

| Estudo | Git / ferramenta |
|--------|------------------|
| Ética, relatório | [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports), [SysReptor](https://github.com/Syslifters/sysreptor), [pwndoc](https://github.com/pwndoc/pwndoc) |
| ATT&CK | [attack-stix-data](https://github.com/mitre-attack/attack-stix-data), site attack.mitre.org |
| CAPEC / STIX | [mitre/cti](https://github.com/mitre/cti) |
| OWASP | [Top10](https://github.com/OWASP/Top10), [wstg](https://github.com/OWASP/wstg), [ASVS](https://github.com/OWASP/ASVS), [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) |
| Threat model | [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) |
| Wiki geral | [HackTricks](https://github.com/HackTricks-wiki/hacktricks) |

## Reconhecimento

Tudo que é subdomínio, CT, httpx, nmap: [OSINT](../../osint-tools-collection/README.md).

Ofensivo em cima do mapa:

| Git | Para quê |
|-----|----------|
| [AutoRecon](https://github.com/Tib3rius/AutoRecon) | Enum de uma máquina de **lab** |
| [reconftw](https://github.com/six2dez/reconftw) | Pipeline de recon (bounty in-scope) |
| [nuclei](https://github.com/projectdiscovery/nuclei) + [templates](https://github.com/projectdiscovery/nuclei-templates) | Checagens conhecidas, com rate limit |
| [WhatWeb](https://github.com/urbanadventurer/WhatWeb) | Fingerprint |
| [testssl.sh](https://github.com/drwetter/testssl.sh) | TLS do seu host |

## Web e API

| Git | Para quê |
|-----|----------|
| [zaproxy](https://github.com/zaproxy/zaproxy) | Proxy FOSS |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interceptação CLI |
| [ffuf](https://github.com/ffuf/ffuf), [feroxbuster](https://github.com/epi052/feroxbuster), [gobuster](https://github.com/OJ/gobuster) | Discovery |
| [Arjun](https://github.com/s0md3v/Arjun), [LinkFinder](https://github.com/GerbenJavado/LinkFinder) | Parâmetros e JS |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | SQLi **em Juice Shop/DVWA** |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | Modelo JWT |
| [dalfox](https://github.com/hahwul/dalfox) | XSS em lab |
| [schemathesis](https://github.com/schemathesis/schemathesis), [OFFAT](https://github.com/OWASP/OFFAT) | API/OpenAPI |
| [SecLists](https://github.com/danielmiessler/SecLists) | Wordlists |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Cheatsheet (estudo) |
| Labs: Juice Shop, WebGoat, crAPI, DVGA — tabela completa na coleção |

## Identidade / AD

| Git | Para quê |
|-----|----------|
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | Lab AD |
| [DetectionLab](https://github.com/clong/DetectionLab) | AD + logs |
| [Impacket](https://github.com/fortra/impacket) | Protocolos Windows |
| [BloodHound](https://github.com/SpecterOps/BloodHound) | Grafo de ACL |
| [NetExec](https://github.com/Pennyw0rth/NetExec) | SMB/LDAP/WinRM em lab |
| [Certipy](https://github.com/ly4k/Certipy) | AD CS |
| [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings), [WADComs](https://github.com/WADComs/WADComs.github.io) | Referência |
| [ROADtools](https://github.com/dirkjanm/ROADtools) | Entra ID |

## Linux / Windows host

| Git | Para quê |
|-----|----------|
| [PEASS-ng](https://github.com/peass-ng/PEASS-ng) | LinPEAS / WinPEAS |
| [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io) | Unix LOL |
| [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) | Windows LOL |
| [lynis](https://github.com/CISOfy/lynis) | Hardening |
| [Seatbelt](https://github.com/GhostPack/Seatbelt) | Enum Windows |

## Nuvem e K8s

| Git | Para quê |
|-----|----------|
| [HackTricks Cloud](https://github.com/HackTricks-wiki/hacktricks-cloud) | Wiki |
| [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Audit |
| [Pacu](https://github.com/RhinoSecurityLabs/pacu), [CloudFox](https://github.com/BishopFox/cloudfox) | Conta **lab** |
| [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | Cenários AWS |
| [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) | K8s ruim de propósito |
| [Trivy](https://github.com/aquasecurity/trivy), [kube-hunter](https://github.com/aquasecurity/kube-hunter) | Imagem / API |
| [Stratus Red Team](https://github.com/DataDog/stratus-red-team) | Técnicas na sua conta |

## Reverse, malware lab, memória

| Git | Para quê |
|-----|----------|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Decompiler |
| [radare2](https://github.com/radareorg/radare2) / [Cutter](https://github.com/rizinorg/cutter) | RE |
| [capa](https://github.com/mandiant/capa), [YARA](https://github.com/VirusTotal/yara) | Comportamento / regras |
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | RAM |

## Purple / detecção

| Git | Para quê |
|-----|----------|
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | T-codes no seu PC |
| [CALDERA](https://github.com/mitre/caldera) | Emulação |
| [Sigma](https://github.com/SigmaHQ/sigma) | Regras |
| [Wazuh](https://github.com/wazuh/wazuh) | SIEM FOSS |
| [falco](https://github.com/falcosecurity/falco) | Runtime containers |

## Como não se afogar

1. Um tema por ciclo (ex.: só web + ZAP + Juice Shop + WSTG).
2. Wiki (HackTricks) aberta; ferramenta só para **confirmar** o que você já descreveu em nota.
3. Não instale C2 (Sliver, Mythic, Metasploit full) no primeiro mês — não ensina HTTP.
4. Recon sem OSINT collection é pentest cego.

Lista viva e completa: [pentest-tools-collection/README.md](../../pentest-tools-collection/README.md).
