import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class ProjectFull(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    owner_id: UUID
    users: list[str]
    created_at: str
    updated_at: str

class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = None
    owner_id: str

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
class ProjectResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    owner_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime

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


