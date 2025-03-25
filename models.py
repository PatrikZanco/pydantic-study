from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String
from database import Base

# Modelo SQLAlchemy para o banco de dados
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=True)

# Modelo Pydantic para validação
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int | None = None

class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True
