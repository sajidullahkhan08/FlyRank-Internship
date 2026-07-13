import os
from fastapi import FastAPI
from service import TaskService
from repository import PostgresTaskRepository, InMemoryTaskRepository

app = FastAPI()

# THE SWAP: Comment out InMemory, uncomment Postgres
# repo = InMemoryTaskRepository() 
repo = PostgresTaskRepository(os.getenv("DATABASE_URL", "postgresql://flyrank:flyrank_password@localhost:5432/flyrank_db"))

service = TaskService(repo)

@app.on_event("startup")
async def startup():
    # If using Postgres, we need to establish the connection pool on startup
    if isinstance(repo, PostgresTaskRepository):
        await repo.connect()

@app.get("/")
def read_root():
    return {"message": "BE-04: Containerized Stack with Postgres"}

@app.post("/tasks")
async def create_task(title: str):
    return await service.add_task(title)

@app.get("/tasks")
async def get_tasks():
    return await service.list_tasks()

# --- STRETCH GOAL: Redis Ping ---
import redis.asyncio as redis
redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379/0"))

@app.get("/ping-redis")
async def ping_redis():
    await redis_client.set("ping", "pong")
    result = await redis_client.get("ping")
    return {"redis_status": result.decode("utf-8")}