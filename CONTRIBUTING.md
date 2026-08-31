# Contribuindo com o Security Guide

Obrigado por querer contribuir! Este guia é mantido pela comunidade e depende de gente apontando ferramentas novas, corrigindo informações desatualizadas e melhorando a didática dos textos.

## Como contribuir

1. Abra uma **Issue** descrevendo o que você quer mudar/adicionar, ou vá direto para um **Pull Request** se a mudança for pequena e óbvia (typo, link quebrado, etc.).
2. Faça um fork do repositório e crie uma branch descritiva (`fix/link-quebrado`, `feat/nova-ferramenta-x`).
3. Abra o PR explicando o motivo da mudança.

## Adicionando uma ferramenta OSINT

Toda ferramenta sugerida para `osint-tools-collection/README.md` precisa seguir os [Critérios de Curadoria](osint-tools-collection/README.md#-critérios-de-curadoria):

- Licença permissiva (GPL, MIT, Apache etc.) e código-fonte auditável.
- Instalação via `git clone`, `pip`, `poetry`, `npm`, `cargo`, `go install` ou Docker público — **sem** portal proprietário obrigatório.
- Execução local possível (mesmo que aceite APIs externas opcionais).
- Projeto ativo (commits/releases/issues recentes) — evite sugerir repositórios abandonados há anos.

Ao adicionar uma linha na tabela, inclua: nome, link do repositório, stack/uso principal e uma descrição curta e direta.

## Reportando link quebrado ou ferramenta desatualizada

Abra uma Issue com o link do repositório afetado e, se souber, uma alternativa mantida. Ferramentas sem atividade recente mas ainda funcionais são marcadas com ⚠️ na tabela em vez de removidas — a menos que o link esteja de fato quebrado (404), caso em que devem ser substituídas ou removidas.

## Estilo

- O conteúdo é em **português** (pt-BR).
- Prefira frases curtas e exemplos práticos a explicações longas.
- Links de repositórios sempre entre `<angle brackets>` no Markdown.
- Rode um verificador de links (ou teste manualmente) antes de submeter uma lista grande de ferramentas novas.

## Código de conduta

Seja respeitoso. Este é um espaço para aprendizado sobre segurança defensiva e OSINT ético — conteúdo voltado a atividades ilegais (ataques não autorizados, invasão de contas de terceiros, etc.) não será aceito.
