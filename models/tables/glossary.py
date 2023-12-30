import datetime
import uuid

from sqlalchemy import Column, Integer, String, UUID, DateTime, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Relationship

from db import Base


class TerminologyCategory(Base):
    __tablename__ = 'termins_categories'

    __table_args__ = (PrimaryKeyConstraint('TermDefinition_id', 'Category_id'),)
    TermDefinition_id = Column(UUID(as_uuid=True), ForeignKey("termins.id"), primary_key=True)
    Category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)



class Terminology(Base):
    __tablename__ = 'termins'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    termin = Column(String(255), nullable=False)
    definition = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    categories = Relationship("Category", secondary="TerminologyCategory")
    glossaries = Relationship("Glossary", secondary="GlossaryTerminology")


class GlossaryTerminology(Base):
    __tablename__ = 'glossary_termins'

    __table_args__ = (PrimaryKeyConstraint('Glossary_id', 'Terminology_id'),)
    Glossary_id = Column(UUID(as_uuid=True), ForeignKey("glossaries.id"), primary_key=True)
    Terminology_id = Column(UUID(as_uuid=True), ForeignKey("termins.id"), primary_key=True)

class Glossary(Base):
    __tablename__ = 'glossaries'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    termins = Relationship("Terminology", secondary="GlossaryTerminology")
