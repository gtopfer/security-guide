# O que é segurança ofensiva

Segurança ofensiva é o conjunto de práticas que **simulam ou analisam o ponto de vista de quem ataca**, para achar falhas **antes** de um adversário real. O produto não é “invadir”: é **evidência reproduzível**, risco traduzido para o negócio e recomendação de correção.

## Ofensiva vs defensiva

| | Defensiva (blue) | Ofensiva (red / pentest) |
|--|------------------|---------------------------|
| Pergunta | Como detectar, conter, recuperar? | O que um adversário consegue fazer *neste* escopo? |
| Artefato típico | Alerta, playbook de IR, hardening | Relatório, PoC controlado em lab, backlog de correção |
| Sucesso | Tempo de detecção baixo, impacto limitado | Achados reais, priorizados, com caminho de remediação |

As duas se alimentam. Sem ofensiva, a defesa otimiza o que já conhece. Sem defesa, a ofensiva vira teatro.

## Papéis que as pessoas misturam

**Pentest (teste de invasão)**  
Engajamento com início, fim, escopo e relatório. Objetivo: cobertura acordada (rede, web, AD, nuvem) e lista de vulnerabilidades com impacto. Costuma seguir metodologia (PTES, OSSTMM, NIST SP 800-115 em espírito).

**Red team**  
Exercício mais longo, com objetivo de negócio (ex.: “acessar o domínio de folha”). Usa stealth, engenharia social e caminhos combinados. Menos “scan completo”, mais “a missão foi cumprida?”. Quase sempre exige purple team / detecção no meio.

**Bug bounty**  
Programa público ou privado: você testa *só* o que as regras listam, em troca de recompensa. Escopo é a lei do jogo. Fora do escopo = incidente.

**Purple team**  
Ataque e defesa no mesmo exercício, com feedback imediato (o alerta disparou? a regra Sigma pegou?).

**Pesquisa de vulnerabilidade / 0-day**  
Achar falhas em software (às vezes com fuzzing, revisão de código). Disclosure responsável; não é “usar 0-day em produção de terceiro”.

**CTF**  
Jogo com flags. Ótimo para raciocínio; ruim se for o *único* treino — o mundo real tem escopo, política e relatórios.

## Cadeia mental (não é receita)

Quase todo trabalho ofensivo, no papel, passa por:

1. Entender o **alvo autorizado** e as restrições.
2. **Reconhecer** o que existe (passivo, depois ativo se permitido).
3. **Priorizar** superfície (o que é autenticado, o que é internet-facing, o que tem dados).
4. **Validar** falhas em condição controlada (não destruir, não exfiltrar além do combinado).
5. **Documentar** impacto e correção.
6. **Devolver** o ambiente (contas de teste, artefatos).

Os documentos desta pasta detalham cada bloco em conceito. A execução técnica fica para labs oficiais e ferramentas listadas no repositório.

## Competências que realmente importam

- Redes e sistemas o suficiente para *ler* um pacote, um log e um processo.
- Web: HTTP, cookies, CORS, sessão — não “lista de payloads”.
- Identidade: o que é um ticket, um token, um hash, um grupo de admin.
- Escrita: se não dá para reproduzir o achado, ele não existe para o cliente.
- Ética: recusar trabalho sem autorização é habilidade profissional, não frescura.

## Leitura seguinte

- [Ética, escopo e lei](etica-e-lei.md)
- [Mentalidade e método](mentalidade-e-metodo.md)
- [Coleção de ferramentas de pentest](../../pentest-tools-collection/README.md)
