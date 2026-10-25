# Referências

Fonte primária e ferramenta de **defesa**. Confira o link de novo antes de usar o material em um treino. Este guia não copia norma nem cartilha.

Não há kit de campanha nesta lista. Ferramenta cujo uso principal é enviar isca não entra nesta trilha.

## Brasil

| Fonte | Uso |
|-------|-----|
| [Lei 12.737/2012](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12737.htm) | Invasão de dispositivo |
| [Marco Civil (Lei 12.965/2014)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm) | Privacidade e registro de acesso |
| [LGPD (Lei 13.709/2018)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) | Dado pessoal em reporte e em exercício |
| [Cartilha — Golpes: não se deixe enganar](https://cartilha.cert.br/fasciculos/#golpes) | Alerta para a pessoa ([PDF](https://cartilha.cert.br/fasciculos/golpes/fasciculo-golpes.pdf)) |
| [Cartilha — Golpes: evite fraudes](https://cartilha.cert.br/fasciculos/#golpes-evite-fraudes) | Fraude e pagamento ([PDF](https://cartilha.cert.br/fasciculos/golpes-evite-fraudes/fasciculo-golpes-evite-fraudes.pdf)) |
| [Cartilha — Caiu? Veja o que fazer](https://cartilha.cert.br/fasciculos/#golpes-o-que-fazer) | Ação depois do golpe ([PDF](https://cartilha.cert.br/fasciculos/golpes-o-que-fazer/fasciculo-golpes-o-que-fazer.pdf)) |
| [Dicas rápidas da Cartilha](https://cartilha.cert.br/dicas-rapidas/#golpes) | Lista curta de e-mail e de golpe |
| [CERT.br — contato](https://www.cert.br/contato/) | Reporte quando não há canal interno |

## Guias e normas

| Fonte | Uso |
|-------|-----|
| [NIST SP 800-177 Rev. 1](https://csrc.nist.gov/pubs/sp/800/177/r1/final) | E-mail confiável (SPF, DKIM, DMARC) |
| [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final) | Programa de aprendizado em segurança e privacidade |
| [NIST SP 800-61 Rev. 2](https://csrc.nist.gov/pubs/sp/800/61/r2/final) | Guia clássico de tratamento de incidente |
| [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Recomendações atuais ligadas ao CSF 2.0 |
| [CISA — reconhecer e reportar phishing](https://www.cisa.gov/secure-our-world/recognize-and-report-phishing) | Alerta curto para a pessoa |
| [CISA — treinar a equipe](https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/teach-employees-avoid-phishing) | Treino sem escrever isca do zero |
| [NCSC — phishing](https://www.ncsc.gov.uk/collection/phishing-scams) | Guia público de reconhecimento |
| [MITRE ATT&CK T1566](https://attack.mitre.org/techniques/T1566/) | Phishing: leia detecção e mitigação |
| [MITRE ATT&CK T1598](https://attack.mitre.org/techniques/T1598/) | Phishing para obter informação |
| [MITRE ATT&CK T1656](https://attack.mitre.org/techniques/T1656/) | Personificação |
| [MITRE ATT&CK M1017](https://attack.mitre.org/mitigations/M1017/) | Treino de usuário |
| [MITRE ATT&CK M1032](https://attack.mitre.org/mitigations/M1032/) | Autenticação multifator |
| [MITRE D3FEND](https://d3fend.mitre.org/) | Vocabulário do lado da defesa |

## Protocolos

- SPF: [RFC 7208](https://www.rfc-editor.org/rfc/rfc7208)
- DKIM: [RFC 6376](https://www.rfc-editor.org/rfc/rfc6376)
- DMARC: [RFC 7489](https://www.rfc-editor.org/rfc/rfc7489)
- ARC: [RFC 8617](https://www.rfc-editor.org/rfc/rfc8617). ARC registra a autenticação quando um intermediário encaminha a mensagem. Não transforma encaminhamento em prova de autoria.

## Software livre de defesa

Estas ferramentas filtram ou autenticam e-mail. Elas não enviam campanha.

| Projeto | Repositório | Função |
|---------|-------------|--------|
| SpamAssassin | <https://github.com/apache/spamassassin> | Filtro de spam. Site: <https://spamassassin.apache.org/> |
| Rspamd | <https://github.com/rspamd/rspamd> | Filtro de spam, com checagem de SPF, DKIM e DMARC. Site: <https://rspamd.com/> |
| OpenDKIM | <https://github.com/trusteddomainproject/OpenDKIM> | Assinatura e conferência DKIM no servidor de e-mail |
| OpenDMARC | <https://github.com/trusteddomainproject/OpenDMARC> | Conferência da política DMARC no servidor de e-mail |

Critério de inclusão: licença de software livre, código auditável e uso de defesa. A contribuição de ferramenta segue o [CONTRIBUTING.md](../CONTRIBUTING.md).

Indicador e regra de detecção continuam nas coleções já existentes. Não duplique o catálogo aqui.

- [Inteligência de ameaças na coleção OSINT](../osint-tools-collection/README.md#inteligência-de-ameaças--ioc)
- [Detecção e logs](../offensive-security/defesa/deteccao-e-logs.md)
- Sigma: <https://github.com/SigmaHQ/sigma>

## Modelo mínimo de registro

Use no chamado interno. Não é um modelo de isca.

```
Data e hora (com fuso):
Canal:
Remetente visível:
Endereço ou número:
Pedido (uma frase):
Ação já feita (nada, clique, dado, pagamento, programa):
Conta ou processo:
Evidência guardada (sem senha e sem código):
```

## Leitura seguinte

- [Índice da trilha](README.md)
- [Fundamentos para iniciantes](../for-noobs/README.md)
