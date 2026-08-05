from typing import Annotated

import typer
from app.cli.console import CliRenderer
from app.models.task_model import TaskStatus
from app.service.service_container import container

app = typer.Typer()
cli = CliRenderer()

@app.command()
def list(status: Annotated[TaskStatus | None, typer.Option("-f", "--filter", help="Filter by status: todo / done / in_progress")]=None):
    
    tasks = container.task_service.list(status)
    cli.render_table(tasks)