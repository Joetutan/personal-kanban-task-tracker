import typer
from rich.console import Console
from typing import Annotated
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

console = Console()

@app.command()
def mark(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           status: Annotated[TaskStatus, typer.Option("-s", "--status", help="task status")] ):
    
    repo = TasksRepository()
    response = TaskManager(repo)
    message = response.mark(id, status)
    console.print(message)