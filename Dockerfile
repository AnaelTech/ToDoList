# Utiliser une image Python
FROM python:3.10-slim

# Répertoire travail
WORKDIR /app

# Fichier nécessaires pour l'image
COPY requirements.txt /app/requirements.txt

# Installation dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie les fichiers dans l'image
COPY . /app/

# Port de l'application
EXPOSE 8000

# Lancer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
