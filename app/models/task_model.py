from enum import Enum

class TaskStatus(Enum):
        DONE = "DONE"
        IN_PROGRESS = "IN_PROGRESS"
        TODO = "TODO"

# data model class
class Task:

    def __init__(self, id, title, status: TaskStatus):
        self.id = id
        self.title = title
        self.status = status