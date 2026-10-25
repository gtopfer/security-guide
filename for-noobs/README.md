# Fundamentos de segurança para iniciantes

Este guia ajuda quem quer melhorar a segurança digital e ainda não tem um ponto de partida. O texto é direto. Cada seção descreve uma ação concreta.

## 1. Higiene básica

Faça o básico antes de usar uma ferramenta avançada.

### Atualize o sistema e os aplicativos

- **Sistema operacional**: instale as atualizações do Windows, do macOS, do Linux, do Android e do iOS.
- **Navegador**: mantenha o Chrome, o Firefox ou o Edge atualizado. O navegador é o programa que acessa a maior parte da internet.
- **Aplicativos**: instale as atualizações dos aplicativos que você usa.

### Bloqueio de tela

- Configure o computador e o celular para bloquear a tela após 1 a 2 minutos de inatividade.
- Use uma senha forte ou biometria (impressão digital ou reconhecimento facial).

## 2. Senhas e gerenciadores

Não reutilize senhas.

### Use um gerenciador de senhas

Não memorize todas as senhas. Guarde-as em um cofre digital.

- **Bitwarden** (recomendado): código aberto, com plano gratuito.
- **KeePassXC**: use quando você prefere um cofre offline.

### Crie senhas fortes

Uma senha forte é longa e aleatória.

- Fraca: `Senha123`, `Flamengo2024`
- Forte: `X7q#m9$Lp2!zR5` (gerada pelo gerenciador)
- Frase-senha: `cavalo-bateria-correto-grampo` (fácil de digitar, difícil de adivinhar)

## 3. Autenticação de dois fatores (2FA/MFA)

Ative o 2FA em todas as contas que oferecem essa opção. Priorize e-mail, rede social e banco.

- **Evite o SMS**: o SMS pode ser interceptado (troca de chip, ou SIM swap).
- **Use um aplicativo autenticador**:
  - **Aegis Authenticator** (Android, código aberto)
  - **Raivo OTP** (iOS, código aberto)
  - **Google Authenticator** ou **Microsoft Authenticator** (amplamente suportados)
- **Chave de segurança (hardware)**: a YubiKey oferece proteção alta. Use quando a conta é crítica.

## 4. Navegação e privacidade

### Navegadores

- **Firefox**: configure a proteção contra rastreamento no modo estrito.
- **Brave**: bloqueia anúncios no próprio navegador.

### Extensões

- **uBlock Origin**: bloqueia anúncio e rastreador. Instale a extensão a partir da loja oficial do navegador.
- **Privacy Badger**: bloqueia rastreadores que o navegador não mostra na página.

### VPN (rede privada virtual)

A VPN oculta o endereço IP do seu provedor de destino e protege o tráfego em uma rede Wi-Fi pública.

- **Proton VPN**: tem um plano gratuito com política de privacidade publicada.
- **Mullvad**: o serviço é voltado à privacidade.

### Tor Browser

O **Tor Browser** encaminha o tráfego por vários relays criptografados. Use-o quando o anonimato é necessário, por exemplo em jornalismo ou em situação de risco.

- Download: <https://www.torproject.org/>
- Não faça login em uma conta pessoal no Tor Browser.
- Não use o Tor Browser para torrent. Essas duas ações ligam a sessão à sua identidade.

## 5. Comunicação

### Aplicativos de mensagem

Prefira um aplicativo com **criptografia de ponta a ponta (E2EE) ativada por padrão**.

- **Signal** (recomendado): E2EE por padrão, código aberto, sem anúncio.
- **Element / Matrix**: federado e pode ser hospedado por você. Serve a grupo e comunidade.
- **WhatsApp**: tem E2EE, mas pertence à Meta. É melhor que o SMS. Não é a opção de maior privacidade.
- **Evite** o Telegram para dado sensível: o E2EE não é o padrão. Evite o SMS para o mesmo fim.

### E-mail

- **Proton Mail**: E2EE entre usuários Proton, sem rastreamento de conteúdo para anúncio.
- **Tuta**: alternativa de código aberto com E2EE.
- Se você usa Gmail ou Outlook, ative a verificação em duas etapas. Confira o endereço antes de abrir um link.

## 6. Criptografia do dispositivo

A criptografia de disco impede a leitura dos arquivos quando o dispositivo é roubado.

### Como ativar

- **Windows**: procure "BitLocker" nas configurações (edições Pro e Enterprise). Na edição Home, use "Criptografia de dispositivo".
- **macOS**: ative o **FileVault** em Ajustes do Sistema, na seção de privacidade e segurança.
- **Linux**: use **LUKS** durante a instalação. A maioria das distribuições oferece essa opção.
- **Android e iOS**: em aparelhos atuais, a criptografia fica ativa quando você define um PIN ou uma senha de tela.

> Sem criptografia de disco, uma pessoa com acesso físico remove o disco e lê os arquivos. A senha da conta do sistema não protege esses arquivos.

## 7. Phishing e engenharia social

O phishing ataca a pessoa que usa o sistema, não só o software.

- **Não abra um link suspeito.** Confira o remetente do e-mail.
- **Desconfie de urgência.** A frase "sua conta será bloqueada agora" é um padrão comum de golpe.
- **Confira o endereço.** `g0ogle.com` não é `google.com`.

O texto completo de defesa (canais, sinais e resposta no trabalho) está na trilha [Engenharia social](../social-engineering/README.md).

## 8. Integridade do arquivo baixado

Antes de instalar um software importante, confirme que o arquivo não foi alterado.

### No Linux e no macOS

```bash
sha256sum arquivo_baixado.iso
# compare com o hash publicado no site oficial
```

### No Windows (PowerShell)

```powershell
Get-FileHash .\arquivo_baixado.iso -Algorithm SHA256
```

### Por que comparar o hash

Um atacante pode interceptar o download ou comprometer um servidor de distribuição. O hash publicado pelo projeto mostra se o arquivo corresponde à cópia oficial.

> Um projeto mantido publica o hash SHA-256 ou uma assinatura GPG na página de download.

## 9. Segurança em dispositivo móvel

O celular guarda sessão de banco, mensagem e fator de autenticação. Proteja o celular com o mesmo rigor do computador.

- **Instale aplicativos só nas lojas oficiais**: Google Play e App Store. Um APK de site de terceiro é um caminho comum de malware.
- **Revise as permissões**: um aplicativo de lanterna não precisa de contatos nem de microfone. Revise em Configurações, Apps, Permissões.
- **Evite root e jailbreak** no aparelho de uso diário. Esses modos removem proteções do sistema.
- **Ative "Encontrar meu dispositivo"** (Google) ou "Buscar" (Apple). Essas funções localizam, bloqueiam ou apagam um aparelho perdido.
- **Em Wi-Fi público**, não acesse o banco e não faça login em conta sensível sem VPN.
- **Desative Bluetooth e NFC** quando você não os usa. Isso reduz a superfície de ataque.

## 10. Resposta a comprometimento

Se você suspeita que uma conta ou um dispositivo foi acessado por outra pessoa, execute estes passos nesta ordem:

1. **Isole o dispositivo.** Desconecte Wi-Fi e dados móveis se você suspeita de malware ativo.
2. **Troque a senha da conta afetada.** Use outro dispositivo confiável, se possível.
3. **Encerre as sessões ativas.** Google, redes sociais e bancos oferecem "sair de todos os dispositivos" ou "gerenciar sessões".
4. **Confira o 2FA.** Confirme que o e-mail de recuperação, o telefone e o aplicativo autenticador ainda são seus. Um atacante pode trocar esses dados para manter o acesso.
5. **Troque as senhas reutilizadas.** Se a senha comprometida existe em outro serviço, troque-a lá. Passe a guardar as senhas em um gerenciador.
6. **Analise o dispositivo.** Execute um antivírus ou antimalware de fonte confiável no computador ou no celular afetado.
7. **Avise os contatos.** Se a conta é de e-mail ou de mensagem, avise pessoas próximas. Uma conta comprometida é usada para golpe contra esses contatos.
8. **Registre o ocorrido.** Guarde capturas de tela e horários. Esse registro serve a um boletim de ocorrência ou a uma contestação no banco.

> Depois da contenção, releia a seção [7. Phishing e engenharia social](#7-phishing-e-engenharia-social). Identifique o caminho de entrada e ajuste o controle correspondente.

## 11. Cópias de segurança

Um dado sem cópia de segurança pode ser perdido.

- **Regra 3-2-1**:
  - Mantenha 3 cópias dos dados.
  - Use 2 mídias diferentes (por exemplo, nuvem e disco externo).
  - Mantenha 1 cópia fora do local físico (por exemplo, nuvem).

## 12. Pegada digital

Depois da proteção básica, verifique o que já está publicado sobre você. Use as ferramentas deste repositório.

### O que o Google indexou

Use **Google Dorks** para localizar informação publicada ou esquecida.

- [Guia de operadores de busca](../osint-tools-collection/docs/google-search/README.md)

### Onde o nome de usuário aparece

Um nome de usuário repetido liga perfis em várias redes.

- [Ferramentas de nome de usuário (Sherlock, Maigret)](../osint-tools-collection/README.md#perfis-e-redes-sociais)

### O e-mail apareceu em um vazamento

Verifique se o endereço aparece em bases de credenciais vazadas.

- [Ferramentas de e-mail e credenciais](../osint-tools-collection/README.md#email-telefone--credenciais)

## Próximo passo

Depois deste guia, leia a [Coleção de ferramentas OSINT](../osint-tools-collection/README.md). Ela mostra como investigar o que está publicado sobre você.

Se o objetivo é entender como um ataque é planejado, para melhorar a defesa, leia [Estudos de segurança ofensiva](../offensive-security/README.md). Essa pasta cobre método, web, identidade e laboratórios legais. Ela não ensina a invadir um sistema de terceiro.
