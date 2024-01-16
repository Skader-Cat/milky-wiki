import datetime
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Relationship, relationship

from db import Base

class Glossary(Base):
    __tablename__ = "glossaries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    termin = Column(String(length=255), nullable=False)
    definition = Column(String)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)

