from datetime import datetime
from uuid import UUID

from pydantic import BaseModel




class CreateCategory(BaseModel):
    name: str
    description: str

class Category(CreateCategory):
    id: UUID
    created_at: datetime
    updated_at: datetime


class AddTerminology(BaseModel):
    termin: str
    definition: str
    categories: list[str]

class Terminology(AddTerminology):
    id: UUID
    created_at: datetime
    updated_at: datetime

class CreateGlossary(BaseModel):
    name: str
    description: str
    termins: list[Terminology]

class Glossary(CreateGlossary):
    id: UUID
    created_at: datetime
    updated_at: datetime


