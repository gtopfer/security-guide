# O que é segurança ofensiva

Segurança ofensiva é o conjunto de práticas que **analisa o ponto de vista de quem ataca**, para encontrar falha **antes** de um adversário real. O produto não é a invasão. O produto é **evidência que outra pessoa consegue repetir**, risco traduzido para o negócio e recomendação de correção.

## Ofensiva e defensiva

| | Defensiva (blue team) | Ofensiva (red team / pentest) |
|--|------------------|---------------------------|
| Pergunta | Como detectar, conter e recuperar? | O que um adversário consegue fazer neste escopo? |
| Artefato típico | Alerta, roteiro de resposta a incidente, hardening | Relatório, prova controlada em laboratório, fila de correção |
| Sucesso | Tempo de detecção baixo e impacto limitado | Achado real, priorizado, com caminho de correção |

As duas práticas se alimentam. Sem a ofensiva, a defesa otimiza só o que já conhece. Sem a defesa, o exercício ofensivo não melhora a detecção.

## Papéis que costumam ser confundidos

**Pentest (teste de invasão)**  
O trabalho tem início, fim, escopo e relatório. O objetivo é a cobertura acordada (rede, web, AD, nuvem) e a lista de vulnerabilidade com impacto. O método usual segue PTES, OSSTMM ou o espírito do NIST SP 800-115.

**Red team**  
O exercício é mais longo. O objetivo é de negócio, por exemplo acessar o domínio que guarda a folha de pagamento. O trabalho usa discrição, engenharia social e caminhos combinados. A pergunta principal é se a missão foi cumprida, não se o scan foi completo. Em geral, o exercício exige purple team e detecção no mesmo período.

**Bug bounty**  
O programa é público ou privado. Você testa somente o que as regras listam, em troca de recompensa. O escopo é a regra do programa. Fora do escopo, o teste é um incidente.

**Purple team**  
Ataque e defesa ocorrem no mesmo exercício, com retorno imediato. A pergunta é se o alerta disparou e se a regra Sigma registrou o evento.

**Pesquisa de vulnerabilidade e 0-day**  
O trabalho encontra falha em software, às vezes com fuzzing ou com revisão de código. O disclosure é responsável. Usar um 0-day em produção de terceiro não faz parte desta pesquisa.

**CTF**  
O jogo usa flags. O CTF treina o raciocínio. Ele não substitui o treino completo: o trabalho real tem escopo, política e relatório.

## Sequência de trabalho (não é receita)

Quase todo trabalho ofensivo, no papel, passa por estas etapas:

1. Entenda o **alvo autorizado** e as restrições.
2. **Reconheça** o que existe. Comece pelo modo passivo. Passe ao modo ativo se o escopo permitir.
3. **Priorize** a superfície: o que exige autenticação, o que está na internet e o que guarda dado.
4. **Valide** a falha em condição controlada. Não destrua o sistema. Não exfiltre além do combinado.
5. **Documente** o impacto e a correção.
6. **Devolva** o ambiente: remova conta de teste e artefato.

Os documentos desta pasta detalham cada bloco em conceito. A execução técnica fica em laboratório oficial e nas ferramentas listadas no repositório.

## Competências que o trabalho exige

- Redes e sistemas suficientes para ler um pacote, um log e um processo.
- Web: HTTP, cookie, CORS e sessão. Não uma lista de payload.
- Identidade: ticket, token, hash e grupo de administrador.
- Escrita: se outra pessoa não consegue repetir o achado, o achado não existe para o cliente.
- Ética: recusar trabalho sem autorização é competência profissional.

## Leitura seguinte

- [Ética, escopo e lei](etica-e-lei.md)
- [Mentalidade e método](mentalidade-e-metodo.md)
- [Coleção de ferramentas de pentest](../../pentest-tools-collection/README.md)
