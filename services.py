from sqlalchemy.orm import Session
from models import UserDB, UserCreate

class UserService:
    """Classe de serviço para operações relacionadas a usuários"""

    @staticmethod
    def create_user(db: Session, user: UserCreate) -> UserDB:
        """Cria um novo usuário no banco de dados"""
        db_user = UserDB(name=user.name, email=user.email, age=user.age)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def list_users(db: Session):
        """Lista todos os usuários"""
        return db.query(UserDB).all()

    @staticmethod
    def get_user(db: Session, user_id: int):
        """Busca um usuário por ID"""
        return db.query(UserDB).filter(UserDB.id == user_id).first()

    @staticmethod
    def delete_user(db: Session, user_id: int):
        """Deleta um usuário por ID"""
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
