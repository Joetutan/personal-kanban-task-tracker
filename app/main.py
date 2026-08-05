
import typer
from app.cli.commands.add_task import app as add
from app.cli.commands.delete_task import app as delete
from app.cli.commands.list_task import app as list
from app.cli.commands.mark_task import app as mark
from app.cli.commands.update_task import app as update
from app.cli.start import InteractiveShell

app = typer.Typer()

app.add_typer(add)
app.add_typer(list)
app.add_typer(delete)
app.add_typer(mark)
app.add_typer(update)


def main():
    InteractiveShell(app).start_shell()

if __name__ == "__main__":
    main()
