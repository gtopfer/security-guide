# 🛡️ Security Guide

Bem-vindo ao **Security Guide**! Um hub central em português com recursos de segurança digital, ferramentas OSINT e guias práticos — do básico ao avançado. Tudo **100% open source**, sem paywalls.

## Para quem é este guia?

| Perfil | Por onde começar |
|--------|-----------------|
| Usuário comum preocupado com privacidade | [Guia para Iniciantes](./for-noobs/README.md) |
| Pesquisador de segurança / OSINT | [Coleção de Ferramentas OSINT](./osint-tools-collection/README.md) |
| Quer aprender Google Dorks | [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) |
| Profissional de CTI / Threat Intel | [Inteligência de Ameaças](./osint-tools-collection/README.md#inteligência-de-ameaças--ioc) |

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

---

## 📖 Guia de Google Dorks

Está separado na seção OSINT, mas merece destaque: o [Guia de Google Dorks](./osint-tools-collection/docs/google-search/README.md) é util tanto para iniciantes (verificar o que está exposto sobre você) quanto para pesquisadores (recon de infraestrutura e dados sensíveis).

---

## 🤝 Contribuição

Contribuições são bem-vindas! Abra uma issue ou pull request para:

- Sugerir novas ferramentas FOSS
- Corrigir informações desatualizadas
- Adicionar seções ao guia para iniciantes

---

*Mantenha-se seguro e curioso.*
