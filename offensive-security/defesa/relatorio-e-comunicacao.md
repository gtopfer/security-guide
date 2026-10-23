# Relatório e comunicação

O entregável de pentest não é a shell: é o **texto que o time consegue corrigir**. Relatórios públicos de consultorias (lista na [coleção de pentest](../../pentest-tools-collection/README.md)) ensinam tom e estrutura.

## Estrutura que funciona

1. **Sumário executivo** — risco em português de negócio, sem jargão. O que pode acontecer este trimestre se não fizer nada.
2. **Escopo e metodologia** — o que foi testado, o que não, janela, contas.
3. **Achados** — cada um com título, severidade *contextual*, evidência, impacto, reprodução *autorizada e mínima*, remediação, referências (CWE, ASVS, CVE).
4. **Superfície / inventário** — mesmo sem exploit.
5. **Limitações** — WAF, falta de conta admin de teste, tempo.

## Reprodução no relatório

O cliente precisa reproduzir no **ambiente dele**. Isso não é desculpa para publicar exploit genérico na internet. Neste repositório não colamos PoCs; no relatório contratual, descreva passos no alvo autorizado com dados de teste, sem dump de PII.

## Severidade

CVSS + contexto (ver [taxonomias](../fundamentos/taxonomias-mitre-owasp-cwe.md)). Três XSS refletidos não somam um Domain Admin. Agrupe por **cadeia**.

## Tom

Sem humilhar o dev. Sem ameaça. Sem “hackeamos vocês”. Fatos, precondições, correção verificável.

## LGPD e evidência

Minimize. Hash, ID interno, print recortado. Relatório é documento com dado pessoal em potencial — trate como tal.

## Bug bounty

O “relatório” é o ticket da plataforma: título claro, endpoint, impacto, conta de teste. Fora de escopo não envie “de brinde” com PoC agressivo.

## Leitura seguinte

- [Como estudar](../pratica/como-estudar.md)
- Repositório de relatórios públicos (link na coleção de pentest)
