# Guia de operadores de busca do Google (Google Dorks)

> Referência para investigação OSINT com a sintaxe avançada do Google (Google Dorks). Nenhum serviço pago é necessário. Consulte pelo Google, pelo Startpage ou por uma instância SearxNG.

Use estas consultas em alvo autorizado, na sua própria pegada digital ou em fonte pública. Um resultado indexado não autoriza cópia, uso ou acesso ao sistema de terceiro.

## 1. Fundamentos

### Operadores principais

| Operador | Exemplo | Uso |
|----------|---------|-----|
| `"texto exato"` | `"exemplo confidencial"` | Busca a frase literal. |
| `OR` | `phishing OR smishing` | Combina termos alternativos. |
| `-palavra` | `"empresa" -site:linkedin.com` | Exclui o termo ou o host. |
| `site:` | `site:example.com login` | Restringe a consulta ao domínio ou subdomínio. |
| `intitle:` / `inurl:` / `intext:` | `intitle:"index of"` | Limita a busca ao título, à URL ou ao texto. |
| `filetype:` | `filetype:xlsx "financeiro"` | Restringe a extensão do arquivo. |
| `*` | `"senha * reset"` | Substitui um token desconhecido. |
| `..` | `2020..2024 "relatório"` | Define um intervalo numérico. |
| `AROUND(n)` | `"empresa" AROUND(3) "vazamento"` | Exige proximidade entre os termos. |

### Filtros adicionais

- `before:` / `after:` — filtra por data (exemplo: `after:2023-01-01 site:example.com`).
- `cache:URL` — abre o cache sem acessar o site de origem.
- `source:` — restringe o Google News a um veículo.
- `location:` — restringe um Google Alert a uma região, para monitoramento.
- `link:dominio` — lista páginas que apontam para o domínio. A cobertura é parcial.

## 2. Consultas por categoria

Substitua `example.com` e `"empresa"` pelo alvo do escopo. Não use estas consultas para coletar dado de pessoa ou de organização sem autorização.

### 2.1 Infraestrutura e portais

- `intitle:"Apache2 Ubuntu Default Page" "It works!"`
- `intitle:"Index of /" "backup"` — listagem de diretório aberta.
- `"Powered by Jetty" inurl:/webapp`
- `inurl:8080 "Jenkins ver."`
- `intext:"SonarQube" "Log in" -github`

### 2.2 Dados sensíveis e configuração

- `"-----BEGIN PRIVATE KEY-----" site:example.com`
- `"AWS_SECRET_ACCESS_KEY" filetype:env`
- `"sql dump" filetype:sql "INSERT INTO"`
- `"confidential" filetype:pptx site:sharepoint.com`
- `"password" ext:ini | ext:cfg "user="`

### 2.3 Dispositivos e IoT

- `inurl:view/view.shtml "Live View / - AXIS"`
- `intitle:"Shenzhen" "IP Camera"`
- `"Server Status" "Uptime" "goform"`
- `"RouterOS v6" inurl:webfig/`

### 2.4 Pessoas, RH e governança

- `"currículo" filetype:pdf "empresa"`
- `"lista de presença" site:example.com filetype:xls`
- `"organograma" site:example.com filetype:ppt`
- `"CIPE" "ata" site:gov.br filetype:pdf`

### 2.5 SaaS e colaboração

- `"public dashboard" "tableau"`
- `site:figma.com "empresa" "shared"`
- `site:miro.com "roadmap" "empresa"`
- `site:linear.app "public issue"`
- `site:atlassian.net "confluence" "PUBLIC"`

### 2.6 Código e repositórios

- `site:github.com "empresa" "confidential"`
- `site:gitlab.com "token" "empresa"`
- `"access_key" "aws" filetype:json`
- `"apiKey" "AIza" ext:txt`

### 2.7 Exposição e configuração pública

- `"index of /admin"` + `("login"|"panel")`
- `"phpinfo()" "PHP Version"`
- `"Directory listing for /"` + `site:example.com`
- `"Error" "Warning" "Notice" filetype:log`

### 2.8 Armazenamento em nuvem exposto

- `site:s3.amazonaws.com "empresa"`
- `site:storage.googleapis.com "confidencial" OR "backup"`
- `site:blob.core.windows.net filetype:pdf OR filetype:xlsx`
- `intitle:"index of" "s3.amazonaws.com"`
- `"bucket" "empresa" filetype:json inurl:s3`

> Mantenha um catálogo local (`docs/dorks.md`) com as colunas `categoria`, `dork` e `contexto`.

## 3. Combinação de operadores

A consulta útil combina operadores. Os padrões abaixo são modelos. Troque o domínio pelo alvo autorizado.

### Credencial em código público

```
(site:github.com OR site:gitlab.com) ("password" OR "passwd" OR "secret") filetype:env OR filetype:yml
```

### Painel administrativo sem página de login visível

```
intitle:"admin" (inurl:/admin | inurl:/dashboard | inurl:/panel) -"login" -"password"
```

### Documento interno em serviço de nuvem pública

```
(site:docs.google.com OR site:drive.google.com OR site:sharepoint.com) "confidencial" OR "interno" "empresa"
```

### Câmera e IoT com interface web publicada

```
(intitle:"webcam" OR intitle:"camera" OR inurl:"/view/viewer_index.shtml") -"login" -"password required"
```

### Software conhecido em host do escopo

```
"phpMyAdmin" inurl:/phpmyadmin -"phpMyAdmin is more fun" site:example.com
"Jenkins" inurl:":8080" "Dashboard [Jenkins]" -site:jenkins.io
```

### Cópia de segurança e arquivo esquecido

```
site:example.com (ext:bak | ext:old | ext:backup | ext:sql | ext:dump) -github
```

### Bucket de armazenamento com nome da organização

```
(site:s3.amazonaws.com OR site:storage.googleapis.com OR site:blob.core.windows.net) "empresa" (filetype:pdf | filetype:sql | filetype:env)
```

> Registre a consulta que produziu um achado em `data/dorks/library.md`, por categoria. Reutilize o registro no próximo trabalho autorizado.

## 4. Roteiros de consulta

### 4.1 Reconhecimento inicial

1. `"<nome empresa>" OR "<sigla empresa>"`
2. `site:example.com -www` (localiza subdomínio)
3. `site:*.example.com filetype:pdf OR filetype:xls`
4. `site:github.com "<empresa>" "password"`

### 4.2 Infraestrutura e aplicação

1. `site:example.com intitle:"Index of /"`
2. `site:example.com filetype:xml "config"`
3. `inurl:example.com "JSESSIONID"`
4. `site:example.com ext:bak | ext:old`

### 4.3 Dado sensível publicado

1. `site:docs.google.com "empresa" -site:docs.google.com/spreadsheets`
2. `site:drive.google.com "confidencial"`
3. `"googleusercontent.com" "empresa" "download"`
4. `site:onedrive.live.com "empresa"`

Registre a saída relevante em `data/dorks/<empresa>.md`.

## 5. Apoio e automação

Não automatize consulta em massa contra o Google. Use SearxNG ou Startpage quando o volume aumenta.

### 5.1 Script SearxNG

```bash
#!/usr/bin/env bash
SEARX_URL="https://searx.local/search"
QUERY=${1:? Informe o dork}
curl -G --data-urlencode "q=${QUERY}" --data "format=json" "$SEARX_URL" | jq '.results[] | {title, url}'
```

### 5.2 Makefile

```makefile
DORK?=site:example.com filetype:pdf
dork:
	./scripts/dork_query.sh "$(DORK)"
```

### 5.3 Lista de verificação

- [ ] Defina a lista inicial de consultas, por categoria.
- [ ] Registre o objetivo de cada consulta (exemplo: `infra`, `dados`, `identity`).
- [ ] Valide um achado sensível em ambiente controlado antes de ampliar a busca.
- [ ] Remova dado pessoal de captura de tela e de link antes de compartilhar.
- [ ] Atualize o catálogo ao fim do trabalho.

## 6. Prática e limites legais

- Respeite a lei e os termos de uso. A consulta em um índice público não é, por si, invasão de sistema. Publicar ou explorar um achado pode ser ilegal.
- Evite automação direta contra o Google. Use SearxNG ou Startpage para reduzir bloqueio.
- Use uma janela privativa ou um perfil sem histórico. Isso reduz a personalização do resultado.
- Varie o User-Agent e o idioma quando você precisa comparar conjuntos de resultados.
- Salve a evidência com a consulta, o horário e a URL. Esse registro permite repetir a busca.

## 7. Referências

- [Exploit-DB Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- [OSINT Framework – Google Search](https://osintframework.com/)
- [SearxNG](https://github.com/searxng/searxng) — metabuscador de código aberto para executar a consulta sem depender só do Google.

> Mantenha um repositório próprio de consultas, com controle de versão. Revise o catálogo e retire resultado duplicado ou obsoleto.
