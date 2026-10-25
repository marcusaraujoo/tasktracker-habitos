# TaskTracker de Hábitos - Bootcamp II (Fase 3: Conteinerização)

O TaskTracker de Hábitos é uma aplicação em linha de comando (CLI) desenvolvida em Python para gerenciamento de rotinas diárias e metas.

Nesta Fase 3 (Entrega Final), a aplicação foi conteinerizada com Docker e orquestrada via Docker Compose para garantir a execução isolada em qualquer ambiente sem necessidade de instalação local do interpretador Python.

---

## 📂 Estrutura do Repositório

tasktracker-habitos/
├── .gitignore
├── Dockerfile              # Receita para construção da imagem Docker
├── docker-compose.yml      # Orquestração do container e interatividade CLI
├── README.md               # Documentação completa do projeto
├── docs/
│   └── planejamento_logico.pdf  # Arquitetura e planejamento da Fase 1
└── src/
    └── main.py             # Código-fonte principal em Python

---

## 🛠️ Tecnologias Utilizadas

- Linguagem: Python 3.11
- Conteinerização: Docker & Docker Compose
- Controle de Versão: Git & GitHub

---

## 🐳 Como Executar a Aplicação via Docker

Certifique-se de ter o Docker ou Docker Desktop instalado na máquina.

### Opção 1: Via Docker Compose (Recomendado)
Para rodar a aplicação em modo interativo via orquestrador:
docker compose run tasktracker

### Opção 2: Via Comandos Docker Nativos

1. Construir a imagem Docker:
   docker build -t tasktracker-image .

2. Executar o container em modo interativo:
   docker run -it --name tasktracker-container tasktracker-image

---

## 💻 Como Executar Localmente sem Docker

Caso queira executar diretamente via terminal local:
python src/main.py
