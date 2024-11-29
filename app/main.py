from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

# Récupérer toutes les tâches
@app.get("/tasks")
def get_all_tasks():
    """
    Retourne toutes les tâches.
    """
    return {"tasks": tasks}

# Récupérer une tâche spécifique par son ID
@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    """
    Retourne une tâche spécifique par son ID.
    """
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return {"task": task}
    raise HTTPException(status_code=404, detail="Task not found")

# Créer une nouvelle tâche
@app.post("/tasks")
def create_task(task: Task):
    """
    Crée une nouvelle tâche.
    """
    if any(existing_task["id"] == task.id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="Task with this ID already exists")
    tasks.append(task.dict())
    return {"message": "Task created successfully", "task": task}

# Mettre à jour une tâche existante
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    """
    Met à jour une tâche existante.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task.dict()
            return {"message": "Task updated successfully", "task": updated_task}
    raise HTTPException(status_code=404, detail="Task not found")

# Modifier partiellement une tâche (par exemple, changer le statut)
@app.patch("/tasks/{task_id}")
def update_task_status(task_id: int, statut: bool):
    """
    Modifie partiellement une tâche, comme le changement de statut.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["statut"] = statut
            return {"message": "Task status updated successfully", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

# Supprimer une tâche
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Supprime une tâche par son ID.
    """
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted successfully"}
