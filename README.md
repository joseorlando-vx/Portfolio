# 🌐 Portfólio Pessoal — José Orlando Vieira Xavier

> **Desafio — Entrega Intermediária: Criação de Repositório com Versionamento**
> Curso de Análise e Desenvolvimento de Sistemas (ADS) — CEUB · 2026

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Online-brightgreen?style=flat-square&logo=github)](https://joseorlando-vx.github.io/portfolio)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-José%20Orlando-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/joseorlandovieira)
[![Versão](https://img.shields.io/badge/Versão-1.0-red?style=flat-square)]()
[![Licença](https://img.shields.io/badge/Licença-MIT-gray?style=flat-square)]()

---

## 📌 Sobre o Projeto

Este repositório foi desenvolvido como parte do **Desafio de Entrega Intermediária** da disciplina de **Introdução à Computação** do curso de ADS no CEUB. O objetivo é criar e configurar um repositório no GitHub com projetos acadêmicos e pessoais, aplicando boas práticas de versionamento com Git, organização de diretórios, documentação e publicação via GitHub Pages.

O projeto central é um **portfólio pessoal** desenvolvido com HTML5 e CSS3 puro, publicado como site estático pelo GitHub Pages, que reúne minha trajetória profissional, projetos, habilidades técnicas e informações de contato.

🔗 **Acesse o site:** [joseorlando-vx.github.io/portfolio](https://joseorlando-vx.github.io/portfolio)

---

## 🎯 Objetivos da Atividade

| # | Requisito | Status |
|---|---|---|
| 1 | Planejamento e estrutura do repositório | ✅ Concluído |
| 2 | Criação de projeto web e versionamento com Git | ✅ Concluído |
| 3 | Organização em pastas e documentação com README.md | ✅ Concluído |
| 4 | Publicação via GitHub Pages | ✅ Concluído |
| 5 | Compartilhamento e integração com LinkedIn | ✅ Concluído |
| 6 | Apresentação do repositório | ✅ Concluído |

---

## 1. 📋 Planejamento do Repositório

### Definição das Seções

O repositório foi planejado para organizar projetos em três categorias principais:

- **Pessoal** — projetos de portfólio e desenvolvimento pessoal
- **Acadêmico** — projetos desenvolvidos durante o curso de ADS no CEUB
- **Documentação** — arquivos de apoio e registros do projeto

### Estrutura de Diretórios

```
portfolio/
│
├── index.html              # Página principal do portfólio (GitHub Pages)
├── foto.jpg                # Foto de perfil utilizada no site
├── README.md               # Documentação principal do repositório
│
├── academico/              # Projetos acadêmicos do curso ADS
│   ├── logica-python/      # Exercícios de Lógica de Programação
│   │   └── README.md
│   └── banco-de-dados/     # Modelagem Entidade-Relacionamento
│       └── README.md
│
└── pessoal/                # Projetos pessoais e experimentos
    └── automacao/          # Estudos de automação com n8n
```

---

## 2. 💻 Criação e Versionamento do Projeto

### Projeto Inicial: Portfólio Web (Versão 1.0)

O projeto inicial criado é uma **página web de portfólio pessoal** desenvolvida inteiramente com HTML5 e CSS3, sem dependência de frameworks externos. O site é responsivo, com design dark moderno e animações em CSS puro.

### Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| HTML5 | Estrutura semântica da página |
| CSS3 | Estilização, animações e responsividade |
| Google Fonts | Tipografia (Syne + DM Sans) |
| Git | Versionamento local do código |
| GitHub | Hospedagem remota do repositório |
| GitHub Pages | Publicação do site estático |

### Histórico de Versões (Git)

| Versão | Commit | Descrição |
|---|---|---|
| 1.0 | `feat: versão 1.0` | Portfólio inicial com página web completa e documentação |

### Comandos Git Utilizados

```bash
# Inicialização e configuração
git init
git config --global user.name "José Orlando Vieira Xavier"
git config --global user.email "joseorlandovx@gmail.com"

# Primeiro commit — Versão 1.0
git add .
git commit -m "feat: versão 1.0 — portfólio inicial com página web e documentação"
git branch -M main
git remote add origin https://github.com/joseorlando-vx/portfolio.git
git push -u origin main
```

---

## 3. 📁 Organização e Documentação

### Estrutura da Página Web

O site é composto por **6 seções** com navegação por âncoras:

| Seção | Conteúdo |
|---|---|
| **Hero** | Apresentação com nome, foto, cargo e contatos |
| **Sobre mim** | Biografia completa e indicadores em destaque |
| **Experiência Profissional** | Histórico de cargos com empresa e período |
| **Projetos** | Iniciativas acadêmicas, pessoais e profissionais |
| **Habilidades** | Skills técnicas e comportamentais |
| **Contato** | Links para LinkedIn, GitHub e e-mail |

### Boas Práticas de Documentação Aplicadas

- ✅ README.md com seções bem definidas e formatação Markdown
- ✅ Badges informativos (GitHub Pages, LinkedIn, versão)
- ✅ Tabelas organizadas para tecnologias e requisitos
- ✅ Árvore de diretórios documentada
- ✅ Histórico de commits descritivo (padrão `feat:`)
- ✅ README individual em cada subpasta do projeto

---

## 4. 🌍 GitHub Pages

O site foi publicado gratuitamente através do **GitHub Pages**, acessível pelo link:

**[https://joseorlando-vx.github.io/portfolio](https://joseorlando-vx.github.io/portfolio)**

### Como foi configurado

1. Acessei o repositório no GitHub → **Settings → Pages**
2. Em *Source*, selecionei branch **main** e pasta **/ (root)**
3. Cliquei em **Save** — o GitHub gerou o link automaticamente
4. O site fica disponível publicamente sem custo algum

---

## 5. 🔗 Compartilhamento e Integração com LinkedIn

### Repositório Público

O repositório está configurado como **público** no GitHub, permitindo que qualquer pessoa acesse o código-fonte e o portfólio. O link direto é:

`https://github.com/joseorlando-vx/portfolio`

### Integração com LinkedIn

O repositório foi integrado ao perfil profissional do LinkedIn de duas formas:

1. **Seção "Projetos"** no LinkedIn — o portfólio foi adicionado como projeto com link direto para o GitHub Pages
2. **Perfil do GitHub** — o link do LinkedIn está vinculado diretamente no perfil do GitHub (Settings → Social accounts)
3. **README.md** — badge clicável do LinkedIn no topo da documentação

🔗 LinkedIn: [linkedin.com/in/joseorlandovieira](https://linkedin.com/in/joseorlandovieira)

---



## 🖥️ Como Visualizar Localmente

1. Clone o repositório:
```bash
git clone https://github.com/joseorlando-vx/portfolio.git
```

2. Abra a pasta clonada e dê duplo clique em `index.html`

Nenhuma instalação adicional é necessária — o site roda diretamente no navegador.

---

## 👤 Autor

<table>
  <tr>
    <td align="center">
      <b>José Orlando Vieira Xavier</b><br/>
      Analista Comercial · Estudante de ADS — CEUB<br/>
      Brasília, DF · 2026
    </td>
  </tr>
</table>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/joseorlandovieira)
[![GitHub](https://img.shields.io/badge/GitHub-joseorlando--vx-black?style=flat-square&logo=github)](https://github.com/joseorlando-vx)
[![E-mail](https://img.shields.io/badge/Email-joseorlandovx%40gmail.com-red?style=flat-square&logo=gmail)](mailto:joseorlandovx@gmail.com)

---

*Desenvolvido como parte do Desafio de Entrega Intermediária — ADS · CEUB · Maio 2026*
