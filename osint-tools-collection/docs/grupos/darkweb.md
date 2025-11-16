# Dark web / deep web

Guia detalhado para operar Tor Browser, Ahmia e OnionSearch de forma segura.

## Tor Browser

### Função
Fornece navegador endurecido (base Firefox ESR) com Tor integrado. Essencial para acessar serviços `.onion` e proteger identidade.

### Instalação
```bash
sudo apt install -y torbrowser-launcher
```

### Configuração
```bash
torbrowser-launcher --settings
```
- Ajuste idioma, diretório e configure bridges se necessário.

### Uso aprofundado
```bash
torbrowser-launcher
```
- A primeira execução baixa a imagem oficial e verifica assinaturas GPG.
- Use perfis diferentes para cada investigação (Menu -> Profiles -> Create).

### Boas práticas
- Desabilite plugins/JS extras.
- Use VPN corporativa antes de abrir o Tor quando a política exigir.
- Nunca faça login em contas pessoais no mesmo perfil Tor.

## Ahmia

### Função
Motor open source que indexa serviços `.onion`. Pode ser instalado localmente para criar mirror ou rodar crawlers privados.

### Instalação detalhada
```bash
cd ~/Tools && git clone https://github.com/ahmia/ahmia-site.git
cd ahmia-site && python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp ahmia/example.env ahmia/.env
```

### Configuração
```bash
source venv/bin/activate
python manage.py migrate
python manage.py collectstatic
```
- Configure o `.env` com credenciais do PostgreSQL/Elasticsearch se estiver usando produção; para dev, SQLite já funciona.

### Uso aprofundado
```bash
python manage.py runserver 127.0.0.1:8001
# acessar http://127.0.0.1:8001 e buscar palavras-chave
```
- Para tornar rastreável via Tor, publique atrás de um serviço onion configurando `HiddenServicePort` no `torrc`.

## OnionSearch (OnionSearchEngine)

### Função
CLI em Python para consultar múltiplos motores onion (Ahmia, Phobos, Recon, etc.) sem abrir navegador.

### Instalação
```bash
pipx install git+https://github.com/megadose/OnionSearch.git
```

### Configuração
```bash
mkdir -p osint_configs
cp OSINT/templates/darkweb/onionsearch.env osint_configs/onionsearch.env
```
- Edite o arquivo copiado com consulta/detalhes desejados antes de executar.

### Uso aprofundado
```bash
source osint_configs/onionsearch.env
TOR_PROXY=socks5://127.0.0.1:9050 onionsearch -q "$ONIONSEARCH_QUERY" --depth "$ONIONSEARCH_DEPTH" \
  --metadata --json -o data/onionsearch_${ONIONSEARCH_QUERY}.json
jq '.[].url' data/onionsearch_${ONIONSEARCH_QUERY}.json
```
- Use `--raw` para salvar HTML e processar depois com `ripgrep`/`jq`.

### Fluxo
1. Rode OnionSearch periodicamente e registre URLs novos.
2. Valide URLs manualmente no Tor Browser (com JavaScript desabilitado).
3. Caso precise indexar, configure instância Ahmia + crawler dedicado.
