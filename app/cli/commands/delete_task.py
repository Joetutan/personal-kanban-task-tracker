from typing import Annotated

import typer
from app.cli.console import CliRenderer
from app.models.task_model import TaskStatus
from app.service.service_container import container

app = typer.Typer()
cli = CliRenderer()

@app.command()
def delete(id: Annotated[int | None, typer.Option(...,"-i", "--id", help="delete task by id")],
           status: Annotated[TaskStatus | None, typer.Option("-s", "--status", help="delete multiple tasks by status")]=None ):
    
    if status is None:
        message = container.task_service.delete(id)
    else:
        message = container.task_service.delete_tasks(status)
    if message: 
        cli.render(message)