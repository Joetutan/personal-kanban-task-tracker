
from app.repository.tasks_repository import TasksRepository
from app.service.task_service import TaskService


class ServiceContainer:

    def __init__(self):
        self.repository = TasksRepository()
        self.task_service = TaskService(repository=self.repository)

container = ServiceContainer()