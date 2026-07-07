import typer
from rich.table import Table
from rich.console import Console
from typing import Annotated
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

console = Console()

@app.command()
def delete(id: Annotated[int | None, typer.Option("-i", "--id", help="delete task by id")]=None,
           status: Annotated[TaskStatus | None, typer.Option("-s", "--status", help="delete multiple tasks by status")]=None ):
    
    if (id is not None) and (status is not None):
        raise typer.Badparameter( "filter by either --id or --status, not both.")
    
    if (id is None) and (status is None):
        raise typer.Badparameter("Specify filter by either --id or --status.")
    
    repo = TasksRepository()
    response = TaskManager(repo)
    if status is None:
        message = response.delete(id)
    else:
        message = response.delete_tasks(status)

    console.print(message)