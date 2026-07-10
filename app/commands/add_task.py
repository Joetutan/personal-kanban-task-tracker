import typer
from app.commands.cli_renderer import Cli
from app.service.task_manager import TaskManager
from app.repository.tasks_repository import TasksRepository

app = typer.Typer()

cli = Cli()

@app.command()
def add(title):
    repo = TasksRepository()
    response = TaskManager(repo)
    task = response.add(title)
    #print(task)
    cli.render_table([(task.id, task.title, task.status)])