import typer
from rich.table import Table
from rich.console import Console
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

console = Console()

table = Table(title="Task Tracker")

table.add_column("ID")
table.add_column("Task")
table.add_column("Status")


@app.command()
def add(title):
    repo = TasksRepository()
    response = TaskManager(repo)
    task = response.add(title)
    print(task)
    table.add_row(f"{task.id}", f"{task.title}", f"{task.status}")
    console.print(table)