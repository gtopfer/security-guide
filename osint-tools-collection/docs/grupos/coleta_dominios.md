# Coleta de domínios e superfície exposta

Combinar fontes passivas (CRT.sh, APIs de parceiros) com bruteforce DNS garante cobertura ampla. Abaixo há um fluxo detalhado para `crt.sh`, `subfinder`, `amass`, `assetfinder` e `massdns`.

## CRT.sh (consulta a certificados)

### Função
CRT.sh indexa certificados emitidos publicamente. Ao consultar `%.dominio`, é possível descobrir subdomínios que apareceram em certificados TLS. O serviço não exige API key e pode ser consultado via HTTP.

### Script recomendado
1. Copie o script versionado em `OSINT/scripts/domains/crtsh.sh` para o diretório onde mantém suas ferramentas.
    ```bash
    mkdir -p ~/Tools/osint
    cp OSINT/scripts/domains/crtsh.sh ~/Tools/osint/crtsh.sh
    chmod +x ~/Tools/osint/crtsh.sh
    ```
2. Exporte `CRTSH_DOMAIN` ou passe o domínio como parâmetro.
- O script depende de `curl` e `jq` para parsear o JSON retornado.

### Uso rico em detalhes
```bash
cd ~/Tools/osint
./crtsh.sh empresa.com | tee data/crtsh_empresa.txt
./crtsh.sh empresa.com | sed 's/\*\.//g' | awk -F '.' '{print $(NF-1)"."$NF}' | sort -u > data/crtsh_rootdomains.txt
```
- O primeiro comando salva todos os subdomínios.
- O segundo reduz a lista apenas a domínios raiz para pivotar em Whois.

## subfinder

### Função
Subfinder (ProjectDiscovery) consulta dezenas de APIs e fontes públicas. Excelente primeira camada antes de scans ativos.

### Instalação
```bash
sudo apt install -y golang
GO111MODULE=on go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```
- Adicione `~/go/bin` ao `PATH`.

### Configuração
```bash
mkdir -p ~/.config/subfinder
cp OSINT/templates/domains/subfinder_config.yaml ~/.config/subfinder/config.yaml
chmod 600 ~/.config/subfinder/config.yaml
```
- Edite o arquivo copiado para adicionar/ajustar as chaves das fontes que você realmente tem disponível.

### Uso aprofundado
```bash
subfinder -d empresa.com -o data/subfinder_empresa.txt -silent -all
httpx -l data/subfinder_empresa.txt -title -status-code -tech-detect -o data/httpx_empresa.txt
```
- O arquivo `httpx` resultante serve para alimentar `nmap` focado.

## amass

### Função
Amass combina fontes passivas e ativas (bruteforce, resolvers, ASN). Ideal para inventário completo.

### Instalação
```bash
sudo snap install amass
```

### Configuração
```bash
mkdir -p ~/.config/amass
cp OSINT/templates/domains/amass_config.ini ~/.config/amass/config.ini
```
- Ajuste flags como `active` ou resolvers conforme o escopo autorizado do projeto.

### Uso aprofundado
```bash
amass enum -config ~/.config/amass/config.ini -d empresa.com -o data/amass_empresa.txt
amass viz -d empresa.com -o graphs/amass_empresa.gv
```
- `viz` gera grafos Graphviz para visualizar relacionamentos entre subdomínios e IPs.

## assetfinder

### Função
Assetfinder cruza certificados, ASN e APIs como SecurityTrails para achar domínios relacionados.

### Instalação
```bash
GO111MODULE=on go install github.com/tomnomnom/assetfinder@latest
```

### Uso detalhado
```bash
assetfinder --subs-only empresa.com | tee data/assetfinder_empresa.txt
comm -12 <(sort data/assetfinder_empresa.txt) <(sort data/crtsh_empresa.txt) > data/subs_confirmados.txt
```
- O `comm` ajuda a validar quais domínios apareceram em múltiplas fontes.

## massdns

### Função
massdns é um resolvedor em massa extremamente rápido. Ele verifica listas gigantes de subdomínios contra resolvers personalizados.

### Instalação
```bash
cd ~/Tools && git clone https://github.com/blechschmidt/massdns.git
cd massdns && make && sudo cp bin/massdns /usr/local/bin/
```

### Configuração e uso
```bash
mkdir -p data
cp OSINT/templates/domains/resolvers.txt data/resolvers.txt
wordlist=subs-top1m.txt
massdns -r data/resolvers.txt -t A -o S -w data/massdns_empresa.txt $wordlist
awk '{print $1}' data/massdns_empresa.txt | sed 's/.$//' > data/massdns_subs.txt
```
- Use `sed 's/.$//'` para remover o ponto final que o massdns adiciona.

## Encadeamento sugerido
1. Execute `crtsh`, `subfinder`, `assetfinder` e `amass` em paralelo.
2. Una tudo em `cat data/*empresa*.txt | sort -u > data/todos_subs.txt`.
3. Use `massdns` para validar resolução.
4. Somente após validar IPs, rode `nmap`/`httpx`.
