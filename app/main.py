from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi import status

app = FastAPI()

# Modèle de données pour les tâches
class TaskBase(BaseModel):
    titre: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., max_length=255)
    statut: bool

class TaskCreate(TaskBase):
    pass  # Aucun champ supplémentaire pour la création

class Task(TaskBase):
    id: int

class TaskUpdate(BaseModel):
    statut: bool | None

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

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_create: TaskCreate):
    """
    Crée une nouvelle tâche.
    """
    # Génération automatique d'un ID
    task_id = max([t["id"] for t in tasks], default=0) + 1
    new_task = task_create.model_dump()  # Utilisation de dict() pour obtenir les données du modèle
    new_task["id"] = task_id

    tasks.append(new_task)
    return new_task

# Mettre à jour une tâche existante
@app.put("/tasks/{task_id}", response_model=Task, status_code=status.HTTP_200_OK)
def update_task(task_id: int, updated_task: Task):
    """
    Met à jour une tâche existante.
    """
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            # Mise à jour de la tâche dans la liste
            tasks[index] = updated_task.model_dump()  # Utilisez .dict() pour obtenir un dictionnaire de la tâche mise à jour
            return updated_task  # Retournez directement l'objet Task mis à jour
    raise HTTPException(status_code=404, detail="Task not found")


#Modifie partiellement une tâche, comme le changement de statut.
@app.patch("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_task_status(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if task_update.statut is not None:
                task["statut"] = task_update.statut
            return  # Pas de contenu à retourner pour un code 204
    raise HTTPException(status_code=404, detail="Task not found")



# Supprimer une tâche
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """
    Supprime une tâche par son ID.
    """
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return {"message": "Task deleted successfully"}
