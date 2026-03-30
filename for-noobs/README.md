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
  - **Tofu** (iOS, Open Source — substitui o Raivo OTP após mudança suspeita de dono em 2023)
  - **Google/Microsoft Authenticator** (Populares, funcionam bem)
- **Chaves de Segurança (Hardware)**: YubiKey (Nível avançado/Paranóico).

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

## 5. Phishing e Engenharia Social 🎣

O elo mais fraco é você.

- **Não clique em links estranhos**: Verifique o remetente do email.
- **Desconfie de urgência**: "Sua conta será bloqueada AGORA" é quase sempre golpe.
- **Verifique a URL**: `g0ogle.com` não é `google.com`.

## 6. Backups 💾

Seus dados não existem se não tiverem backup.

- **Regra 3-2-1**:
  - 3 cópias dos dados.
  - 2 mídias diferentes (ex: Nuvem + HD Externo).
  - 1 cópia fora do local físico (ex: Nuvem).

## 7. Verifique sua Pegada Digital 👣

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
