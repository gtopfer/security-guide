# Automação e scripts

Automatizar pipelines permite repetir investigações com confiabilidade. Abaixo descrevo o repositório `osint_stuff_tool_collection` e uma stack mínima em Python (Requests + BeautifulSoup).

## OSINT-Tools (cipher387)

### Visão geral
Repositório gigante mantido por @cipher387 com scripts, listas e coleções categorizadas. Ideal para montar uma wiki interna ou buscar fontes alternativas.

### Instalação
```bash
cd ~/Tools && git clone https://github.com/cipher387/osint_stuff_tool_collection.git
```

### Estrutura e configuração
```bash
cd osint_stuff_tool_collection
ls collections
```
- Cada pasta contém arquivos `.md` com listas curadas. Use `rg` para pesquisar termos específicos.

### Uso avançado
```bash
rg -n "Telegram" collections -g "*.md"
rg -n "Metadata" --files-with-matches collections | xargs -I{} cp {} ~/Projetos/wiki/
```
- Combine arquivos relevantes em um handbook próprio.

### Automação com Makefile
```bash
cp OSINT/scripts/automation/Makefile.osint ~/Tools/osint_stuff_tool_collection/Makefile.osint
cd ~/Tools/osint_stuff_tool_collection
make -f Makefile.osint pull index
```
- O alvo `index` gera índice pesquisável para ferramentas offline e o `pull` mantém o repositório atualizado.

## Python + Requests/BeautifulSoup

### Visão geral
Quando nenhuma ferramenta atende, criar um scraper específico é rápido com Requests + BeautifulSoup. É importante tratar headers, retries e parsing estruturado.

### Ambiente isolado
```bash
python3 -m venv scrapers-venv
source scrapers-venv/bin/activate
pip install --upgrade pip requests beautifulsoup4 httpx tenacity
```

### Script base
```python
#!/usr/bin/env python3
import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_exponential

BASE_URL = "https://exemplo.com/noticias"
OUTPUT = Path("data/noticias.json")

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, min=1, max=60))
def fetch(page: int) -> str:
    resp = requests.get(BASE_URL, params={"page": page}, timeout=15, headers={"User-Agent": "Mozilla"})
    resp.raise_for_status()
    return resp.text

def parse(html: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    resultados = []
    for card in soup.select("article.card"):
        resultados.append({
            "titulo": card.select_one("h2").get_text(strip=True),
            "link": card.select_one("a")['href'],
            "data": card.select_one("time")['datetime'],
        })
    return resultados

def main() -> None:
    tudo = []
    for page in range(1, 6):
        html = fetch(page)
        tudo.extend(parse(html))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(tudo, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

### Execução
```bash
source scrapers-venv/bin/activate
python3 scripts/osint_scraper.py
cat data/noticias.json | jq '.[0:5]'
```

### Boas práticas
- Respeite `robots.txt` e termos de uso.
- Armazene variáveis sensíveis (tokens) em `.env` e use `python-dotenv`.
- Use `mitmproxy`/`burp` para entender APIs antes de codificar o scraper.
