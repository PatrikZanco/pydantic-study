from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando a conexão com o SQLite
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Criando a base do SQLAlchemy
Base = declarative_base()

# Criando a sessão do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Fornece uma sessão do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
