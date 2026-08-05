from rich.console import Console
from rich.table import Table


class CliRenderer:
    def __init__(self):
        self.console = Console()

    def render_message(self, message:str):
        self.console.print(message)
    
    def render_table(self, tasks:list):
        table = Table(title="Task Tracker")
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Status")
        #table.add_column("Priority")
        tasks.sort()
        for id, title, status in tasks:
            if status == "DONE":
                table.add_row(f"{id}", f"{title}", f"[green]{status}[/green]")
            else:
                table.add_row(f"{id}", f"{title}", f"{status}")

        self.console.print(table)