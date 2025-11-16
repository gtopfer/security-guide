# Contributing

Obrigado por contribuir com o Security-Guide. Estas instruções ajudam a manter qualidade, segurança e reprodutibilidade.

## Como começar

1. Crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instale dependências (exemplo: OSINT):

```bash
pip install --upgrade pip
pip install -r "Security-Guide/osint-tools-collection/scripts/requirements.txt"
```

3. Rode testes:

```bash
pytest -q
```

## Estilo de código

- Use `black` e `isort` (configuração via `pre-commit` está incluída).
- Execute `pre-commit run --all-files` antes de abrir PR.

## Política de dados sensíveis

- Não comite dados reais de alvos em `data/outputs/` — essa pasta deve ser ignorada pelo repositório.
- Inclua apenas exemplos sanitizados em `data/examples/`.
- Se for necessário compartilhar dados reais, anote autorização e remova/anonimize antes do commit.

## Segurança e uso responsável

- Ferramentas de OSINT e Threat Intelligence podem ter implicações legais e éticas. Execute scripts somente contra alvos que você tem autorização para analisar.
- Documente o propósito e a autorização em issues/PRs quando aplicar estas ferramentas em domínios que não são de teste.

## Pull Requests

- Siga o template de PR (se existir), descreva o problema, as alterações e como testar.
- Para mudanças em scripts de coleta, inclua um exemplo de comando e um arquivo de exemplo em `data/examples/`.

## Licença

Adicione um arquivo `LICENSE` no repositório principal se este projeto for público. Entre em contato com o responsável por propriedade intelectual se houver dúvidas.
