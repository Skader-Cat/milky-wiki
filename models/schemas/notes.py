from uuid import UUID

from pydantic import BaseModel


class NoteBase(BaseModel):
    id: UUID
    title: str
    description: str

class NoteCreate(BaseModel):
    title: str
    description: str
    content: str
    linked_project_id: UUID
    owner_id: str

class NoteFull(NoteBase):
    title: str
    description: str
    content: str
    linked_project_id: UUID
    owner_id: str
    created_at: str
    updated_at: str

class NoteResponse(NoteBase):
    title: str
    description: str
    content: str
    owner_id: str
    created_at: str
    updated_at: str