# APPLICATION TODOLIST :notebook_with_decorative_cover:

---

# ToDoList API

ToDoList est une application API construite avec **FastAPI**, permettant de gérer une liste de tâches. Ce projet utilise des méthodes DevOps et est déployable avec **Docker**.

## Fonctionnalités
- Ajouter des tâches.
- Consulter toutes les tâches.
- Modifier une tâche.
- Supprimer une tâche.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- [Python 3.10+](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

## Installation

### 1. Clonez le dépôt
```bash
git clone https://github.com/AnaelTech/ToDoList.git
cd ToDoList
```

### 2. Installez les dépendances (optionnel si vous utilisez Docker uniquement)
Créez un environnement virtuel et installez les dépendances :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configuration de l'application
Si votre application nécessite des variables d'environnement (par exemple pour la base de données), créez un fichier `.env` à la racine du projet et configurez vos variables :

```env
DATABASE_URL=sqlite:///./todolist.db
```

### 4. Lancer avec Docker
Construisez et lancez le conteneur Docker :
```bash
docker build -t todolist-api .
docker run -d -p 8000:8000 todolist-api
```
L'API sera disponible à l'adresse : [http://localhost:8000](http://localhost:8000).

## Utilisation

### Documentation de l'API
FastAPI gère automatiquement une documentation interactive que vous pouvez consulter à :
- [Swagger UI](http://localhost:8000/docs)
- [ReDoc](http://localhost:8000/redoc)

### Points d'entrée principaux
Voici un résumé des principales routes disponibles :

| Méthode | Endpoint       | Description              |
|----------|----------------|--------------------------|
| `GET`    | `/tasks`       | Récupère toutes les tâches |
| `POST`   | `/tasks`       | Crée une nouvelle tâche   |
| `GET`    | `/tasks/{id}`  | Récupère une tâche par ID |
| `PUT`    | `/tasks/{id}`  | Modifie une tâche       |
| `DELETE` | `/tasks/{id}`  | Supprime une tâche      |

## Tests

Pour exécuter les tests unitaires (si disponibles) :
```bash
pytest
```

---

Développé par [AnaelTech](https://github.com/AnaelTech).