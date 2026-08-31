# Google Dorking Field Guide

> Referência prática para investigações OSINT usando apenas sintaxe avançada do Google (a.k.a. Google Dorks). Nenhum serviço pago é necessário; explore via Google, Startpage ou instâncias SearxNG.

## 1. Fundamentos do Dorking

### Operadores Essenciais
| Operador | Exemplo | Uso |
|----------|---------|-----|
| `"texto exato"` | `"exemplo confidencial"` | Frase literal. |
| `OR` | `phishing OR smishing` | Combina termos. |
| `-palavra` | `"empresa" -site:linkedin.com` | Exclui termos/hosts. |
| `site:` | `site:example.com login` | Restringe domínio/subdomínio. |
| `intitle:` / `inurl:` / `intext:` | `intitle:"index of"` | Limita área da página. |
| `filetype:` | `filetype:xlsx "financeiro"` | Restringe extensão. |
| `*` | `"senha * reset"` | Coringa para token desconhecido. |
| `..` | `2020..2024 "relatório"` | Intervalo numérico. |
| `AROUND(n)` | `"empresa" AROUND(3) "vazamento"` | Proximidade entre termos. |

### Filtros Avançados
- `before:` / `after:` — filtra por data (ex.: `after:2023-01-01 site:example.com`).
- `cache:URL` — visualizar cache sem acessar site original.
- `source:` — Google News por veículo.
- `location:` — Google Alerts restrito a regiões (para monitoramento).
- `link:dominio` — páginas que apontam para o domínio (ainda parcial).

## 2. Dorks por Categoria

### 2.1 Infraestrutura e Portais
- `intitle:"Apache2 Ubuntu Default Page" "It works!"`
- `intitle:"Index of /" "backup"` — listagens abertas.
- `"Powered by Jetty" inurl:/webapp`
- `inurl:8080 "Jenkins ver."`
- `intext:"SonarQube" "Log in" -github`

### 2.2 Dados Sensíveis e Configurações
- `"-----BEGIN PRIVATE KEY-----" site:example.com`
- `"AWS_SECRET_ACCESS_KEY" filetype:env`
- `"sql dump" filetype:sql "INSERT INTO"`
- `"confidential" filetype:pptx site:sharepoint.com`
- `"password" ext:ini | ext:cfg "user="`

### 2.3 Dispositivos & IoT
- `inurl:view/view.shtml "Live View / - AXIS"`
- `intitle:"Shenzhen" "IP Camera"`
- `"Server Status" "Uptime" "goform"`
- `"RouterOS v6" inurl:webfig/`

### 2.4 Pessoas, RH e Governança
- `"currículo" filetype:pdf "empresa"`
- `"lista de presença" site:example.com filetype:xls`
- `"organograma" site:example.com filetype:ppt`
- `"CIPE" "ata" site:gov.br filetype:pdf`

### 2.5 SaaS & Colaboração
- `"public dashboard" "tableau"`
- `site:figma.com "empresa" "shared"`
- `site:miro.com "roadmap" "empresa"`
- `site:linear.app "public issue"`
- `site:atlassian.net "confluence" "PUBLIC"`

### 2.6 Código & Repositórios
- `site:github.com "empresa" "confidential"`
- `site:gitlab.com "token" "empresa"`
- `"access_key" "aws" filetype:json`
- `"apiKey" "AIza" ext:txt`

### 2.7 Busca por Vulnerabilidades Públicas
- `"index of /admin"` + `("login"|"panel")`
- `"phpinfo()" "PHP Version"`
- `"Directory listing for /"` + `site:example.com`
- `"Error" "Warning" "Notice" filetype:log`

### 2.8 Cloud Storage Exposto
- `site:s3.amazonaws.com "empresa"`
- `site:storage.googleapis.com "confidencial" OR "backup"`
- `site:blob.core.windows.net filetype:pdf OR filetype:xlsx`
- `intitle:"index of" "s3.amazonaws.com"`
- `"bucket" "empresa" filetype:json inurl:s3`

> Mantenha um catálogo local (`docs/dorks.md`) com colunas `categoria`, `dork`, `contexto`.

## 3. Combinações Avançadas de Operadores

A força do dorking está em combinar operadores. Exemplos de padrões de alta eficácia:

### Exposição de credenciais em código
```
(site:github.com OR site:gitlab.com) ("password" OR "passwd" OR "secret") filetype:env OR filetype:yml
```

### Painéis administrativos sem autenticação
```
intitle:"admin" (inurl:/admin | inurl:/dashboard | inurl:/panel) -"login" -"password"
```

### Documentos internos em serviços de nuvem pública
```
(site:docs.google.com OR site:drive.google.com OR site:sharepoint.com) "confidencial" OR "interno" "empresa"
```

### Câmeras e IoT com interface web exposta
```
(intitle:"webcam" OR intitle:"camera" OR inurl:"/view/viewer_index.shtml") -"login" -"password required"
```

### CVEs e vulnerabilidades conhecidas por software
```
"phpMyAdmin" inurl:/phpmyadmin -"phpMyAdmin is more fun" site:example.com
"Jenkins" inurl:":8080" "Dashboard [Jenkins]" -site:jenkins.io
```

### Backups e arquivos esquecidos em servidores
```
site:example.com (ext:bak | ext:old | ext:backup | ext:sql | ext:dump) -github
```

### Buckets de cloud storage mal configurados
```
(site:s3.amazonaws.com OR site:storage.googleapis.com OR site:blob.core.windows.net) "empresa" (filetype:pdf | filetype:sql | filetype:env)
```

> Dica: salve combinações eficazes em `data/dorks/library.md` por categoria para reutilizar em engajamentos futuros.

## 4. Playbooks de Dorking

### 4.1 Recon Basic
1. `"<nome empresa>" OR "<sigla empresa>"`
2. `site:example.com -www` (descobrir subdomínios)
3. `site:*.example.com filetype:pdf OR filetype:xls`
4. `site:github.com "<empresa>" "password"`

### 4.2 Infra & Apps
1. `site:example.com intitle:"Index of /"`
2. `site:example.com filetype:xml "config"`
3. `inurl:example.com "JSESSIONID"`
4. `site:example.com ext:bak | ext:old`

### 4.3 Dados Sensíveis
1. `site:docs.google.com "empresa" -site:docs.google.com/spreadsheets`
2. `site:drive.google.com "confidencial"`
3. `"googleusercontent.com" "empresa" "download"`
4. `site:onedrive.live.com "empresa"`

Documente saídas relevantes em `data/dorks/<empresa>.md`.

## 5. Automação & Ferramentas de Apoio

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

### 5.3 Checklist
- [ ] Definir lista inicial de dorks (por categoria).
- [ ] Registrar objetivo por consulta (ex.: `infra`, `dados`, `identity`).
- [ ] Validar achados sensíveis em ambiente controlado antes de escalar.
- [ ] Sanitizar prints/links antes de compartilhar.
- [ ] Atualizar catálogo pós-engajamento.

## 6. Boas Práticas e Ética
- Respeite legislação/ToS — dorking não é intrusão, mas divulgar/explorar achados pode ser ilegal.
- Evite automação direta contra Google: use SearxNG/Startpage para reduzir bloqueios.
- Utilize perfis limpos/private windows para minimizar personalização.
- Rotacione User-Agent/Idioma para obter resultados distintos.
- Salve evidências com contexto (query, timestamp, URL) para reprodutibilidade.

## 7. Referências Extras
- [Exploit-DB Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- [OSINT Framework – Google Search](https://osintframework.com/)
- [SearxNG](https://github.com/searxng/searxng) – metabuscador open source para rodar dorks sem depender direto do Google.

> Continuidade: mantenha um repositório próprio de dorks versionado e revise periodicamente para retirar resultados duplicados ou obsoletos.
