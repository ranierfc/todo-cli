# To-Do List CLI

Uma aplicação de linha de comando para gerenciar tarefas, com persistência em JSON.

## Como usar

```bash
# Adicionar tarefa
python src/cli.py --add "Estudar Python"

# Listar tarefas
python src/cli.py --list

# Listar tarefas com detalhes
python src/cli.py --list --verbose

# Listar tarefas concluídas
python src/cli.py --list --filter completed

# Listar tarefas pendentes
python src/cli.py --list --filter pending

# Filtrar tarefas criadas antes de uma data
python src/cli.py --list --created-before 2025-01-31

# Filtrar tarefas concluídas após uma data
python src/cli.py --list --completed-after 2025-01-31

# Remover tarefa (por índice)
python src/cli.py --remove 0

# Marcar tarefa como concluída (por índice)
python src/cli.py --complete 0
```

## Requisitos

- Python 3.8+