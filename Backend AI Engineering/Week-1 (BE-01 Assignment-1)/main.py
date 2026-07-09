from fastapi import FastAPI

# Initialize the FastAPI application
app = FastAPI()

# Endpoint 1: The Root Route
@app.get("/")
def read_root():
    return {
        "message": "Hello from FlyRank Backend!",
        "assignment": "BE-01",
        "status": "success"
    }

# Endpoint 2: A Second Route
@app.get("/intern")
def read_intern():
    return {
        "track": "Backend AI Engineering",
        "week": 1,
        "learning": "Request-Response Loop"
    }