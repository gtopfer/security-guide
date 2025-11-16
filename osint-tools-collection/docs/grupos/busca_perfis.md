# Busca em sites, pessoas e perfis

Esta categoria cobre recursos de referência que ajudam a descobrir quais fontes consultar para cada tipo de dado. Apesar de não serem scanners automatizados, eles organizam o processo investigativo.

## OSINT Framework

### Por que usar
OSINT Framework é um site estático que cataloga centenas de serviços divididos por tema (e-mails, redes sociais, geoint, etc.). Clonar o repositório permite usar o mapa offline, sem depender do domínio oficial. Ele é ótimo para montar playbooks personalizados ou treinar novos analistas.

### Instalação offline
```bash
cd ~/Tools && git clone https://github.com/lockfale/osint-framework.git
cd osint-framework && npm install
```
- O `npm install` baixa dependências de build simples (`copyfiles` e `d3`).

### Configuração
```bash
cd ~/Tools/osint-framework
cp OSINT/templates/busca_perfis/osint-framework.env .env.local
```
- Edite `.env.local` para ajustar porta/tema antes de reexecutar `npm start`.

### Uso detalhado
1. **Servidor local**
    ```bash
    cd ~/Tools/osint-framework
    npm start
    # abra http://localhost:8000 ou na porta definida
    ```
2. **Exportar mapa para PDF**
    - Abra o site no navegador, expanda a categoria desejada e use `Firefox -> Imprimir -> Salvar como PDF` para criar guias rápidos.
3. **Customizar categorias**
    ```bash
    cd ~/Tools/osint-framework
    sed -i 's/Social Networks/Social Networks (verificar 2FA)/' public/index.html
    git add public/index.html
    ```
    - Você pode duplicar ramos, remover serviços descontinuados ou adicionar URLs internos do time.

### Fluxo recomendado
- Manter um fork privado com anotações internas.
- Após definir um caso, exportar o ramo correspondente e anexar a um playbook (por exemplo, “Persona -> Social Media -> Verification”).

## Coleções comunitárias (Bellingcat e afins)

Embora Bellingcat mantenha diversas ferramentas específicas, o que mais ajuda na fase de busca é reunir listas vivas de links. Combine o OSINT Framework com coleções da comunidade, como o repositório `cipher387/osint_stuff_tool_collection` (documentado no grupo de automação) e planilhas públicas do Bellingcat.

### Exemplo de extração automática
```bash
curl -s https://raw.githubusercontent.com/bellingcat/auto-archiver/main/README.md | pandoc -t plain > docs/auto-archiver.txt
rg -n "Twitter" docs/auto-archiver.txt
```
- Assim você transforma orientações da comunidade em notas locais pesquisáveis.
