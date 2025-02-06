from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

# Define the task model
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# In-memory storage for tasks
TASKS_FILE = 'memory.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

@app.on_event("startup")
def startup_event():
    if not os.path.exists(TASKS_FILE):
        save_tasks([])

@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks = load_tasks()
    task.id = len(tasks) + 1
    tasks.append(task.dict())
    save_tasks(tasks)
    return task

@app.get("/tasks/", response_model=List[Task])
def get_tasks():
    tasks = load_tasks()
    return tasks

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    tasks = load_tasks()
    task_to_delete = next((task for task in tasks if task['id'] == task_id), None)
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task_to_delete)
    save_tasks(tasks)
    return task_to_delete