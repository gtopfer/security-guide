# Redes sociais – Coleta focal

Aqui estão instruções detalhadas para Twint, Sherlock e Instagram Scraper, cobrindo desde autenticação até encadeamento com outras fases.

## Twint

### Conceito
Twint faz scraping de Twitter/X sem usar a API oficial. Ele aceita filtros por data, geolocalização, idioma, hashtags e exporta em vários formatos.

### Instalação recomendada
```bash
pipx install --force git+https://github.com/twintproject/twint.git
pipx inject twint aiohttp_socks cchardet
```
- O `inject` adiciona pacotes opcionais para lidar com proxies e caracteres especiais.

### Configuração
1. **Variáveis padrão**
    ```bash
    mkdir -p osint_configs
    cp OSINT/templates/redes_sociais/twint.env osint_configs/twint.env
    ```
    - Edite o arquivo copiado com o alvo real, filtros e datas.
2. **Proxy opcional**
    ```bash
    cp OSINT/templates/redes_sociais/twint_proxy.env osint_configs/twint_proxy.env
    ```
    - Exporte com `source osint_configs/twint_proxy.env` antes de rodar se quiser rotear via Tor.

### Uso aprofundado
1. **Busca por perfil + palavra-chave**
    ```bash
    source osint_configs/twint.env
    twint -u "$TW_TARGET" -s "$TW_KEYWORD" --since "$TW_SINCE" --until "$TW_UNTIL" --limit "$TW_LIMIT" \
      -o data/twint_${TW_TARGET}_${TW_KEYWORD}.json --json
    ```
2. **Busca geográfica**
    ```bash
    twint -g "-23.5505,-46.6333,20km" --since "$TW_SINCE" -o data/twint_sp.csv --csv
    ```
3. **Construir grafos**
    ```bash
    twint -u "$TW_TARGET" --followers --user-full -o data/${TW_TARGET}_followers.json --json
    python3 scripts/twint_to_graph.py data/${TW_TARGET}_followers.json data/${TW_TARGET}_graph.gexf
    ```

### Boas práticas
- Rodar com `--database` para gravar direto em SQLite e facilitar consultas SQL.
- Usar `twint -u alvo --resume log.txt` para retomar coletas interrompidas.
- Filtrar resultados com `jq 'select(.language=="pt")'` antes de armazenar.

## Sherlock

### Conceito
Sherlock verifica um username em centenas de plataformas simultaneamente. É ótimo para confirmar identidades encontradas no Twint ou e-mails vazados.

### Instalação
```bash
cd ~/Tools && git clone https://github.com/sherlock-project/sherlock.git
cd sherlock && python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Configuração
```bash
cd ~/Tools/sherlock
cp OSINT/templates/redes_sociais/alvos_sherlock.txt alvos.txt
```
- Você pode editar `sherlock/resources/data.json` para adicionar sites privados ou remover serviços irrelevantes.

### Uso aprofundado
1. **Execução paralela**
    ```bash
    source venv/bin/activate
    python3 sherlock.py -l alvos.txt --print-found --proxy socks5://127.0.0.1:9050 \
      --timeout 15 --folderoutput outputs/$(date +%Y%m%d)
    ```
2. **Exportar apenas URLs válidas**
    ```bash
    find outputs -name "*.txt" -exec grep -Hi "[+]" {} \; | cut -d ' ' -f2 > data/perfis.txt
    ```
3. **Integrar com Recon-ng**
    ```bash
    mkdir -p ~/Tools/recon-ng/rc
    cp OSINT/scripts/recon/import_list.rc ~/Tools/recon-ng/rc/
    cd ~/Tools/recon-ng && ./recon-ng -r rc/import_list.rc
    ```

### Boas práticas
- Defina `--print-all` apenas em ambientes controlados (gera muito log).
- Atualize frequentemente o repositório e execute `python3 -m pytest tests` para validar templates.

## Instagram Scraper

### Conceito
Permite baixar postagens, stories, highlights e comentários de perfis públicos ou autenticados. Ótimo para manter evidências com metadados originais.

### Instalação
```bash
pipx install instagram-scraper
```

### Configuração
```bash
mkdir -p ~/.config/instagram-scraper
cp OSINT/templates/redes_sociais/instagram_config.json ~/.config/instagram-scraper/config.json
```
- Autenticar melhora limites de coleta e evita bloqueios frequentes.

### Uso aprofundado
1. **Baixar todo o feed**
    ```bash
    instagram-scraper persona --maximum 1000 --media-types image,video --comments --metadata-json
    ```
2. **Monitorar hashtags**
    ```bash
    instagram-scraper --tag investigacao --maximum 200 --destination data/hashtag_investigacao
    ```
3. **Comparar diffs**
    ```bash
    cd data/instagram/persona && git init && git add . && git commit -m "snapshot"
    # Após nova coleta
    git status && git diff
    ```

### Boas práticas
- Use `--retry-forever` quando estiver baixando muitos itens.
- Configure `cron` para atualizar automaticamente perfis investigados.
- Armazene hashes (`sha256sum`) dos arquivos baixados para cadeia de custódia.
