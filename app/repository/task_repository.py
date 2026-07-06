
from abc import ABC, abstractmethod
from app.models.task_model import Task

# repository class

class TaskRepository(ABC):

    @abstractmethod
    def add(self, task: Task) -> None:
        ...
    @abstractmethod
    def mark(self, task_id: int) -> Task|None:
        ...
    @abstractmethod
    def list(self)-> list[Task]:
        ...
    @abstractmethod
    def update(self, task: Task) -> None:
        ...
    @abstractmethod
    def delete(self, task_id: int) -> None:
        ...



    ...
'''
class InMemoryRepository(TaskRepository):

    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add(self, task: Task):
        task.id =self.next_id
        self.tasks[self.next_id] = task
        self.next_id +=1
    
    def get(self, task_id):
        return self.task.get(task_id)
    
    def list(self):
        return list((k,v) for k,v in self.tasks.items())
    
    def update(self, task):
        self.tasks[task.id] = task
    
    def delete(self, task_id):
        self.tasks.pop(task_id, None)


class JsonRepository(TaskRepository):
    
    def __init__(self, filename):
        self.filename = filename
    
    #Serialize and deserialize
'''