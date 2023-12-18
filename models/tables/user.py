import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime
from sqlalchemy.orm import Relationship

from db import Base
from models.tables.project import Project_User


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)
    projects = Relationship("Project", secondary="project_user", back_populates="users")
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())