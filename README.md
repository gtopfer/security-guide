# Security Guide

[![Licença: GPL v3](https://img.shields.io/badge/Licen%C3%A7a-GPLv3-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-bem--vindas-brightgreen.svg)](CONTRIBUTING.md)
[![100% FOSS](https://img.shields.io/badge/ferramentas-100%25%20FOSS-orange.svg)](osint-tools-collection/README.md)

O **Security Guide** reúne, em português, material de segurança digital. O repositório cobre proteção pessoal, defesa contra engenharia social, OSINT, pentest, red team e estudo ofensivo. As ferramentas listadas são software livre. Este guia não vende acesso a conteúdo.

## Índice

- [Para quem é este guia](#para-quem-é-este-guia)
- [Roteiro de estudo](#roteiro-de-estudo)
- [Conteúdo](#conteúdo)
- [Estudos ofensivos](./offensive-security/README.md)
- [Engenharia social (defesa)](./social-engineering/README.md)
- [Guia de Google Dorks](#guia-de-google-dorks)
- [Contribuição](#contribuição)
- [Código de Conduta](CODE_OF_CONDUCT.md)
- [Licença](#licença)

## Para quem é este guia

| Perfil | Ponto de partida |
|--------|------------------|
| Pessoa que protege a própria conta e os próprios dados | [Fundamentos para iniciantes](./for-noobs/README.md) |
| Pesquisador de segurança ou de OSINT | [Coleção de ferramentas OSINT](./osint-tools-collection/README.md) |
| Pessoa que estuda operadores de busca do Google | [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) |
| Profissional de CTI ou de threat intelligence | [Inteligência de ameaças](./osint-tools-collection/README.md#inteligência-de-ameaças--ioc) |
| Pentester, red team ou programa de bug bounty | [Coleção de ferramentas de pentest](./pentest-tools-collection/README.md) |
| Pessoa que estuda segurança ofensiva (conceitos, sem trilha de certificação) | [Estudos de segurança ofensiva](./offensive-security/README.md) |
| Pessoa que reconhece golpe e responde no trabalho (usuário, service desk ou SOC) | [Engenharia social: conceitos e defesa](./social-engineering/README.md) |

## Roteiro de estudo

Siga esta ordem quando o estudo começa do zero.

```
Nível 1 — Proteção pessoal
└── Fundamentos para iniciantes: senhas, 2FA, criptografia, phishing, cópias de segurança
    └── Engenharia social: conceitos, sinais e playbooks de defesa

Nível 2 — Exposição pública
└── Pegada digital: Google Dorks sobre a própria pessoa; verificação de e-mails em vazamentos

Nível 3 — Ferramentas OSINT básicas
└── Sherlock (nomes de usuário), holehe (e-mails), Subfinder (domínios)

Nível 4 — Reconhecimento de infraestrutura
└── Amass, httpx, GoWitness, Nmap

Nível 5 — Análise e correlação
└── IntelOwl, MISP, OpenCTI, regras Sigma

Nível 6 — Automação de pipelines
└── n8n, Prefect, Cortex/Analyzers

Nível 7 — Segurança ofensiva (opcional; exige autorização por escrito)
└── Estudos (método, web, AD, nuvem) + laboratórios legais + coleção de pentest
```

Cada nível depende do nível anterior. Estude a defesa antes do reconhecimento ativo. Essa ordem reduz o risco de uso fora de escopo.

## Conteúdo

### 1. [Fundamentos para iniciantes](./for-noobs/README.md)

Guia prático para proteger contas, dispositivos e dados. O texto define o termo técnico quando ele aparece.

- Higiene básica: atualizações e bloqueio de tela
- Senhas e gerenciadores
- Autenticação de dois fatores (2FA)
- Navegação e VPN
- Comunicação (Signal, Proton Mail)
- Criptografia de disco (BitLocker, FileVault, LUKS)
- Phishing e engenharia social
- Dispositivos móveis
- Resposta quando uma conta ou um dispositivo é comprometido
- Cópias de segurança (regra 3-2-1)
- Verificação da pegada digital

### 2. [Coleção de ferramentas OSINT](./osint-tools-collection/README.md)

Catálogo de projetos de código aberto para investigação OSINT e CTI. A execução é local. O uso básico não exige cadastro pago.

- Frameworks e suítes de reconhecimento
- Perfis e redes sociais
- E-mail, telefone e credenciais
- Domínios, endereços IP e infraestrutura
- Inteligência de ameaças (IOC e CTI)
- Automação e pipelines

### 3. [Coleção de ferramentas de pentest](./pentest-tools-collection/README.md)

Catálogo de ferramentas e listas de código aberto para pentest, red team e bug bounty. Use estas ferramentas somente com autorização por escrito.

- Listas e coleções de referência
- Ferramentas de teste (Metasploit, sqlmap, dirsearch, Hydra)
- Agentes de IA para pentest (uso experimental, com escopo)
- Laboratórios e aplicações vulneráveis de propósito

### 4. [Estudos de segurança ofensiva](./offensive-security/README.md)

Documentos em português sobre temas ofensivos: método, reconhecimento, web, API, redes, Linux, Windows, Active Directory, nuvem, CI/CD, engenharia social, detecção e relatório. Não há trilha de certificação. Não há payload. Não há procedimento de exploit.

- Fundamentos: ética, PTES, ATT&CK e modelagem de ameaças
- Superfícies: web, mobile, protocolos, identidade, nuvem e contêineres
- Prática em laboratórios legais e material livre (OWASP, PortSwigger, MITRE)
- Catálogo FOSS no mesmo formato da coleção OSINT: [coleção de pentest](./pentest-tools-collection/README.md) (HackTricks, ZAP, Impacket, GOAD, Prowler)

### 5. [Engenharia social: conceitos e defesa](./social-engineering/README.md)

Trilha sobre phishing, vishing, pretexting e fraude de e-mail corporativo. O texto explica o risco e a defesa. Não há roteiro de ataque. Não há kit. Não há modelo de mensagem.

- Conceitos e princípios de influência, só como alerta
- Canais e sinais para a pessoa, para o service desk e para o SOC
- Playbooks: reporte, contenção de conta, autenticação de e-mail e treino
- Fontes: CERT.br, NIST, CISA, MITRE e software livre de defesa

## Guia de Google Dorks

O guia fica na seção OSINT. O [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) serve a dois usos. A pessoa iniciante verifica o que está publicado sobre ela. O pesquisador consulta infraestrutura e arquivos públicos dentro do escopo autorizado.

## Contribuição

Contribuições são bem-vindas. Leia o [guia de contribuição](CONTRIBUTING.md) antes de abrir uma issue ou um pull request. Você pode:

- Sugerir uma ferramenta de software livre.
- Corrigir uma informação desatualizada ou um link quebrado.
- Ampliar o guia para iniciantes.
- Ampliar a trilha de [engenharia social](./social-engineering/README.md) com conceito e defesa, sem roteiro de ataque.
- Ampliar os [estudos de segurança ofensiva](./offensive-security/README.md) com conceitos e referências, sem exploit.

Este repositório é um espaço de estudo. Siga o [Código de Conduta](CODE_OF_CONDUCT.md). OSINT ético e prática ofensiva exigem autorização.

## Licença

Este projeto usa a [GNU General Public License v3.0](LICENSE).
A participação também segue o [Código de Conduta](CODE_OF_CONDUCT.md).
