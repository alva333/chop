

from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

# Add to existing models.py
from sqlalchemy import Boolean
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.hashed_password)

    def get_password_hash(self, password):
        return pwd_context.hash(password)

class Window(Base):
    __tablename__ = "windows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    content = Column(String)


class Folder(Base):
    __tablename__ = "folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)