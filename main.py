from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import UserCreate, UserResponse
from services import UserService

# Criar as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Cria um novo usuário no banco de dados"""
    return UserService.create_user(db, user)

@app.get("/users/", response_model=list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    """Lista todos os usuários cadastrados"""
    return UserService.list_users(db)

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """Busca um usuário pelo ID"""
    user = UserService.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.delete("/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Remove um usuário pelo ID"""
    if UserService.delete_user(db, user_id):
        return {"message": "Usuário removido com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
