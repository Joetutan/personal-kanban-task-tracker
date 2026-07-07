
import typer
from app.commands.add_task import app as add
from app.commands.list_task import app as list
from app.commands.delete_task import app as delete
from app.commands.mark_task import app as mark
from app.commands.update_task import app as update

app = typer.Typer()

app.add_typer(add)
app.add_typer(list)
app.add_typer(delete)
app.add_typer(mark)
app.add_typer(update)

if __name__ == "__main__":
    app()


