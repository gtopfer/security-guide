# Mentalidade e método

Ferramenta sem método vira barulho. Método sem curiosidade vira checklist inútil. Ofensiva boa é **hipótese → evidência → próximo passo**, com notas que outro analista entenda.

## Mentalidade

- **Enumerar mais do que “explorar”.** A maioria dos engajamentos reais se decide na superfície (serviço esquecido, painel de staging, bucket, usuário com senha padrão de documentação).
- **Assumir que você está errado.** Banner mente, WAF mente, o diagrama do cliente mente. Confirme.
- **Uma coisa de cada vez.** Mudar cinco variáveis no mesmo teste impede saber o que funcionou — e impede o relatório.
- **Pensar em impacto, não em CVE.** Um XSS refletido em página de marketing não é o mesmo que IDOR no endpoint de folha.
- **Escrever na hora.** Timestamp, alvo, o que tentou, o que viu. Memória no fim do dia mente.

## PTES (visão de mapa)

O *Penetration Testing Execution Standard* organiza fases. Use como esqueleto, não como religião:

1. **Pre-engagement** — contrato, ROE, contas de teste, janela.
2. **Intelligence gathering** — OSINT e recon (veja a pasta [reconhecimento](../reconhecimento/visao-geral.md)).
3. **Threat modeling** — quem seria o adversário (script kiddie, insider, ransomware) e o que ele quereria.
4. **Vulnerability analysis** — o que *parece* frágil; ainda não é “ganhei”.
5. **Exploitation** — validação controlada no que foi autorizado (em lab / escopo).
6. **Post-exploitation** — o que aquele acesso *significaria* (movimento, dados). Em muitos pentests isso é limitado de propósito.
7. **Reporting** — o entregável.

NIST SP 800-115 e OSSTMM cobrem espírito parecido (planejar, descobrir, atacar com limite, relatar). Escolha um e seja consistente.

## Kill chain e ATT&CK

A *cyber kill chain* ( recon → weaponize → deliver → exploit → install → C2 → actions) é linear demais para AD e nuvem, mas ajuda a explicar para gestão.

[MITRE ATT&CK](https://attack.mitre.org/) descreve **técnicas** observadas (T-codes). Serve para:

- Mapear o que você *poderia* testar no escopo.
- Conversar com o blue team (“isso seria T1078 Valid Accounts”).
- Não memorizar números: use a matriz como índice.

Detalhes em [taxonomias](taxonomias-mitre-owasp-cwe.md).

## Hipóteses de trabalho (exemplo de raciocínio)

“O app de RH na internet usa o mesmo IdP interno.”  
→ Como verifico *sem* atacar? Docs, cabeçalhos, JS público, contas de teste.  
→ Se for verdade, o impacto é federação, não “mais um formulário”.

“O backup do lab está em storage com ACL pública.”  
→ Confirmo listagem *somente* se o ROE permitir GET em cloud do cliente.  
→ Impacto: dados, não “achei um S3”.

O valor está em **amarrar evidência ao impacto**, não em colecionar screenshots de scanners.

## Notas e higiene de lab

Sugestão de estrutura local (nomes, não ferramenta obrigatória):

```
notas/
  escopo.md
  inventario-hosts.md
  hipoteses.md
  achados/
  evidencias/   # prints com data; sem dado pessoal demais
```

- Separe **fato** (“porta 443 abre TLS1.2”) de **interpretação** (“provável CDN na frente”).
- Não cole senha real de produção nas notas que vão para Git.

## Relação com este repositório

- OSINT e dorks: [osint-tools-collection](../../osint-tools-collection/README.md)
- Ferramentas: [pentest-tools-collection](../../pentest-tools-collection/README.md)
- Relatório: [relatorio-e-comunicacao](../defesa/relatorio-e-comunicacao.md)

## Leitura seguinte

- [Taxonomias](taxonomias-mitre-owasp-cwe.md)
- [Visão geral de recon](../reconhecimento/visao-geral.md)
