import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime, ForeignKey
from sqlalchemy.orm import Relationship

from db import Base

class Project_User(Base):
    __tablename__ = "project_user"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())

class Project(Base):
    __tablename__ = "projects"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    owner_id = Column(UUID(as_uuid=True))
    users = Relationship("User", secondary=Project_User, back_populates="projects")
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
