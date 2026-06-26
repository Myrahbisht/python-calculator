from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Welcome to Tast API"}

@app.get("/tasks")
def get_tasks():
    return{"tasks": tasks}

@app.post("/tasks")
def add_task(task: dict):
    tasks.append(task)
    return{"message": "Task Added", "task": task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        removed = tasks.pop(task_id)
        return{"message": "Deleted", "task": removed}
    return {"error": "Task not found"}