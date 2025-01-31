# To-Do List CLI

Uma aplicação de linha de comando para gerenciar tarefas, com persistência em JSON.

## Como usar

```bash
# Adicionar tarefa
python src/cli.py --add "Estudar Python"

# Adicionar tarefa com prioridade alta
python src/cli.py --add "Corrigir bug crítico" --priority alta

# Listar tarefas
python src/cli.py --list

# Listar tarefas com detalhes
python src/cli.py --list --verbose

# Listar tarefas de prioridade alta
python src/cli.py --list --filter-priority alta

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

### Importante

Ao usar filtros (`--filter`, `--created-before`, etc.), os índices exibidos são **reais** (referentes à lista completa).
Use esses índices para remover/editar tarefas, mesmo após filtrar.

## Requisitos

- Python 3.8+