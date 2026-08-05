from typing import Annotated

import typer
from app.cli.console import CliRenderer
from app.service.service_container import container

app = typer.Typer()
cli = CliRenderer()

@app.command()
def update(id: Annotated[int , typer.Option("-i", "--id", help=" task by id")],
           title: Annotated[str, typer.Option("-t", "--title", help="task title")] ):
    task = container.task_service.update(id,title)
    cli.render_table([(task.id, task.title, task.status)])