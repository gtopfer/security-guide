# 📋 Modelos e Templates

Templates e arquivos de configuração para diferentes ferramentas OSINT.

## Estrutura

```
modelos/
├── busca_perfis/           # Templates para busca de perfis sociais
├── darkweb/                # Configurações para investigação dark web
├── domains/                # Templates de DNS e domínios
├── metadados/              # Configurações para análise de metadados
└── redes_sociais/          # Templates de redes sociais
```

## Uso

1. Copie o template apropriado para sua investigação
2. Customize com seus parâmetros
3. Use nas ferramentas correspondentes

## Exemplo

```bash
cp modelos/busca_perfis/.env ~/.env
# Edite ~/.env com seus dados
```

## Templates Disponíveis

### Busca de Perfis
- `osint-framework.env` - Configuração para OSINT Framework

### Dark Web
- `onionsearch.env` - Configuração para busca em Tor

### Domínios
- `amass_config.ini` - Configuração para Amass
- `resolvers.txt` - Lista de resolvedores DNS
- `subfinder_config.yaml` - Configuração para Subfinder

### Metadados
- `exiftool_osint.args` - Argumentos para ExifTool
- `metagoofil.env` - Configuração para Metagoofil

### Redes Sociais
- `alvos_sherlock.txt` - Lista de alvos para Sherlock
- `instagram_config.json` - Configuração para Instagram
- `twint_proxy.env` - Proxy para Twint
- `twint.env` - Configuração geral para Twint

---

**Contribuições:** Novos templates são bem-vindos!
