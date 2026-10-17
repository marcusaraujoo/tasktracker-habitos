# TaskTracker de Hábitos - Bootcamp II (Fase 2)

O **TaskTracker de Hábitos** é uma aplicação em linha de comando (CLI) desenvolvida em Python para gerenciamento e acompanhamento de rotinas e metas diárias. 

Este projeto faz parte da **Fase 2 (Entrega Intermediária)** da disciplina Bootcamp II, promovendo a migração do planejamento lógico arquitetural para uma implementação prática com controle de versão via Git e publicação no GitHub.

---

## 🎯 Funcionalidades Principais

- **Cadastro de Hábitos:** Permite cadastrar hábitos com validações estritas de entrada.
- **Validação de Título:** Impede o cadastro de hábitos sem nome ou com espaços em branco.
- **Validação de Prioridade:** Garante a classificação estrita entre *Alta*, *Média* e *Baixa*.
- **Prevenção de Duplicidade:** Evita o cadastro de hábitos duplicados no mesmo dia.
- **Acompanhamento de Progresso:** Exibe os hábitos cadastrados, detalhes e o progresso de hábitos concluídos.
- **Marcação de Conclusão:** Permite alterar o status de um hábito de *Pendente* para *Concluído*.

---

## 📂 Estrutura do Repositório

```plaintext
tasktracker-habitos/
├── README.md               # Documentação principal e guia de uso
├── .gitignore              # Regras para ignorar arquivos temporários do Python
├── docs/
│   └── planejamento_logico.pdf  # Planejamento lógico e arquitetura da Fase 1
└── src/
    └── main.py             # Código-fonte principal da aplicação em Python
