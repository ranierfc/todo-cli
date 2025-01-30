# To-Do List CLI

Uma aplicação de linha de comando para gerenciar tarefas, com persistência em JSON.

## Como usar

```bash
# Adicionar tarefa
python src/cli.py --add "Estudar Python"

# Listar tarefas
python src/cli.py --list

# Listar tarefas concluídas
python src/cli.py --list --filter completed

# Listar tarefas pendentes
python src/cli.py --list --filter pending

# Remover tarefa (por índice)
python src/cli.py --remove 0

# Marcar tarefa como concluída (por índice)
python src/cli.py --complete 0
```

## Requisitos

- Python 3.8+