# Relatório e comunicação

O entregável do pentest não é a shell. É o **texto que o time consegue corrigir**. Relatórios públicos de consultoria, listados na [coleção de pentest](../../pentest-tools-collection/README.md), mostram tom e estrutura.

## Estrutura que funciona

1. **Sumário executivo** — risco em linguagem de negócio, sem jargão. O que pode ocorrer neste trimestre se nada for feito.
2. **Escopo e método** — o que foi testado, o que não foi, a janela e as contas.
3. **Achados** — cada um com título, severidade contextual, evidência, impacto, reprodução autorizada e mínima, correção e referência (CWE, ASVS, CVE).
4. **Superfície e inventário** — mesmo sem exploit.
5. **Limitações** — WAF, falta de conta de administrador de teste, tempo.

## Reprodução no relatório

O cliente precisa repetir o teste no **ambiente dele**. Isso não autoriza publicar um exploit genérico na internet. Este repositório não cola prova de conceito. No relatório contratual, descreva os passos no alvo autorizado, com dado de teste, sem dump de dado pessoal.

## Severidade

Use CVSS mais contexto. Veja [taxonomias](../fundamentos/taxonomias-mitre-owasp-cwe.md). Três XSS refletidos não equivalem a um Domain Admin. Agrupe por **cadeia**.

## Tom

Não humilhe quem desenvolve. Não ameace. Não escreva "invadimos vocês". Escreva fato, pré-condição e correção verificável.

## LGPD e evidência

Minimize. Use hash, identificador interno e captura recortada. O relatório pode conter dado pessoal. Trate-o como tal.

## Bug bounty

O relatório é o ticket da plataforma: título claro, endpoint, impacto e conta de teste. Não envie um item fora de escopo com prova de conceito agressiva.

## Leitura seguinte

- [Como estudar](../pratica/como-estudar.md)
- Repositório de relatórios públicos (link na coleção de pentest)
