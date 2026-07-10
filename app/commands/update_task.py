import typer
from typing import Annotated
from app.commands.cli_renderer import Cli
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()
cli = Cli()

@app.command()
def update(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           title: Annotated[str, typer.Option("-t", "--title", help="task title")] ):
    repo = TasksRepository()
    response = TaskManager(repo)
    task = response.update(id,title)
    cli.render_table([(task.id, task.title, task.status)])