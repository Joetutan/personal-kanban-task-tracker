from app.repository.task_repository import TaskRepository
#from app.models.task import Task
#from app.models.task import TaskStatus

# service class
class TaskManager: 

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add(self,title):
        self.repository.add(title)
    
    def update(self, task_id, title):
        self.repository.update(task_id, title)
    
    def mark(self, status, task_id):
        self.repository.mark(task_id,status)
    
    def list(self, status):
        return self.repository.list(status)
    
    def delete(self, task_id):
        self.repository.delete(task_id)
