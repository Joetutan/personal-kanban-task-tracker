import typer
from typing import Annotated
from app.commands.cli_renderer import Cli
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

cli = Cli()
@app.command()
def mark(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           status: Annotated[TaskStatus, typer.Option("-s", "--status", help="task status")] ):
    
    repo = TasksRepository()
    response = TaskManager(repo)
    task = response.mark(id, status)
    cli.render_table([(task.id, task.title, task.status)])
