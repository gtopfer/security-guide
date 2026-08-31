# 🛡️ Security Guide

[![Licença: GPL v3](https://img.shields.io/badge/Licen%C3%A7a-GPLv3-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-bem--vindas-brightgreen.svg)](CONTRIBUTING.md)
[![100% FOSS](https://img.shields.io/badge/ferramentas-100%25%20FOSS-orange.svg)](osint-tools-collection/README.md)

Bem-vindo ao **Security Guide**! Um hub central em português com recursos de segurança digital, ferramentas OSINT, pentest/red team e guias práticos — do básico ao avançado. Tudo **100% open source**, sem paywalls.

## Índice

- [Para quem é este guia?](#para-quem-é-este-guia)
- [Roadmap de Aprendizado](#-roadmap-de-aprendizado)
- [Conteúdo](#-conteúdo)
- [Guia de Google Dorks](#-guia-de-google-dorks)
- [Contribuição](#-contribuição)
- [Licença](#licença)

## Para quem é este guia?

| Perfil | Por onde começar |
|--------|-----------------|
| Usuário comum preocupado com privacidade | [Guia para Iniciantes](./for-noobs/README.md) |
| Pesquisador de segurança / OSINT | [Coleção de Ferramentas OSINT](./osint-tools-collection/README.md) |
| Quer aprender Google Dorks | [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) |
| Profissional de CTI / Threat Intel | [Inteligência de Ameaças](./osint-tools-collection/README.md#inteligência-de-ameaças--ioc) |
| Pentester / Red Team / Bug Bounty | [Coleção de Ferramentas de Pentest](./pentest-tools-collection/README.md) |

---

## 🗺️ Roadmap de Aprendizado

Se você está começando do zero e quer progredir de forma estruturada:

```
Nível 1 — Proteção pessoal
└── Guia para Iniciantes: senhas, 2FA, criptografia, phishing, backups

Nível 2 — Entender sua exposição
└── Pegada digital: Google Dorks sobre si mesmo, verificação de emails vazados

Nível 3 — Ferramentas OSINT básicas
└── Sherlock (usernames), holehe (emails), Subfinder (domínios)

Nível 4 — Reconhecimento de infraestrutura
└── Amass, httpx, GoWitness, Nmap

Nível 5 — Análise e correlação
└── IntelOwl, MISP, OpenCTI, Sigma rules

Nível 6 — Automação de pipelines
└── n8n, Prefect, Cortex/Analyzers

Nível 7 — Pentest e red team (opcional, requer autorização)
└── Labs (Juice Shop, Mutillidae), sqlmap, Metasploit, Sn1per
```

> Cada nível pressupõe domínio do anterior. Não pule etapas — entender como se defender é o que torna um pesquisador ético eficaz.

---

## 📂 Conteúdo

### 1. [Guia para Iniciantes (For Noobs)](./for-noobs/README.md)

Um guia prático para quem está começando a se preocupar com segurança digital e privacidade. Sem jargão técnico desnecessário.

- Higiene cibernética básica (atualizações, bloqueio de tela)
- Senhas fortes e gerenciadores
- Autenticação de dois fatores (2FA)
- Navegação segura e VPN
- Comunicação segura (Signal, ProtonMail)
- Criptografia de disco (BitLocker, FileVault, LUKS)
- Phishing e engenharia social
- Segurança mobile e resposta a incidentes (o que fazer se você for comprometido)
- Backups com a regra 3-2-1
- Como verificar sua pegada digital

### 2. [Coleção de Ferramentas OSINT](./osint-tools-collection/README.md)

Uma biblioteca viva com projetos **100% open source** para investigações OSINT/CTI. Executáveis localmente, sem cadastros pagos.

- Frameworks & suites de reconhecimento
- Perfis e redes sociais
- Email, telefone e credenciais
- Domínios, IPs e infraestrutura
- Inteligência de ameaças (IOC/CTI)
- Automação e pipelines
- E muito mais...

### 3. [Coleção de Ferramentas de Pentest](./pentest-tools-collection/README.md)

Ferramentas e listas **100% open source** para pentest, red team e bug bounty — uso autorizado apenas.

- Listas e coleções de recursos
- Ferramentas clássicas (Metasploit, sqlmap, dirsearch, Hydra...)
- Agentes de IA para pentest (experimental)
- Labs e apps propositalmente vulneráveis para praticar

---

## 📖 Guia de Google Dorks

Está separado na seção OSINT, mas merece destaque: o [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) é util tanto para iniciantes (verificar o que está exposto sobre você) quanto para pesquisadores (recon de infraestrutura e dados sensíveis).

---

## 🤝 Contribuição

Contribuições são bem-vindas! Veja o [guia de contribuição](CONTRIBUTING.md) para abrir uma issue ou pull request para:

- Sugerir novas ferramentas FOSS
- Corrigir informações desatualizadas ou links quebrados
- Adicionar seções ao guia para iniciantes

---

*Mantenha-se seguro e curioso.*


## Licença

Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).
