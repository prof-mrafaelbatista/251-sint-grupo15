Projeto Final - Fundamentos de Programação em Python Aluna: Maria Gabriele Araújo Gonçalves Turma: SPI P1 - Noite

🎯 Objetivo Geral Desenvolver uma aplicação web interativa utilizando o framework Flask, com o propósito de criar um site informativo sobre os fundamentos da programação em Python.

O projeto inclui:

Uma funcionalidade de perguntas e respostas integrada com a API do Gemini.

Um dicionário interativo de termos relacionados à programação.

✅ Requisitos do Projeto 🏗️ Estrutura Flask Utilização do framework Flask para:

Criação de rotas

Utilização de templates

Manipulação de dados via formulários

👥 Página Sobre a Equipe Apresentação dos integrantes do grupo

Nomes, redes sociais profissionais e informações relevantes

📚 Conteúdo do Site Seções explicativas sobre fundamentos da programação em Python:

Estruturas de seleção

Estruturas de repetição

Vetores e matrizes

Funções e procedimentos

Tratamento de exceções

Cada seção contém conceito, aplicações práticas e exemplos de código.

💡 Seção de Tirar Dúvidas (API Gemini) Permite que o usuário envie perguntas.

Recebe e exibe respostas diretamente da API do Gemini.

📖 Dicionário de Termos Visualização dos termos e suas definições

Funcionalidade para:

Adicionar novos termos

Editar definições existentes

Remover termos

Persistência dos dados via arquivo CSV

🎨 Interface de Usuário Navegação clara e intuitiva

Design amigável com auxílio do Bootstrap

🗺️ Estrutura do Site Página Inicial: Visão geral do projeto e navegação

Sobre a Equipe: Informações dos integrantes

Conteúdo Python: Material didático sobre fundamentos de Python

Chat IA: Perguntas e respostas via API Gemini

Glossário: Dicionário interativo de termos de programação

Gerenciamento de Glossário: Adicionar, editar e remover termos

🛠️ Tecnologias Utilizadas Linguagem: Python 3.13

Framework Web: Flask

Front-end: HTML + Bootstrap

Persistência: Arquivo CSV (bd_glossario.csv)

API Externa: Gemini (para chatbot IA)

🔗 Integração com a API do Gemini O usuário envia uma pergunta por meio de um formulário.

O Flask processa a requisição e envia para a API do Gemini.

A resposta da API é exibida diretamente na interface do site.

⚠️ Observação: Para funcionamento externo da API Gemini, é necessário inserir uma API Key válida.

🧠 Principais Componentes do Código app.py Define as rotas do site:

/ (index)

/sobre

/conteudo

/chat (Chat IA)

/glossario

/adicionar

/editar/

/remover/

Gerencia:

Leitura e escrita do glossário (bd_glossario.csv)

Comunicação com a API do Gemini

bd_glossario.csv Banco de dados simples que armazena os termos e definições do glossário

templates/ Arquivos HTML responsáveis pelas páginas do site

static/ Arquivos estáticos como imagens, CSS e scripts adicionais

🚀 Observações Finais O projeto prioriza a usabilidade, a clareza das informações e a facilidade de navegação.

O Bootstrap foi utilizado para garantir um design responsivo e moderno.
