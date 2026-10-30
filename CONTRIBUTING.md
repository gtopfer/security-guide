# Contribuindo com o Security Guide

Este guia é mantido pela comunidade. Uma contribuição útil indica uma ferramenta nova, corrige um dado desatualizado ou torna um texto mais claro.

## Como contribuir

1. Abra uma **issue** e descreva a mudança. Para uma correção pequena e evidente (erro de digitação ou link quebrado), abra um **pull request** direto.
2. Faça um fork do repositório. Crie um branch com nome descritivo (`fix/link-quebrado`, `feat/nova-ferramenta-x`).
3. No pull request, explique o motivo da mudança.

## Adicionar uma ferramenta (OSINT ou pentest)

Uma ferramenta nova em `osint-tools-collection/README.md` ou em `pentest-tools-collection/README.md` segue os critérios de curadoria:

- A licença é permissiva (GPL, MIT, Apache ou equivalente) e o código-fonte é auditável.
- A instalação usa `git clone`, `pip`, `poetry`, `npm`, `cargo`, `go install` ou uma imagem Docker pública. Não exija um portal proprietário.
- A execução local é possível. Uma API externa pode ser opcional.
- O projeto tem manutenção recente (commit, release ou issue). Não sugira um repositório abandonado há anos.

Na linha da tabela, inclua o nome, o link do repositório, a stack ou o uso principal, e uma descrição curta.

## Reportar um link quebrado ou uma ferramenta desatualizada

Abra uma issue com o link do repositório. Se você conhece uma alternativa mantida, inclua o link dela.

Uma ferramenta sem atividade recente, mas ainda funcional, permanece na tabela com a marca **manutenção irregular**. Não remova essa linha só pela falta de commits novos.

Substitua ou remova a linha quando o link retorna 404.

## Estilo

- Escreva em **português do Brasil** (pt-BR).
- Use frases curtas. Prefira um exemplo concreto a um parágrafo longo.
- Coloque links de repositório entre `<angle brackets>` no Markdown.
- Antes de enviar uma lista grande, verifique os links (ferramenta ou teste manual).

## Estudos de segurança ofensiva (`offensive-security/`)

Um texto novo nesta pasta deve:

- Permanecer em **pt-BR**.
- Explicar o conceito: o que é, o que estudar e o que ler.
- Apontar para um laboratório oficial e para a fonte primária (OWASP, MITRE, RFC, documentação do fornecedor).
- **Não** incluir payload, exploit, prova de conceito, dump de prova ou procedimento para reproduzir um ataque.

## Engenharia social (`social-engineering/`)

A pasta tem duas trilhas.

- **Defesa** (arquivos na raiz da pasta): o que a pessoa vê, qual sinal observar e qual ação tomar.
- **Estudos ofensivos** (`social-engineering/estudos-ofensivos/`): autorização, fase, vetor e limite de reporte. O texto nomeia o conceito. O texto não ensina a executar o contato.

Um texto novo nesta pasta deve:

- Permanecer em **pt-BR**.
- Na defesa, explicar o conceito e a ação.
- Nos estudos ofensivos, explicar a fase, o vetor e a autorização. Não ensinar a montar a tentativa.
- Apontar para a fonte primária (CERT.br, NIST, CISA, MITRE, RFC). Na defesa, aponte para o playbook já existente. Não duplique o playbook.
- **Não** incluir roteiro de ataque, passo a passo de campanha, modelo de mensagem, texto de isca, kit de phishing, script, payload, configuração de ferramenta de campanha nem dado de exercício (alvo, resultado ou prova de cliente).

Essa proibição vale para as duas trilhas.

## Código de conduta

O texto completo está no [Código de Conduta](CODE_OF_CONDUCT.md).

Trate as pessoas com respeito. Este espaço cobre segurança defensiva, OSINT ético e estudo ofensivo **autorizado**.

O repositório recusa conteúdo para atividade ilegal. Isso inclui ataque sem autorização e invasão de conta de terceiro.
