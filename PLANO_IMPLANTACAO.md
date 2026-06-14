# Plano de Implantação — PortfolioHUB + IA GEMINI

**Autor:** José Orlando Vieira Xavier  
**Matrícula:** 22610685  
**Curso:** Análise e Desenvolvimento de Sistemas — CEUB  
**Disciplina:** Bootcamp 1 — Prof. Marcelo Carboni  
**Data:** Junho de 2026  

---

## 1. Introdução

O **PortfolioHUB** é uma plataforma centralizada para exibição e gerenciamento de projetos acadêmicos e profissionais, desenvolvida ao longo do semestre letivo de 2026. O Google Gemini foi utilizado como assistente de IA em todas as etapas da implantação — desde o planejamento até os testes finais.

- **Portfólio ao vivo:** [joseorlando-vx.github.io/Portfolio](https://joseorlando-vx.github.io/Portfolio)
- **Repositório:** [github.com/joseorlando-vx/Portfolio](https://github.com/joseorlando-vx/Portfolio)
- **Google Sites (V1):** [sites.google.com/view/joseorlandovx](https://sites.google.com/view/joseorlandovx)

---

## 2. Configuração do Google Gemini como Guia

O Gemini foi configurado como assistente técnico logo no início do projeto, com o seguinte prompt de configuração:

> **Prompt:** "Atue como meu assistente técnico e consultor de implantação de sistemas. Seu papel: guiar decisões técnicas, validar segurança, sugerir melhores práticas de GitHub e Google Workspace, documentar cada etapa e apoiar em testes. O projeto é avaliado em: Implementação, Segurança, Documentação, Colaboração e Apresentação."

O Gemini confirmou o papel e passou a atuar em cinco frentes:
1. Orientação em decisões arquiteturais
2. Validação de políticas de segurança
3. Recomendação de melhores práticas (GitHub, Google Workspace)
4. Apoio na documentação técnica
5. Suporte em testes de produção

---

## 3. Cronograma de Implantação

| Etapa | Período | Objetivos | Ferramentas | Uso do Gemini | Status |
|-------|---------|-----------|-------------|---------------|--------|
| 1. Concepção | Abr/2026 | Identidade visual, 6 seções obrigatórias | Google Sites, Docs | Sugestões de estrutura e design | ✅ |
| 2. Protótipo V1 | Abr/2026 | Publicação no Google Sites, vídeo YouTube | Sites, OBS, YouTube | Revisão do conteúdo do portfólio | ✅ |
| 3. Migração | Mai/2026 | Desenvolvimento HTML5/CSS3 | VS Code, GitHub Desktop | Orientação sobre estrutura de pastas | ✅ |
| 4. Versionamento | Mai/2026 | GitHub Pages, LinkedIn, README | Git, GitHub Pages | Boas práticas de Git e README | ✅ |
| 5. Segurança | Jun/2026 | 2FA, SSH, branch protection | GitHub Security | Definição das políticas de segurança | ✅ |
| 6. Documentação | Jun/2026 | Documentação final, testes, vídeo | Docs, YouTube | Checklist de produção e revisão | ✅ |

---

## 4. Uso do Gemini em Cada Etapa

### 4.1 Planejamento — Prompt de Planejamento

> **Prompt:** "Preciso implantar um portfólio pessoal no GitHub Pages. Gere um plano detalhado de 6 etapas incluindo segurança, controle de versão e boas práticas de colaboração."

**Como o Gemini ajudou:** sugeriu a divisão em 6 fases (concepção → protótipo → migração → versionamento → segurança → documentação), recomendou o uso de branches separadas (main/dev) e alertou sobre a necessidade de branch protection desde o início.

### 4.2 Google Workspace — Prompt de Integração

> **Prompt:** "Como integrar as funcionalidades do Google Workspace (Drive, Calendar, Gmail) em um portfólio publicado via GitHub Pages?"

**Como o Gemini ajudou:** apresentou 4 opções de integração (iframes, APIs, Apps Script e links diretos), com vantagens e desvantagens de cada uma. Optei por links diretos por ser a solução mais simples e segura para um site estático.

### 4.3 Segurança — Prompt de Políticas

> **Prompt:** "Quais são as melhores práticas de segurança para um repositório GitHub público que hospeda um portfólio pessoal? Considere autenticação, tokens, proteção de branches e conformidade com normas atuais."

**Como o Gemini ajudou:** gerou uma política completa cobrindo 5 áreas:
1. **Gerenciamento de Acesso:** senhas fortes, 2FA obrigatório, princípio do menor privilégio
2. **Proteção de Dados:** classificação, DLP, backups regulares
3. **Conformidade:** LGPD, ISO 27001, NIST Cybersecurity Framework
4. **Treinamento:** conscientização sobre phishing e engenharia social
5. **Monitoramento:** logs de atividades, plano de resposta a incidentes

Ferramentas recomendadas: Google Admin Console, Security Center, Vault e Endpoint Verification.

### 4.4 GitHub — Prompt de Versionamento

> **Prompt:** "Quais as melhores práticas para usar Git e GitHub em um projeto de portfólio individual?"

**Como o Gemini ajudou:** recomendou commits semânticos (feat:, fix:, docs:), uso de branches para cada funcionalidade, Pull Requests mesmo em projeto solo, Issues para rastreamento, GitHub Projects como kanban, e README.md completo com badges.

### 4.5 Testes — Prompt de Checklist

> **Prompt:** "Liste os pontos de verificação essenciais antes de lançar um portfólio no GitHub Pages em produção. Inclua links, SEO, responsividade, segurança e performance."

**Como o Gemini ajudou:** gerou um checklist de 10 pontos que foi aplicado integralmente:

- [x] GitHub Pages ativo e acessível
- [x] URL funcionando
- [x] Links internos testados
- [x] Imagens carregando (sem 404)
- [x] Meta tags SEO configuradas
- [x] Responsividade mobile testada
- [x] Nenhuma credencial no repositório
- [x] README.md atualizado
- [x] Commits limpos e semânticos
- [x] Branch protection ativa

### 4.6 Revisão de Código — Prompt de Qualidade

> **Prompt:** "Revise meu código HTML/CSS e sugira melhorias de acessibilidade (WCAG 2.1), performance (Core Web Vitals) e SEO."

**Como o Gemini ajudou:** sugeriu conversão de imagens para WebP, lazy loading, meta tags completas (title, description, og:image), sitemap.xml e robots.txt. As sugestões de maior impacto foram implementadas antes do lançamento.

### 4.7 Uso como Ferramenta de Suporte

> **Prompt:** "Como posso usar o Google Gemini de forma eficiente como guia e ferramenta de suporte durante a implantação?"

**Como o Gemini ajudou:** orientou a ser específico nas perguntas, experimentar abordagens diferentes, gerar conteúdo (textos, scripts, códigos), documentar todas as interações para consulta posterior, e considerar a integração do Gemini ao PortfolioHUB como chatbot ou sistema de recomendação.

---

## 5. Políticas de Segurança Implementadas

| Prática | Status |
|---------|--------|
| Autenticação 2FA via app autenticador | ✅ Implementado |
| Chave SSH Ed25519 | ✅ Implementado |
| Tokens PAT com escopo limitado e expiração 90 dias | ✅ Implementado |
| Nenhuma credencial commitada | ✅ Implementado |
| Dependabot para alertas de vulnerabilidades | ✅ Habilitado |
| Branch protection na main (exige PR, proíbe force push) | ✅ Implementado |
| Licença MIT | ✅ Implementado |
| .gitignore configurado | ✅ Implementado |

---

## 6. Estrutura do Repositório

```
Portfolio/
├── index.html              ← Página principal
├── README.md               ← Documentação com badges
├── PLANO_IMPLANTACAO.md    ← Este documento
├── LICENSE                 ← MIT License
├── .gitignore
├── academico/
│   └── logica-python/
│       ├── exercicios.py
│       └── README.md
└── pessoal/
    └── README.md
```

---

## 7. Controle de Versão

- **Branches:** `main` (produção) e `dev` (desenvolvimento)
- **Commits semânticos:** `feat:`, `fix:`, `docs:`, `style:`
- **Pull Requests:** revisão antes de merge na main
- **Tags:** v1.0, v1.1 etc.

---

## 8. Gerenciamento de Riscos

| Risco | Mitigação |
|-------|-----------|
| Atraso nas entregas | Cronograma com margens de segurança |
| Falha de integração | Testes incrementais a cada etapa |
| Vazamento de credenciais | .gitignore + PAT com expiração |
| Perda de dados | Histórico Git como backup |
| Incompatibilidade mobile | Testes em DevTools + dispositivo real |

---

## 9. Considerações Finais

O Google Gemini atuou como parceiro técnico em todas as etapas — do planejamento à produção. Cada recomendação foi analisada criticamente antes de ser aplicada, garantindo que as decisões técnicas fossem fundamentadas e adequadas ao contexto real do projeto.

O PortfolioHUB está em produção, acessível publicamente, versionado e continuamente atualizável.

---

**Contato:** jose.orlandox@sempreceub.com  
**LinkedIn:** linkedin.com/in/joseorlandovieira  
**GitHub:** github.com/joseorlando-vx
