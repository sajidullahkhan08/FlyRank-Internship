from typing import Protocol, List, Dict, Any
import asyncpg # We will install this

# 1. The Interface (Contract)
class TaskRepository(Protocol):
    async def create(self, title: str) -> Dict[str, Any]: ...
    async def get_all(self) -> List[Dict[str, Any]]: ...

# 2. The Old In-Memory Implementation (Keep this for reference/proof)
class InMemoryTaskRepository:
    def __init__(self):
        self._db = []
        self._counter = 1

    async def create(self, title: str) -> Dict[str, Any]:
        task = {"id": self._counter, "title": title}
        self._counter += 1
        self._db.append(task)
        return task

    async def get_all(self) -> List[Dict[str, Any]]:
        return self._db

# 3. The New Postgres Implementation
class PostgresTaskRepository:
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        # Creates a connection pool to the database
        self.pool = await asyncpg.create_pool(self.dsn)

    async def create(self, title: str) -> Dict[str, Any]:
        async with self.pool.acquire() as connection:
            row = await connection.fetchrow(
                "INSERT INTO tasks (title) VALUES ($1) RETURNING id, title",
                title
            )
            return dict(row)

    async def get_all(self) -> List[Dict[str, Any]]:
        async with self.pool.acquire() as connection:
            rows = await connection.fetch("SELECT id, title FROM tasks ORDER BY id")
            return [dict(row) for row in rows]