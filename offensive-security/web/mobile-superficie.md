# Mobile (Android e iOS): superfície para estudo

O celular concentra sessão de banco, segundo fator e e-mail. A ofensiva mobile ética é **segurança de aplicação mais plataforma**. Não é clonar o aplicativo de mensagem da vítima.

## Modelo

- O aplicativo é binário, dado local, comunicação entre processos e backend. A API continua sendo [web e API](../web/apis-e-auth.md).
- A loja (Play ou App Store) reduz malware e aplicativo abusivo. Não elimina.
- Root e jailbreak no aparelho do dia a dia removem mitigação. O guia [para iniciantes](../../for-noobs/README.md) recomenda não fazer isso no telefone pessoal.

## Android (conceitos)

- UID por aplicativo, permissão, intent, backup e armazenamento interno ou externo.
- WebView: XSS vira ponte para o aplicativo.
- Certificate pinning é uma ideia de confiança no TLS. Um pinning mal feito impede a interceptação legítima de laboratório.

## iOS (conceitos)

- O sandbox é mais rígido. Há Keychain e ATS (App Transport Security).
- Sideload corporativo e perfil de MDM são superfície da empresa.

## OWASP MASVS e MASTG

Padrão de estudo: <https://mas.owasp.org/> — requisito e teste. Execute o teste somente no **seu** aplicativo ou em laboratório.

## O que não fazer

Não intercepte tráfego de aplicativo de terceiro na rede de outra pessoa. Não implante spyware. Não contorne biometria em aparelho que não é seu.

## Leitura seguinte

- [APIs](../web/apis-e-auth.md)
- [MASVS](https://mas.owasp.org/)

## Repositórios para aprofundar

[MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF), [apktool](https://github.com/iBotPeaches/Apktool), [jadx](https://github.com/skylot/jadx), [Frida](https://github.com/frida/frida), [objection](https://github.com/sensepost/objection), [MASTG](https://github.com/OWASP/mastg). Laboratórios DIVA, InjuredAndroid e iGoat estão na coleção de pentest.
