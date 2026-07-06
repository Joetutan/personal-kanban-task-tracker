from app.models.task_model import TaskStatus
import argparse

# argument parser
class ArgumentParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="A simple cli task tracker")
        self.subparsers = self.parser.add_subparsers(dest="command", required=True)
        self.configure()
    
    def configure(self):

        self.configure_add()
        self.configure_list()
        self.configure_delete()
        self.configure_mark()
        self.configure_update()
    
    def parse(self):
        return self.parser.parse_args()
    
    def configure_add(self):
        parser = self.subparsers.add_parser("add", help="create new task")
        parser.add_argument("-t", "--title", required=True, help="task title")
        

    def configure_list(self):
        parser=self.subparsers.add_parser("list", help="list all tasks")
        parser.add_argument("-s","--status", type=TaskStatus, default=None, help="filter by status")
        
    def configure_delete(self):
        parser = self.subparsers.add_parser("delete", help="Delete a task")
        parser.add_argument("-i","--id", type=int, help="task ID")

    def configure_update(self):
        parser = self.subparsers.add_parser("update", help="update task")
        parser.add_argument("-i","--id", type=int, help="task ID")
        parser.add_argument("-t", "--title", required=True, help="task title")

    def configure_mark(self):
        parser = self.subparsers.add_parser("mark", help="Mark task TODO/IN_PROGRESS/DONE")
        parser.add_argument("-i","--id", type=int, help="task ID")
        parser.add_argument("-s","--status", type=TaskStatus, help="task status")

    #def configure_exit(self):
    #    self.subparsers.add_parser("exit", help="end session")