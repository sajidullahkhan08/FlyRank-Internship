## BE-04: Containerized Stack

### Architecture Proof (The Swap)

The application uses the **Repository Pattern**. The `TaskService` and FastAPI routes in `main.py` remain completely unchanged. We simply swapped the dependency injection from `InMemoryTaskRepository` to `PostgresTaskRepository` in `main.py`, proving that storage logic is cleanly decoupled from business logic.

### Persistence Proof

Data persistence was verified with the following steps:

1. Started stack: `docker compose up -d`
2. Created a task: `curl -X POST "http://localhost:8000/tasks?title=PersistentTask"`
3. Restarted both app and database containers: `docker compose restart app db`
4. Fetched tasks: `curl http://localhost:8000/tasks`
5. **Result:** The task remained intact, proving the Docker named volume (`postgres_data`) successfully survived the container restart.

### Stretch Goals Completed

- Added **Redis** to `docker-compose.yml` with a health check.
- Added `/ping-redis` endpoint to verify app-to-Redis connectivity.
- Added a database index (`idx_tasks_title`) in `init.sql` for optimized title lookups.
