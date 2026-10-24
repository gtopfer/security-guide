# Mapa: tema de estudo, repositório e ferramenta

A coleção OSINT cobre **reconhecimento passivo**. A [coleção de pentest](../../pentest-tools-collection/README.md) é o equivalente ofensivo: wiki, laboratório, proxy, web, AD, nuvem, engenharia reversa, purple team e C2 de laboratório.

Use este mapa para **aprofundar um tema** sem abrir 200 repositórios. Clone somente o que você vai ler ou executar nesta semana.

## Fundamentos e método

| Estudo | Repositório ou ferramenta |
|--------|------------------|
| Ética e relatório | [public-pentesting-reports](https://github.com/juliocesarfort/public-pentesting-reports), [SysReptor](https://github.com/Syslifters/sysreptor), [pwndoc](https://github.com/pwndoc/pwndoc) |
| ATT&CK | [attack-stix-data](https://github.com/mitre-attack/attack-stix-data), site attack.mitre.org |
| CAPEC e STIX | [mitre/cti](https://github.com/mitre/cti) |
| OWASP | [Top10](https://github.com/OWASP/Top10), [wstg](https://github.com/OWASP/wstg), [ASVS](https://github.com/OWASP/ASVS), [CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) |
| Modelo de ameaça | [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon) |
| Wiki geral | [HackTricks](https://github.com/HackTricks-wiki/hacktricks) |

## Reconhecimento

Subdomínio, Certificate Transparency, httpx e nmap: [OSINT](../../osint-tools-collection/README.md).

Camada ofensiva sobre esse mapa:

| Repositório | Para quê |
|-----|----------|
| [AutoRecon](https://github.com/Tib3rius/AutoRecon) | Enumeração de uma máquina de laboratório |
| [reconftw](https://github.com/six2dez/reconftw) | Pipeline de reconhecimento (bug bounty no escopo) |
| [nuclei](https://github.com/projectdiscovery/nuclei) e [templates](https://github.com/projectdiscovery/nuclei-templates) | Verificação conhecida, com limite de taxa |
| [WhatWeb](https://github.com/urbanadventurer/WhatWeb) | Fingerprint |
| [testssl.sh](https://github.com/drwetter/testssl.sh) | TLS do seu host |

## Web e API

| Repositório | Para quê |
|-----|----------|
| [zaproxy](https://github.com/zaproxy/zaproxy) | Proxy de software livre |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interceptação pela linha de comando |
| [ffuf](https://github.com/ffuf/ffuf), [feroxbuster](https://github.com/epi052/feroxbuster), [gobuster](https://github.com/OJ/gobuster) | Descoberta |
| [Arjun](https://github.com/s0md3v/Arjun), [LinkFinder](https://github.com/GerbenJavado/LinkFinder) | Parâmetro e JavaScript |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | SQL injection no Juice Shop ou no DVWA |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | Modelo de JWT |
| [dalfox](https://github.com/hahwul/dalfox) | XSS em laboratório |
| [schemathesis](https://github.com/schemathesis/schemathesis), [OFFAT](https://github.com/OWASP/OFFAT) | API e OpenAPI |
| [SecLists](https://github.com/danielmiessler/SecLists) | Wordlist |
| [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | Folha de referência para estudo |
| Laboratórios: Juice Shop, WebGoat, crAPI e DVGA — tabela completa na coleção |

## Identidade e AD

| Repositório | Para quê |
|-----|----------|
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | Laboratório de AD |
| [DetectionLab](https://github.com/clong/DetectionLab) | AD e logs |
| [Impacket](https://github.com/fortra/impacket) | Protocolos Windows |
| [BloodHound](https://github.com/SpecterOps/BloodHound) | Grafo de ACL |
| [NetExec](https://github.com/Pennyw0rth/NetExec) | SMB, LDAP e WinRM em laboratório |
| [Certipy](https://github.com/ly4k/Certipy) | AD CS |
| [InternalAllTheThings](https://github.com/swisskyrepo/InternalAllTheThings), [WADComs](https://github.com/WADComs/WADComs.github.io) | Referência |
| [ROADtools](https://github.com/dirkjanm/ROADtools) | Entra ID |

## Host Linux e Windows

| Repositório | Para quê |
|-----|----------|
| [PEASS-ng](https://github.com/peass-ng/PEASS-ng) | LinPEAS e WinPEAS |
| [GTFOBins](https://github.com/GTFOBins/GTFOBins.github.io) | Living off the land no Unix |
| [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS) | Living off the land no Windows |
| [lynis](https://github.com/CISOfy/lynis) | Hardening |
| [Seatbelt](https://github.com/GhostPack/Seatbelt) | Enumeração Windows |

## Nuvem e Kubernetes

| Repositório | Para quê |
|-----|----------|
| [HackTricks Cloud](https://github.com/HackTricks-wiki/hacktricks-cloud) | Wiki |
| [Prowler](https://github.com/prowler-cloud/prowler), [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Auditoria |
| [Pacu](https://github.com/RhinoSecurityLabs/pacu), [CloudFox](https://github.com/BishopFox/cloudfox) | Conta de laboratório |
| [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | Cenário AWS |
| [Kubernetes Goat](https://github.com/madhuakula/kubernetes-goat) | Kubernetes vulnerável de propósito |
| [Trivy](https://github.com/aquasecurity/trivy), [kube-hunter](https://github.com/aquasecurity/kube-hunter) | Imagem e API |
| [Stratus Red Team](https://github.com/DataDog/stratus-red-team) | Técnica na sua conta |

## Engenharia reversa, laboratório de malware e memória

| Repositório | Para quê |
|-----|----------|
| [Ghidra](https://github.com/NationalSecurityAgency/ghidra) | Decompilador |
| [radare2](https://github.com/radareorg/radare2) / [Cutter](https://github.com/rizinorg/cutter) | Engenharia reversa |
| [capa](https://github.com/mandiant/capa), [YARA](https://github.com/VirusTotal/yara) | Comportamento e regra |
| [Volatility 3](https://github.com/volatilityfoundation/volatility3) | Memória RAM |

## Purple team e detecção

| Repositório | Para quê |
|-----|----------|
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Código T no seu computador |
| [CALDERA](https://github.com/mitre/caldera) | Emulação |
| [Sigma](https://github.com/SigmaHQ/sigma) | Regra |
| [Wazuh](https://github.com/wazuh/wazuh) | SIEM de software livre |
| [falco](https://github.com/falcosecurity/falco) | Tempo de execução de contêiner |

## Como não perder o foco

1. Um tema por ciclo. Exemplo: somente web, ZAP, Juice Shop e WSTG.
2. Deixe a wiki (HackTricks) aberta. Use a ferramenta para **confirmar** o que você já descreveu na nota.
3. Não instale C2 (Sliver, Mythic ou Metasploit completo) no primeiro mês. Isso não ensina HTTP.
4. Reconhecimento sem a coleção OSINT deixa o pentest sem mapa.

Lista viva e completa: [pentest-tools-collection/README.md](../../pentest-tools-collection/README.md).
