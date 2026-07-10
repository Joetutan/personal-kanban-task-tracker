from rich.console import Console
from rich.table import Table

class Cli:
    def __init__(self):
        self.console = Console()
        self.table = Table(title="Task Tracker")

    def render_message(self, message:str):
        self.console.print(message)
    
    def render_table(self, tasks:list):
        table = self.table
        table.add_column("ID")
        table.add_column("Title")
        table.add_column("Status")
        #table.add_column("Priority")
        tasks.sort()
        for id, title, status in tasks:
            table.add_row(f"{id}", f"{title}", f"{status}")

        self.console.print(table)
    