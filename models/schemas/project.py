from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ProjectFull(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    owner: str
    users: list[str]
    created_at: str
    updated_at: str

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    owner: str

class ProjectUpdate(BaseModel):
    name: str
    description: Optional[str] = None
    owner: str

class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: Optional[str] = None
    owner: str
    created_at: str
    updated_at: str

class ProjectListResponse(BaseModel):
    projects: list[ProjectResponse]
    total: int
    page: int
    size: int

class ProjectUserResponse(BaseModel):
    id: UUID
    project_id: UUID
    user_id: UUID
    created_at: str
    updated_at: str

class ProjectUserListResponse(BaseModel):
    project_users: list[ProjectUserResponse]
    total: int
    page: int
    size: int


