import sys
import os

# Ajouter le répertoire racine (où se trouve 'app') au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_get_tasks():
    """Teste la route qui affiche toutes les tasks"""
    response = client.get("/tasks")
    assert response.status_code == 200

    tasks = [
    {"id": 1, "titre": "Task 1", "description": "First task", "statut": True},
    {"id": 2, "titre": "Task 2", "description": "Second task", "statut": False},
]
    assert response.json().get("tasks") == tasks


def test_get_one_tasks():
    """Teste la route qui affiche qu'une task"""
    response = client.get("/tasks/1")
    assert response.status_code == 200

    expected_task = {"id": 1, "titre": "Task 1", "description": "First task", "statut": True}
    assert response.json().get("task") == expected_task

def test_create_task():
    """Teste la création d'une nouvelle tâche sans fournir d'ID."""
    new_task = {"titre": "Task 3", "description": "Third task", "statut": False}
    response = client.post("/tasks", json=new_task)

    assert response.status_code == 201  # Vérifie que le statut est bien 201
    data = response.json()

    # Vérifie que la tâche est créée correctement
    assert data["titre"] == new_task["titre"]
    assert data["description"] == new_task["description"]
    assert data["statut"] == new_task["statut"]
    assert "id" in data  # Vérifie que l'ID est généré

def test_update_task():
    """Teste la mise à jour d'une task."""
    updated_task = {"id": 1, "titre": "Task 1 Updated", "description": "Updated description", "statut": False}
    response = client.put("/tasks/1", json=updated_task)
    assert response.status_code == 200

    updated_response = response.json()
    assert updated_response["titre"] == updated_task["titre"]
    assert updated_response["description"] == updated_task["description"]
    assert updated_response["statut"] == updated_task["statut"]

    # Testez la mise à jour d'une tâche inexistante
    response = client.put("/tasks/999", json=updated_task)
    assert response.status_code == 404
    error_response = response.json()
    assert error_response["detail"] == "Task not found"


def test_patch_task():
    """Test la mise à jour partielle d'une task"""
    updated_task = {"statut": True}  # Seulement le champ 'statut' à mettre à jour
    response = client.patch("/tasks/1", json=updated_task)
    
    # Vérifie que la réponse a le bon code de statut
    assert response.status_code == 204

    # Vérifier que le statut a bien été mis à jour
    response_get = client.get("/tasks/1")
    task = response_get.json().get("task")
    assert task["statut"] == True  # Assurez-vous que le statut a été mis à jour


    
def test_delete_task():
    """Teste la suppression d'une task."""
    # Supprimez une tâche existante
    response = client.delete("/tasks/3")
    assert response.status_code == 204

    # Vérifiez que la tâche a bien été supprimée
    response = client.get("/tasks/3")
    assert response.status_code == 404

    # Testez la suppression d'une tâche inexistante
    # response = client.delete("/tasks/999")
    # assert response.status_code == 404
