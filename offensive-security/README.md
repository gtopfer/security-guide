# Estudos de segurança ofensiva

Material de **estudo** em português sobre segurança ofensiva: o que existe, como se organiza, o que ler e onde praticar com autorização. Não é uma trilha de certificação. Não é um roteiro de ataque.

> Pratique somente em **laboratório seu**, em aplicação vulnerável de propósito, ou em contrato e programa com **escopo escrito**. No Brasil, ataque sem autorização a sistema de terceiro pode configurar crime (entre outras normas, a Lei 12.737/2012 e o Marco Civil da Internet).

## Como usar esta pasta

1. Leia [O que é segurança ofensiva](fundamentos/o-que-e.md) e [Ética, escopo e lei](fundamentos/etica-e-lei.md).
2. Estude o [método](fundamentos/mentalidade-e-metodo.md) e as [taxonomias](fundamentos/taxonomias-mitre-owasp-cwe.md). Esses textos organizam o restante.
3. Percorra os temas (web, redes, sistemas, identidade, nuvem) na ordem que o seu contexto exigir.
4. Aprofunde com repositórios: [mapa de tema para repositório](biblioteca/mapa-ferramentas.md) e [coleção de pentest](../pentest-tools-collection/README.md). O formato é o mesmo da [coleção OSINT](../osint-tools-collection/README.md). O reconhecimento de host continua na coleção OSINT.
5. Feche o ciclo com [como estudar](pratica/como-estudar.md), [laboratórios legais](pratica/labs-legais.md) e o [glossário](biblioteca/glossario.md).

Cada documento explica **conceito, vocabulário, o que observar e o que ler**. Não traz payload, exploit nem passo para reproduzir ataque.

## Índice

### Fundamentos

| Documento | Sobre |
|-----------|--------|
| [O que é segurança ofensiva](fundamentos/o-que-e.md) | Pentest, red team, bug bounty e purple team: diferenças |
| [Ética, escopo e lei](fundamentos/etica-e-lei.md) | Autorização, regras de engajamento e disclosure |
| [Mentalidade e método](fundamentos/mentalidade-e-metodo.md) | PTES, kill chain, hipótese e nota |
| [Taxonomias](fundamentos/taxonomias-mitre-owasp-cwe.md) | ATT&CK, CAPEC, CWE, CVSS e OWASP |
| [Threat modeling](fundamentos/threat-modeling.md) | STRIDE, hipótese e fronteira |

### Reconhecimento

| Documento | Sobre |
|-----------|--------|
| [Visão geral de recon](reconhecimento/visao-geral.md) | Objetivo do reconhecimento no ciclo ofensivo |
| [Passivo vs ativo](reconhecimento/passivo-vs-ativo.md) | Ruído, risco legal e fonte pública |
| [Superfície de ataque](reconhecimento/mapeamento-de-superficie.md) | Ativo, exposição e priorização |

### Aplicações web e APIs

| Documento | Sobre |
|-----------|--------|
| [HTTP, cookies e sessão](web/modelo-http-e-sessao.md) | Como a web autentica e mantém estado |
| [OWASP Top 10](web/owasp-top-10.md) | Classe de risco, sem receita de exploit |
| [APIs e autorização](web/apis-e-auth.md) | REST, token, IDOR e BOLA |
| [Cliente, XSS e CSRF](web/client-side.md) | Confiança no navegador e same-origin |
| [Mobile](web/mobile-superficie.md) | Android, iOS e MASVS |

### Redes

| Documento | Sobre |
|-----------|--------|
| [TCP/IP e serviços](redes/modelo-tcpip-e-servicos.md) | Porta, banner e o que um scan indica |
| [Protocolos comuns](redes/protocolos-comuns.md) | DNS, HTTP, SMB, LDAP e SSH: superfície típica |
| [Wireless e físico](redes/wireless-e-fisico.md) | Wi-Fi e prédio, somente com regras de engajamento |

### Sistemas

| Documento | Sobre |
|-----------|--------|
| [Superfície Linux](sistemas/linux-superficie.md) | Usuário, SUID, serviço e pacote |
| [Superfície Windows](sistemas/windows-superficie.md) | SAM, serviço, token e UAC (conceitos) |
| [Privilégios](sistemas/privilegios-o-que-estudar.md) | Por que a escalada existe e o que estudar, sem receita |
| [Containers e Kubernetes](sistemas/containers-e-k8s.md) | Isolamento, RBAC e imagem |

### Identidade e diretório

| Documento | Sobre |
|-----------|--------|
| [Active Directory](identidade/active-directory-conceitos.md) | Domínio, Kerberos, GPO e relação de confiança |
| [Credenciais](identidade/autenticacao-e-credenciais.md) | Hash, MFA, spraying e força bruta (conceitos) |

### Nuvem, supply chain e pessoa

| Documento | Sobre |
|-----------|--------|
| [Superfície em nuvem](nuvem/cloud-superficie.md) | IAM, armazenamento público e metadado |
| [CI/CD e supply chain](nuvem/cicd-e-supply-chain.md) | Pipeline como caminho de comprometimento |
| [Engenharia social](humano/engenharia-social.md) | Pretexto e phishing como classe de risco |

### Fechamento (defesa e prática)

| Documento | Sobre |
|-----------|--------|
| [Detecção e logs](defesa/deteccao-e-logs.md) | O que o atacante deixa e o que o SOC procura |
| [Relatório e comunicação](defesa/relatorio-e-comunicacao.md) | Achado, impacto, evidência e correção |
| [Hardening pelo ataque](defesa/hardening-pelo-ataque.md) | Converter hipótese em controle |
| [Como estudar](pratica/como-estudar.md) | Ritmo, anotação e o que não omitir |
| [Labs legais](pratica/labs-legais.md) | Onde treinar com autorização explícita |
| [Livros e normas](biblioteca/livros-e-normas.md) | Referência estável |
| [Cursos e material livre](biblioteca/cursos-gratuitos.md) | OWASP, PortSwigger, MITRE e outros |
| [Mapa de ferramentas e repositórios](biblioteca/mapa-ferramentas.md) | Tema de estudo e repositório de software livre |
| [Coleção de pentest (catálogo)](../pentest-tools-collection/README.md) | Wiki, laboratório, web, AD, nuvem, engenharia reversa e purple team |
| [Glossário](biblioteca/glossario.md) | Termo ofensivo e defensivo |

## O que esta pasta não é

- Não substitui contrato, regras de engajamento nem curso pago.
- Não ensina a invadir conta, a contornar autenticação de terceiro nem a escrever malware.
- Não é material de prova de certificação. Não há simulado nem dump.

Estude o ataque para desenhar uma defesa melhor. Pratique somente onde a lei e o dono do sistema permitem.
