import typer
from app.commands.cli_renderer import Cli
from app.models.task_model import TaskStatus
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository
from typing import Annotated

app = typer.Typer()

cli = Cli()

@app.command()
def list(status: Annotated[TaskStatus | None, typer.Option("-f", "--filter", help="Filter by status: todo / done / in_progress")]=None):
    repo = TasksRepository()
    response = TaskManager(repo)
    tasks = response.list(status)
    cli.render_table(tasks)