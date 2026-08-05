from typing import Annotated

import typer
from app.cli.console import CliRenderer
from app.service.service_container import container

app = typer.Typer()
cli = CliRenderer()

@app.command()
def add(title: Annotated[str,typer.Option(...,"-a", "--add",help="Task title")]):

    task = container.task_service.add(title)
    cli.render_table([(task.id, task.title, task.status)])