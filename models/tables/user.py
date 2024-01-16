import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import Relationship

from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(length=50), nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(length=255), nullable=False)  # Максимальная длина пароля ограничена 255 символами
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)

class UserRole(Base):
    __tablename__ = "user_roles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_name = Column(String(length=50), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)