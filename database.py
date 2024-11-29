from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://todo_user:yourpassword@localhost/todo_db"

# Créez un moteur de base de données
engine = create_engine(DATABASE_URL)

# Définir une classe de base pour SQLAlchemy
Base = declarative_base()

# Créez une session de base de données
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
