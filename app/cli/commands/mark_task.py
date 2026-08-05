from typing import Annotated

import typer
from app.cli.console import CliRenderer
from app.models.task_model import TaskStatus
from app.service.service_container import container

app = typer.Typer()
cli = CliRenderer()

@app.command()
def mark(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           status: Annotated[TaskStatus, typer.Option("-s", "--status", help="task status")] ):
    task = container.task_service.mark(id, status)
    cli.render_table([(task.id, task.title, task.status)])
