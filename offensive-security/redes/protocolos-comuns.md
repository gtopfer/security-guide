# Protocolos comuns e superfície típica

Lista de estudo: o que cada família *é* e que classe de risco costuma carregar. Sem comandos de ataque.

## DNS

Resolve nomes. Superfície: transferência de zona mal configurada (vaza mapa), records TXT (SPF/DMARC — também defesa de e-mail), subdomínios esquecidos, DNS rebinding como *classe* em apps que confiam em “é intranet”.

Estude: tipos de record, resolvers, cache.

## HTTP(S)

Ver pasta [web](../web/modelo-http-e-sessao.md). Na rede: vhosts, proxy reverso, TLS offload.

## SSH

Admin remoto. Superfície: senha vs chave, usuário `root` permitido, versão antiga, port knocking como obscuridade (não é controle). Defesa: chave, MFA, allowlist, jump host.

## SMB / RPC (Windows)

Compartilhamentos e API remota histórica. Superfície: share aberto, named pipes, auth NTLM na rede. Estude **o que é** um share e um *null session* em material histórico; pratique só em lab Windows isolado.

## LDAP / Kerberos

Identidade. Ver [Active Directory](../identidade/active-directory-conceitos.md). Expor LDAP anônimo ou certificado ruim em AD é tema de superfície.

## SMTP / IMAP / Magia de e-mail

Relay aberto (clássico), spoofing (SPF/DKIM/DMARC), webmail. Engenharia social *entrega* por aqui.

## RDP / VPN / TLS VPN

Borda de acesso remoto: credencial, MFA, CVE de appliance (classe: patch de perímetro). Inventariar *o que* está na 443 além do site marketing.

## SNMP, IPMI, WinRM, WMI, Docker API, Kubernetes API

Gerência. Se está na internet sem auth, o problema é **exposição**, não “técnica avançada”. Estude o *propósito* do protocolo (monitorar, controlar hardware, orquestrar).

## Banco de dados em porta padrão

Postgres, MySQL, Mongo, Redis, Elasticsearch: o achado típico é **não deveria estar no 0.0.0.0**. Auth default e falta de TLS são classes de misconfig.

## ICS / IoT (aviso)

Protocolos sem auth histórica (Modbus, etc.). Não teste em planta real “para ver”. Labs específicos ou simulação.

## Como usar esta lista

Monte um quadro: protocolo → função de negócio → se internet-facing faz sentido → log típico. Isso é o que um pentester júnior *deveria* saber antes de qualquer framework.

## Leitura seguinte

- [Linux](../sistemas/linux-superficie.md)
- [Windows](../sistemas/windows-superficie.md)
