# 🚀 Quick Start - Comece Aqui!

Bem-vindo à **Coleção de Ferramentas OSINT**! Este é o guia mais rápido para começar.

## ⚡ 5 Minutos para Começar

### 1️⃣ Entenda o Projeto (1 min)

```
Este é um repositório com 200+ ferramentas OSINT organizadas em 11 categorias:

Buscas → Redes Sociais → Pessoas → Email → Domínios → Imagens 
→ Análise → Mapas → Notícias → Ameaças → Privacidade

Tudo em PORTUGUÊS! 🇧🇷
```

### 2️⃣ Explore as Categorias (2 min)

| Categoria | Abra | Exemplos |
|-----------|------|----------|
| 🔎 Buscas Gerais | [00_buscas_gerais/README.md](./00_buscas_gerais/README.md) | Google, Bing, Shodan |
| 📱 Redes Sociais | [01_redes_sociais/README.md](./01_redes_sociais/README.md) | Twitter, Instagram, LinkedIn |
| 👥 Pessoas | [02_busca_pessoas/README.md](./02_busca_pessoas/README.md) | FaceCheck, genealogia |
| 📧 Email/Telefone | [03_email_telefone/README.md](./03_email_telefone/README.md) | HIBP, PhoneInfoga |
| 🌐 Domínio/IP | [04_dominio_ip/README.md](./04_dominio_ip/README.md) | WHOIS, DNS, CRT.sh |
| 🖼️ Imagens | [05_busca_imagens/README.md](./05_busca_imagens/README.md) | TinEye, PimEyes |
| 📸 Análise | [06_analise_imagens/README.md](./06_analise_imagens/README.md) | EXIF, Forensia |
| 🗺️ Mapas | [07_geoespacial_mapas/README.md](./07_geoespacial_mapas/README.md) | Google Maps, satélite |
| 📰 Notícias | [08_noticias_dados/README.md](./08_noticias_dados/README.md) | Google News, RSS |
| 🎯 Ameaças | [09_threat_intelligence/README.md](./09_threat_intelligence/README.md) | Malware, APT |
| 🔒 Privacidade | [10_privacidade_seguranca/README.md](./10_privacidade_seguranca/README.md) | VPN, criptografia |

### 3️⃣ Escolha Seu Caminho (2 min)

```
❌ "Quero uma ferramenta rápida"
   → Escolha uma categoria acima
   → Procure a ferramenta
   → Clique no link

✅ "Quero automatizar com scripts"
   → Vá para ferramentas/README.md
   → Instale requirements.txt
   → Copie .env.example para .env
   → Execute osint_collector.py

✅ "Quero aprender metodologia"
   → Leia docs/INDICE.md
   → Escolha um playbook
   → Siga o checklist
```

---

## 📚 Guias Essenciais

### Se Você É Iniciante
```
1. Leia: docs/INDICE.md
2. Escolha: Uma categoria
3. Aprenda: Os guias em docs/grupos/
4. Pratique: Com as ferramentas
```

### Se Você Quer Programar
```
1. Leia: ferramentas/README.md
2. Instale: pip install -r ferramentas/requirements.txt
3. Configure: cp .env.example .env
4. Execute: python ferramentas/coletores/osint_collector.py --help
```

### Se Você Quer Investigar Algo Específico
```
Pessoa? → 02_busca_pessoas/ + 03_email_telefone/
Website? → 04_dominio_ip/ + 08_noticias_dados/
Malware? → 09_threat_intelligence/
Redes Sociais? → 01_redes_sociais/
Imagens? → 05_busca_imagens/ + 06_analise_imagens/
Localização? → 07_geoespacial_mapas/
```

---

## 🎯 Seus Primeiros Passos

### Opção A: Exploração Rápida (5 min)
```bash
# 1. Entre no repo
cd osint-tools-collection

# 2. Abra um README de categoria
cat 01_redes_sociais/README.md

# 3. Escolha uma ferramenta
# 4. Visite o URL dela
# 5. Pronto!
```

### Opção B: Aprender Metodologia (15 min)
```bash
# 1. Entre no repo
cd osint-tools-collection

# 2. Leia o índice
cat docs/INDICE.md

# 3. Escolha um playbook
cat docs/grupos/busca_perfis.md

# 4. Siga o checklist
```

### Opção C: Usar Scripts (20 min)
```bash
# 1. Clone/entre no repo
cd osint-tools-collection

# 2. Crie ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instale dependências
pip install -r ferramentas/requirements.txt

# 4. Configure
cp .env.example .env
# Edite .env com suas credenciais

# 5. Execute
python ferramentas/coletores/osint_collector.py --target example.com --output data/outputs/
```

---

## 📖 Documentação

| Arquivo | O que faz |
|---------|-----------|
| **README.md** | Visão geral do projeto |
| **ESTRUTURA.md** | Visualização da estrutura |
| **REORGANIZACAO.md** | O que foi mudado |
| **docs/INDICE.md** | Índice de tudo |
| **docs/metodologia.md** | Como investigar corretamente |
| **ferramentas/README.md** | Como usar scripts |

---

## 💡 Dicas Importantes

### 🔍 Encontrando Ferramentas
```
Não sabe qual ferramenta usar?
1. Abra a categoria relevante (ex: 04_dominio_ip/README.md)
2. Procure por Ctrl+F
3. Leia a descrição
4. Clique no URL
```

### 🛠️ Usando Scripts
```
1. Vá para ferramentas/
2. Instale requirements.txt
3. Crie um .env
4. Execute o script desejado
5. Resultados em data/outputs/
```

### 📚 Aprendendo
```
1. Comece em docs/INDICE.md
2. Siga um playbook (ex: busca_perfis.md)
3. Use as ferramentas sugeridas
4. Crie seu próprio fluxo
```

---

## 🤔 Perguntas Comuns

### P: Qual ferramenta devo usar para [X]?
**R:** Abra a categoria apropriada e use Ctrl+F para buscar.

### P: Como instalo as dependências?
**R:** 
```bash
pip install -r ferramentas/requirements.txt
```

### P: Como crio um .env?
**R:**
```bash
cp .env.example .env
# Edite com suas credenciais
```

### P: Os scripts funcionam em Windows?
**R:** Sim! Python é cross-platform. WSL recomendado para melhor experiência.

### P: Quais ferramentas são gratuitas?
**R:** Quase todas! Algumas têm planos freemium. Veja a descrição de cada uma.

---

## 🚀 Próximas Ações

- [ ] Leia [README.md](./README.md) completo
- [ ] Explore [docs/INDICE.md](./docs/INDICE.md)
- [ ] Escolha uma categoria para explorar
- [ ] Se programador: instale [ferramentas/requirements.txt](./ferramentas/requirements.txt)
- [ ] Contribua com novas ferramentas/documentação!

---

## 📞 Precisa de Ajuda?

1. **Consulte a documentação** em `docs/`
2. **Veja exemplos** em `dados/examples/`
3. **Abra uma Issue** no GitHub
4. **Leia o arquivo apropriado** para sua necessidade

---

**🎉 Bem-vindo! Comece a explorar agora!**

Próximo passo recomendado: → [docs/INDICE.md](./docs/INDICE.md)
