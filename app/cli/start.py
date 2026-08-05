import shlex
import traceback

from rich.console import Console
from typer.main import get_command


class InteractiveShell:

    def __init__(self, app):
        self.cli = get_command(app)
        self.console = Console()
    
    def start_shell(self):
        
        while True:
            
            raw = self.console.input("[bold cyan]Kanban >>  [/bold cyan]")
            if not raw:
                continue
            if raw in {"exit", "quit", "q"}:
                break
            args = shlex.split(raw)
            try:
                self.cli.main(args=args, prog_name="vault", standalone_mode=False,)
            except Exception as e:  # noqa: BLE001
                #self.console.print(f"[red]{e}[/red]")
                traceback.print_exc(e)