from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pytest import Session

app = FastAPI()

# Modèle de données pour les tâches
class Task(BaseModel):
    id: int
    titre: str
    description: str
    statut: bool

# Exemple de base de données en mémoire
tasks = [
    {"id": 1, "titre": "Task 1", "description": "First task", "statut": True},
    {"id": 2, "titre": "Task 2", "description": "Second task", "statut": False},
]

# Route de base
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Récupérer toutes les tâches
@app.get("/tasks")
def get_all_tasks():
    return {"tasks": tasks}

# Récupérer une tâche spécifique par son ID
@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return {"task": task}
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    return {"task_title": task.title, "task_id": task_id}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with Session(engine) as session: # type: ignore
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Hero not found")
        session.delete(task)
        session.commit()
        return {"ok": True}
