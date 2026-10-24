# Mentalidade e método

Ferramenta sem método produz ruído. Método sem pergunta produz checklist que não encontra o risco. O trabalho ofensivo útil segue **hipótese, evidência e próximo passo**, com nota que outro analista entende.

## Mentalidade

- **Enumere antes de explorar.** Na maior parte dos trabalhos reais, o resultado depende da superfície: serviço esquecido, painel de homologação, bucket ou usuário com senha padrão da documentação.
- **Confirme a premissa.** Banner, WAF e diagrama do cliente podem estar errados. Verifique.
- **Mude uma variável por vez.** Cinco mudanças no mesmo teste impedem saber o que funcionou. Também impedem o relatório.
- **Meça o impacto, não só o CVE.** Um XSS refletido em página de marketing não tem o mesmo impacto de um IDOR no endpoint da folha de pagamento.
- **Escreva na hora.** Registre horário, alvo, o que você tentou e o que você observou. A memória no fim do dia omite detalhe.

## PTES (mapa de fases)

O *Penetration Testing Execution Standard* organiza as fases. Use-o como estrutura, não como lista rígida:

1. **Pre-engagement** — contrato, regras de engajamento, conta de teste e janela.
2. **Intelligence gathering** — OSINT e reconhecimento. Veja a pasta [reconhecimento](../reconhecimento/visao-geral.md).
3. **Threat modeling** — qual adversário é plausível (oportunista, insider, ransomware) e o que ele buscaria.
4. **Vulnerability analysis** — o que parece frágil. Isso ainda não é um comprometimento.
5. **Exploitation** — validação controlada no que foi autorizado (laboratório ou escopo).
6. **Post-exploitation** — o que aquele acesso significaria (movimento e dado). Em muitos pentests esta fase é limitada de propósito.
7. **Reporting** — o entregável.

O NIST SP 800-115 e o OSSTMM cobrem a mesma ideia: planejar, descobrir, testar com limite e relatar. Escolha um método e mantenha-o.

## Kill chain e ATT&CK

A *cyber kill chain* (reconhecimento, preparação, entrega, exploração, instalação, comando e controle, ação) é linear demais para AD e para nuvem. Ainda assim, ajuda a explicar o ciclo para a gestão.

O [MITRE ATT&CK](https://attack.mitre.org/) descreve **técnicas** observadas (códigos T). Use a matriz para:

- Mapear o que você pode testar no escopo.
- Conversar com o blue team ("isto seria T1078 Valid Accounts").
- Não memorizar números. Use a matriz como índice.

O detalhe está em [taxonomias](taxonomias-mitre-owasp-cwe.md).

## Hipótese de trabalho (exemplo de raciocínio)

"O aplicativo de RH na internet usa o mesmo provedor de identidade interno."  
Como verifico isso sem atacar? Documentação, cabeçalho, JavaScript público e conta de teste.  
Se a hipótese for verdadeira, o impacto é a federação, não "mais um formulário".

"A cópia de segurança do laboratório está em armazenamento com ACL pública."  
Confirmo a listagem somente se as regras de engajamento permitirem GET na nuvem do cliente.  
O impacto é o dado, não o fato isolado de existir um bucket.

O valor está em **ligar a evidência ao impacto**, não em acumular captura de tela de scanner.

## Notas e higiene de laboratório

Estrutura local sugerida (nomes, não uma ferramenta obrigatória):

```
notas/
  escopo.md
  inventario-hosts.md
  hipoteses.md
  achados/
  evidencias/   # captura com data; sem dado pessoal além do necessário
```

- Separe o **fato** ("a porta 443 oferece TLS 1.2") da **interpretação** ("há um CDN na frente").
- Não grave senha real de produção em nota que vai para o Git.

## Relação com este repositório

- OSINT e dorks: [osint-tools-collection](../../osint-tools-collection/README.md)
- Ferramentas: [pentest-tools-collection](../../pentest-tools-collection/README.md)
- Relatório: [relatorio-e-comunicacao](../defesa/relatorio-e-comunicacao.md)

## Leitura seguinte

- [Taxonomias](taxonomias-mitre-owasp-cwe.md)
- [Visão geral de recon](../reconhecimento/visao-geral.md)
