from repository import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def add_task(self, title: str):
        return await self.repository.create(title)

    async def list_tasks(self):
        return await self.repository.get_all()