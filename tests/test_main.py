import sys
import os

# Ajouter le répertoire racine (où se trouve 'app') au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """Teste la route racine /"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
