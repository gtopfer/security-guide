# ⚔️ Estudos de Segurança Ofensiva

Material de **estudo** em português sobre temas de segurança ofensiva: o que existe, como se organiza, o que ler e onde praticar com autorização. Não é trilha de certificação e não é um playbook de ataque.

> ⚠️ Pratique só em **labs seus**, aplicações propositalmente vulneráveis ou contratos/programas com **escopo escrito**. No Brasil, ataque não autorizado a sistema alheio pode configurar crime (entre outros, Lei 12.737/2012 e Marco Civil da Internet).

## Como usar esta pasta

1. Leia [O que é segurança ofensiva](fundamentos/o-que-e.md) e [Ética, escopo e lei](fundamentos/etica-e-lei.md).
2. Estude o [método](fundamentos/mentalidade-e-metodo.md) e as [taxonomias](fundamentos/taxonomias-mitre-owasp-cwe.md) — elas organizam o resto.
3. Percorra os temas (web, redes, sistemas, identidade, nuvem) na ordem que fizer sentido para você.
4. Feche com [como estudar](pratica/como-estudar.md), [labs legais](pratica/labs-legais.md) e o [glossário](biblioteca/glossario.md).
5. Ferramentas FOSS ficam na [coleção de pentest](../pentest-tools-collection/README.md) e na [coleção OSINT](../osint-tools-collection/README.md).

Cada documento explica **conceitos, vocabulário, o que observar e o que ler**. Não traz payloads, exploits nem passos para reproduzir ataques.

## Índice

### Fundamentos

| Documento | Sobre |
|-----------|--------|
| [O que é segurança ofensiva](fundamentos/o-que-e.md) | Pentest, red team, bug bounty, purple team — diferenças |
| [Ética, escopo e lei](fundamentos/etica-e-lei.md) | Autorização, regras de engajamento, disclosure |
| [Mentalidade e método](fundamentos/mentalidade-e-metodo.md) | PTES, kill chain, hipóteses, notas |
| [Taxonomias](fundamentos/taxonomias-mitre-owasp-cwe.md) | ATT&CK, CAPEC, CWE, CVSS, OWASP |
| [Threat modeling](fundamentos/threat-modeling.md) | STRIDE, hipóteses, fronteiras |

### Reconhecimento

| Documento | Sobre |
|-----------|--------|
| [Visão geral de recon](reconhecimento/visao-geral.md) | Objetivo do reconhecimento no ciclo ofensivo |
| [Passivo vs ativo](reconhecimento/passivo-vs-ativo.md) | Ruído, risco legal, fontes públicas |
| [Superfície de ataque](reconhecimento/mapeamento-de-superficie.md) | Ativos, exposição, priorização |

### Aplicações web e APIs

| Documento | Sobre |
|-----------|--------|
| [HTTP, cookies e sessão](web/modelo-http-e-sessao.md) | Como a web autentica e mantém estado |
| [OWASP Top 10](web/owasp-top-10.md) | Classes de risco, não receitas de exploit |
| [APIs e autorização](web/apis-e-auth.md) | REST, tokens, IDOR, BOLA |
| [Cliente, XSS e CSRF](web/client-side.md) | Confiança no browser, same-origin |
| [Mobile](web/mobile-superficie.md) | Android/iOS, MASVS |

### Redes

| Documento | Sobre |
|-----------|--------|
| [TCP/IP e serviços](redes/modelo-tcpip-e-servicos.md) | Portas, banners, o que um scan *significa* |
| [Protocolos comuns](redes/protocolos-comuns.md) | DNS, HTTP, SMB, LDAP, SSH — superfície típica |
| [Wireless e físico](redes/wireless-e-fisico.md) | Wi-Fi, prédio — só com ROE |

### Sistemas

| Documento | Sobre |
|-----------|--------|
| [Superfície Linux](sistemas/linux-superficie.md) | Usuários, SUID, serviços, pacotes |
| [Superfície Windows](sistemas/windows-superficie.md) | SAM, serviços, tokens, UAC (conceitos) |
| [Privilégios](sistemas/privilegios-o-que-estudar.md) | Por que existe escalada; o que estudar sem “receita” |
| [Containers e Kubernetes](sistemas/containers-e-k8s.md) | Isolamento, RBAC, imagem |

### Identidade e diretório

| Documento | Sobre |
|-----------|--------|
| [Active Directory](identidade/active-directory-conceitos.md) | Domínio, Kerberos, GPOs, confiança |
| [Credenciais](identidade/autenticacao-e-credenciais.md) | Hash, MFA, spraying vs brute (conceitos) |

### Nuvem, supply chain e humano

| Documento | Sobre |
|-----------|--------|
| [Superfície em nuvem](nuvem/cloud-superficie.md) | IAM, storage público, metadados |
| [CI/CD e supply chain](nuvem/cicd-e-supply-chain.md) | Pipeline como caminho de compromisso |
| [Engenharia social](humano/engenharia-social.md) | Pré-texto, phishing como classe de risco |

### Fechamento (defesa e prática)

| Documento | Sobre |
|-----------|--------|
| [Detecção e logs](defesa/deteccao-e-logs.md) | O que o atacante deixa; o que o SOC procura |
| [Relatório e comunicação](defesa/relatorio-e-comunicacao.md) | Achado, impacto, evidência, remediação |
| [Hardening pelo ataque](defesa/hardening-pelo-ataque.md) | Inverter hipóteses em controles |
| [Como estudar](pratica/como-estudar.md) | Ritmo, anotações, o que não pular |
| [Labs legais](pratica/labs-legais.md) | Onde treinar com autorização explícita |
| [Livros e normas](biblioteca/livros-e-normas.md) | Referências estáveis |
| [Cursos e material livre](biblioteca/cursos-gratuitos.md) | OWASP, PortSwigger, MITRE, etc. |
| [Glossário](biblioteca/glossario.md) | Termos ofensivos e defensivos |

## O que esta pasta não é

- Não substitui contrato, ROE nem curso pago.
- Não ensina a invadir contas, burlar autenticação de terceiros nem escrever malware.
- Não é material de prova de certificação (sem simulados, sem dumps).

**Estude o ataque para desenhar defesa melhor — e só pratique onde a lei e o dono do sistema permitem.**
