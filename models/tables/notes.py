import datetime
import uuid

from sqlalchemy import UUID, Column, String, DateTime
from sqlalchemy.orm import Relationship

from db import Base


from sqlalchemy import Column, String, DateTime, ForeignKey, UUID
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    content = Column(String)
    owner_id = Column(UUID(as_uuid=True))
    linked_project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"))
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())

