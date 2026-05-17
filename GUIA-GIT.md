# 📋 Passo a Passo — Git & GitHub

## 1. Crie o repositório no GitHub

1. Acesse github.com e faça login
2. Clique em **New repository** (botão verde "New")
3. Nome: `portfolio`
4. Descrição: `Portfólio acadêmico e pessoal — ADS CEUB`
5. Marque **Public**
6. **NÃO** marque "Add a README" (já temos um)
7. Clique em **Create repository**

---

## 2. Configure o Git na sua máquina (só na primeira vez)

```bash
git config --global user.name "José Orlando Vieira Xavier"
git config --global user.email "seu@email.com"
```

---

## 3. Suba os arquivos (versão 1.0)

Abra o terminal na pasta onde estão os arquivos e execute:

```bash
# Inicializa o repositório local
git init

# Adiciona todos os arquivos
git add .

# Cria o primeiro commit (versão 1.0)
git commit -m "feat: versão 1.0 — portfólio inicial com página web e documentação"

# Renomeia a branch para main
git branch -M main

# Conecta ao repositório remoto (substitua SEU_USUARIO pelo seu username)
git remote add origin https://github.com/SEU_USUARIO/portfolio.git

# Envia para o GitHub
git push -u origin main
```

---

## 4. Ative o GitHub Pages

1. No repositório, clique em **Settings**
2. No menu lateral, clique em **Pages**
3. Em "Source", selecione **main** e pasta **/ (root)**
4. Clique em **Save**
5. Aguarde ~1 min. O link será: `https://SEU_USUARIO.github.io/portfolio`

---

## 5. Para futuras atualizações

```bash
git add .
git commit -m "feat: descrição do que foi alterado"
git push
```

---

## ✅ Checklist de entrega

- [ ] Repositório criado e público no GitHub
- [ ] index.html (página web) no repositório
- [ ] README.md principal criado
- [ ] Pastas `academico/` e `pessoal/` criadas
- [ ] GitHub Pages ativo com o link funcionando
- [ ] Link do GitHub adicionado no LinkedIn
- [ ] Vídeo de apresentação no YouTube (5 min)
- [ ] PDF de entrega enviado até 17/05/2026 23h55
