import datetime
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Relationship, relationship

from db import Base

class Terminology(Base):
    __tablename__ = "termins"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    termin = Column(String)
    definition = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
    categories = relationship("Category", secondary="termin_category", back_populates="termins")
    glossaries = relationship("Glossary", secondary="glossary_terminology", back_populates="termins")
    author = Column(UUID(as_uuid=True), ForeignKey("users.id"))

class TerminologyCategory(Base):
    __tablename__ = "termin_category"
    __table_args__ = (
        PrimaryKeyConstraint('termin_id', 'category_id'),
    )
    termin_id = Column(UUID(as_uuid=True), ForeignKey("termins.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())


class Glossary(Base):
    __tablename__ = "glossaries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())
    termins = relationship("Terminology", secondary="glossary_terminology", back_populates="glossaries")



class GlossaryTerminology(Base):
    __tablename__ = "glossary_terminology"
    __table_args__ = (
        PrimaryKeyConstraint('glossary_id', 'terminology_id'),
    )
    glossary_id = Column(UUID(as_uuid=True), ForeignKey("glossaries.id"))
    terminology_id = Column(UUID(as_uuid=True), ForeignKey("termins.id"))
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now())

