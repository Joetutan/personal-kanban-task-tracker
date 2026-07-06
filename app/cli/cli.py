from app.cli.argument_parser import ArgumentParser
from app.service.task_manager import TaskManager

# Entry/Boundary class

class Cli:
    def __init__(self,parser: ArgumentParser, service: TaskManager):
        self.parser = parser
        self.service = service

    def run(self):
        args = self.parser.parse()
        self.process(args)
    
    def process(self, args):

        match args.command:
                case "add":
                    self.service.add(args.title)
                    #self.display_success("Task added.")
                case "list":
                    tasks = self.service.list(args.status)
                    tasks.sort()
                    for i,t,c in tasks:
                        print(f"\n{i} | {t} | {c} |")
                case "update":
                    self.service.update(args.id, args.title)
                case "mark":
                    self.service.mark(args.status, args.id)
                case "delete":
                    self.service.delete(args.id)
                case _:
                    print("unknown command")