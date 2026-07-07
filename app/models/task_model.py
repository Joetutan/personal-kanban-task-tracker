from enum import Enum

class TaskStatus(Enum):
        DONE = "done"
        IN_PROGRESS = "in_progress"
        TODO = "todo"

# data model class
class Task:

    def __init__(self, id, title, status: TaskStatus):
        self.id = id
        self.title = title
        self.status = status