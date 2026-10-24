# Protocolos comuns e superfície típica

Lista de estudo: o que cada família é e qual classe de risco ela costuma carregar. Sem comando de ataque.

## DNS

Resolve nome. Superfície: transferência de zona mal configurada (vaza o mapa), registro TXT (SPF e DMARC, que também defendem o e-mail), subdomínio esquecido e DNS rebinding como classe em aplicativo que confia em "é a intranet".

Estude tipo de registro, resolvedor e cache.

## HTTP(S)

Veja a pasta [web](../web/modelo-http-e-sessao.md). Na rede: virtual host, proxy reverso e terminação TLS.

## SSH

Administração remota. Superfície: senha em vez de chave, usuário `root` permitido, versão antiga e port knocking como obscuridade (não é controle). Defesa: chave, MFA, lista de permissão e bastion.

## SMB e RPC (Windows)

Compartilhamento e API remota histórica. Superfície: share aberto, named pipe e autenticação NTLM na rede. Estude o que é um share e o que foi uma sessão nula, em material histórico. Pratique somente em laboratório Windows isolado.

## LDAP e Kerberos

Identidade. Veja [Active Directory](../identidade/active-directory-conceitos.md). LDAP anônimo ou certificado inadequado no AD é tema de superfície.

## SMTP, IMAP e e-mail

Relay aberto (caso clássico), falsificação (SPF, DKIM e DMARC) e webmail. A engenharia social entrega a mensagem por aqui.

## RDP, VPN e VPN sobre TLS

Borda de acesso remoto: credencial, MFA e CVE de appliance (classe: correção de perímetro). Inventarie o que escuta na porta 443 além do site de marketing.

## SNMP, IPMI, WinRM, WMI, API do Docker e API do Kubernetes

Gerência. Se o serviço está na internet sem autenticação, o problema é a **exposição**, não uma técnica avançada. Estude o propósito do protocolo: monitorar, controlar hardware ou orquestrar.

## Banco de dados em porta padrão

PostgreSQL, MySQL, MongoDB, Redis e Elasticsearch: o achado típico é que o serviço **não deveria escutar em 0.0.0.0**. Autenticação padrão e falta de TLS são classes de configuração incorreta.

## ICS e IoT

Protocolo sem autenticação histórica (Modbus, entre outros). Não teste em planta real "para ver". Use laboratório específico ou simulação.

## Como usar esta lista

Monte um quadro: protocolo, função de negócio, se a exposição à internet faz sentido, e log típico. Isso é o que um pentester no início precisa saber antes de qualquer framework.

## Leitura seguinte

- [Linux](../sistemas/linux-superficie.md)
- [Windows](../sistemas/windows-superficie.md)
