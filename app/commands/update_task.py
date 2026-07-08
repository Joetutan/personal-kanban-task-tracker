import typer
from rich.table import Table
from rich.console import Console
from typing import Annotated
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

console = Console()

table = Table(title="Task Tracker")

table.add_column("ID")
table.add_column("Task")
table.add_column("Status")


@app.command()
def update(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           title: Annotated[str, typer.Option("-t", "--title", help="task title")] ):
    repo = TasksRepository()
    response = TaskManager(repo)
    task = response.update(id,title)
    table.add_row(f"{task.id}", f"{task.title}", f"{task.status}")
    console.print(table)