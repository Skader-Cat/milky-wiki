from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from db import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    termins = relationship("TermDefinition", secondary="TermDefinitionCategory")

