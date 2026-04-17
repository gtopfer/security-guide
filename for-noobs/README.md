# 🐣 Security for Noobs: O Guia Básico

Se você chegou aqui, provavelmente quer melhorar sua segurança digital mas não sabe por onde começar. Este guia foi feito para ser simples, direto e prático. Sem "techobabble" desnecessário.

## 1. Higiene Cibernética Básica 🧼

Antes de usar ferramentas avançadas, faça o básico bem feito.

### Atualize TUDO

- **Sistema Operacional**: Windows, macOS, Linux, Android, iOS. Se tem update, instale.
- **Navegadores**: Chrome, Firefox, Edge. Eles são sua porta para a internet.
- **Apps**: Mantenha seus aplicativos atualizados.

### Bloqueio de Tela

- Configure seu computador e celular para bloquear a tela automaticamente após 1-2 minutos de inatividade.
- Use senhas fortes ou biometria (digital/face).

## 2. Senhas e Gerenciadores 🔑

**A regra de ouro:** Nunca reutilize senhas.

### Use um Gerenciador de Senhas

Não tente memorizar tudo. Use um cofre digital.

- **Bitwarden** (Recomendado, Open Source, Gratuito)
- **KeePassXC** (Para quem prefere offline)

### Crie Senhas Fortes

Uma senha forte é longa e aleatória.

- Ruim: `Senha123`, `Flamengo2024`
- Boa: `X7q#m9$Lp2!zR5` (Gerada pelo gerenciador)
- Passphrase: `cavalo-bateria-correto-grampo` (Fácil de digitar, difícil de quebrar)

## 3. Autenticação de Dois Fatores (2FA/MFA) 🛡️

Ative o 2FA em **todas** as contas que suportarem (Email, Redes Sociais, Bancos).

- **Evite SMS**: SMS pode ser interceptado (SIM Swap).
- **Use Apps Autenticadores**:
  - **Aegis Authenticator** (Android, Open Source)
  - **Raivo OTP** (iOS, Open Source)
  - **Google/Microsoft Authenticator** (Populares, funcionam bem)
- **Chaves de Segurança (Hardware)**: YubiKey (nível avançado, máxima proteção).

## 4. Navegação e Privacidade 🌐

### Navegadores

- **Firefox**: Configure para privacidade estrita.
- **Brave**: Bom para bloquear anúncios nativamente.

### Extensões Essenciais

- **uBlock Origin**: O melhor bloqueador de anúncios e rastreadores. Não aceite imitações.
- **Privacy Badger**: Bloqueia rastreadores invisíveis.

### VPN (Virtual Private Network)

Útil para esconder seu IP e proteger dados em Wi-Fi público.

- **ProtonVPN** (Tem plano grátis confiável)
- **Mullvad** (Foco total em privacidade)

### Tor Browser

Para anonimato mais elevado (jornalistas, ativistas, situações de risco), o **Tor Browser** roteia seu tráfego por múltiplos relays criptografados. Use quando uma VPN comum não é suficiente.

- Download em: <https://www.torproject.org/>
- Não use para login em contas pessoais ou torrents — isso quebra o anonimato.

## 5. Comunicação Segura 💬

### Aplicativos de Mensagens

Nem todo app de mensagens é igual. Prefira os que usam **criptografia ponta a ponta (E2EE) por padrão**.

- **Signal** (Recomendado): E2EE por padrão, open source, sem anúncios.
- **Element/Matrix**: Federado e self-hostável, bom para grupos e comunidades.
- **WhatsApp**: Tem E2EE, mas é da Meta. Melhor que SMS, mas não ideal.
- **Evite**: Telegram (sem E2EE por padrão), SMS para informações sensíveis.

### Email Seguro

- **Proton Mail**: E2EE nativo entre usuários Proton, sem rastreamento.
- **Tutanota**: Alternativa open source com E2EE.
- Se usar Gmail/Outlook, ative a verificação em duas etapas e desconfie de links.

## 6. Criptografia do Dispositivo 🔒

Criptografia garante que, mesmo se seu dispositivo for roubado, os dados não podem ser lidos.

### Como ativar

- **Windows**: Procure por "BitLocker" nas configurações (disponível no Pro/Enterprise). No Home, use "Criptografia do dispositivo".
- **macOS**: Ative o **FileVault** em Preferências do Sistema → Segurança e Privacidade.
- **Linux**: Use **LUKS** durante a instalação — a maioria das distros oferece a opção.
- **Android/iOS**: Em dispositivos modernos, a criptografia já está ativa por padrão ao definir um PIN ou senha de tela.

> Sem criptografia de disco, basta retirar o HD/SSD para ler todos os arquivos — sem precisar da sua senha.

## 7. Phishing e Engenharia Social 🎣

O elo mais fraco é você.

- **Não clique em links estranhos**: Verifique o remetente do email.
- **Desconfie de urgência**: "Sua conta será bloqueada AGORA" é quase sempre golpe.
- **Verifique a URL**: `g0ogle.com` não é `google.com`.

## 8. Verifique a Integridade do que Você Baixa 🔏

Antes de instalar qualquer software importante, confirme que o arquivo não foi alterado ou corrompido.

### No Linux/macOS

```bash
sha256sum arquivo_baixado.iso
# compare com o hash publicado no site oficial
```

### No Windows (PowerShell)

```powershell
Get-FileHash .\arquivo_baixado.iso -Algorithm SHA256
```

### Por que fazer isso?

Atacantes podem interceptar downloads ou comprometer servidores de distribuição. O hash publicado pelo projeto é sua garantia de que o arquivo é legítimo.

> Projetos sérios sempre publicam o hash SHA256 (ou assinatura GPG) na página de download.

## 9. Backups 💾

Seus dados não existem se não tiverem backup.

- **Regra 3-2-1**:
  - 3 cópias dos dados.
  - 2 mídias diferentes (ex: Nuvem + HD Externo).
  - 1 cópia fora do local físico (ex: Nuvem).

## 10. Verifique sua Pegada Digital 👣

Agora que você se protegeu, que tal ver o que a internet já sabe sobre você? Use as ferramentas do próprio repositório para investigar.

### O que o Google sabe?

Use **Google Dorks** para encontrar informações vazadas ou esquecidas.

- 👉 [Aprenda a usar Dorks](../osint-tools-collection/docs/google-search/README.md)

### Onde seu nome de usuário é usado?

Verifique se seu nickname favorito revela suas outras redes sociais.

- 👉 [Ferramentas de Username (Sherlock, Maigret)](../osint-tools-collection/README.md#perfis-e-redes-sociais)

### Seu email vazou?

Descubra se sua senha já está em bancos de dados de hackers.

- 👉 [Ferramentas de Email & Credenciais](../osint-tools-collection/README.md#email-telefone--credenciais)

---

## Próximos Passos 🚀

Agora que você cobriu o básico, explore a [Coleção de Ferramentas OSINT](../osint-tools-collection/README.md) para aprender como investigar e entender o que está exposto sobre você na internet.
