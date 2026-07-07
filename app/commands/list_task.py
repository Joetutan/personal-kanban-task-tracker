import typer
from rich.table import Table
from rich.console import Console
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository
from typing import Annotated

app = typer.Typer()
console = Console()

table = Table(title="Task Tracker")
table.add_column("ID")
table.add_column("Task")
table.add_column("Status")

@app.command()
def list(status: Annotated[TaskStatus | None, typer.Option("-f", "--filter", help="Filter by status: todo / done / in_progress")]=None):
    repo = TasksRepository()
    response = TaskManager(repo)
    tasks = response.list(status)
    tasks.sort()
    for task in tasks:
        table.add_row(f"{task[0]}", f"{task[1]}", f"{task[2]}")
    console.print(table)