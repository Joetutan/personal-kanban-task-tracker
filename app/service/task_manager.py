from app.repository.tasks_repository import TasksRepository
from app.models.task_model import Task
from app.models.task_model import TaskStatus

# service class
class TaskManager: 

    def __init__(self, repository: TasksRepository):
        self.repository = repository

    def add(self,title:str) -> Task:
        task = Task(id=0,title=title,status="TODO")
        return self.repository.add(task)
    
    def list(self, status: TaskStatus | None) -> list[Task]:
        return self.repository.list(status)
    
    def delete(self, id:int) -> str:
        return self.repository.delete(id)
    
    def delete_tasks(self, status:TaskStatus) -> str:
        return self.repository.delete_tasks(status)

    def update(self, id:int, title:str) -> Task:
        task = Task(id=id, title=title, status="")
        return self.repository.update(task)
    
    def mark(self, id: int, status:TaskStatus) -> Task:
        task = Task(id=id, title="", status=status)
        return self.repository.mark(task)

