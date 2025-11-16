# Metadados e arquivos

Ferramentas focadas em extrair informações de documentos/imagens. ExifTool e Metagoofil fornecem trilhas de auditoria úteis.

## ExifTool

### Visão detalhada
ExifTool lê e escreve metadados de praticamente qualquer formato. Para OSINT, serve para descobrir GPS, autores, software utilizados e timestamps originais.

### Instalação
```bash
sudo apt install -y libimage-exiftool-perl
mkdir -p data/exif
```

### Configuração
```bash
mkdir -p ~/.config
cp OSINT/templates/metadados/exiftool_osint.args ~/.config/exiftool_osint.args
```
- Ajuste o arquivo caso precise incluir/excluir campos específicos.

### Uso aprofundado
```bash
exiftool -@ ~/.config/exiftool_osint.args evidencias/*.jpg -csv > data/exif/resumo.csv
exiftool -ee -gpslatitude -gpslongitude -n videos/*.mp4 > data/exif/videos_gps.txt
```
- A opção `-ee` extrai metadados embutidos em stream de vídeo.

### Fluxo
1. Rode `sha256sum` nos arquivos originais antes da análise.
2. Use `mapshaper` ou `qgis` para plottar os pontos resultantes.
3. Remova informações sensíveis antes de compartilhar externamente.

## Metagoofil

### Visão detalhada
Metagoofil busca documentos públicos (PDF, DOCX, PPTX) em mecanismos de busca, baixa-os e extrai metadados como autor e software. Excelente para descobrir padrões de e-mail e versões de Office.

### Instalação
```bash
cd ~/Tools && git clone https://github.com/opsdisk/metagoofil.git
cd metagoofil && python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### Configuração
```bash
mkdir -p configs
cp OSINT/templates/metadados/metagoofil.env configs/metagoofil.env
```

### Uso aprofundado
```bash
source venv/bin/activate
source configs/metagoofil.env
python3 metagoofil.py -d "$DOMAIN" -t "$FILETYPES" -n "$RESULTS" -w -o dumps/$DOMAIN
exiftool dumps/$DOMAIN/*.pdf -Creator -Producer -csv > data/metagoofil_autores.csv
```
- Combine com `sort -u` para extrair listas únicas de usuários.

### Fluxo
1. Execute metagoofil com poucos tipos de arquivo para testar.
2. Após baixar documentos, rode `strings`/`yara` para descobrir nomes de servidor.
3. Alimente os autores encontrados em Sherlock/Maigret para procurar perfis.
