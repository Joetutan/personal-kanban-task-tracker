
from app.cli.cli import Cli
from app.repository.postgres_repo import PostgresRepository
from app.service.task_manager import TaskManager
from app.cli.argument_parser import ArgumentParser

#from app.todo_app import CLI, TaskRepository, TaskManager, ArgumentParser
def main():

    repository = PostgresRepository()

    service = TaskManager(repository)

    parser = ArgumentParser()

    cli = Cli(parser, service)
    
    cli.run()

if __name__ == "__main__":
    main()


