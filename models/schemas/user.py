
from pydantic import BaseModel
from uuid import UUID

class UserResponse(BaseModel):
    id: UUID
    email: str
    username: str
    role: str


class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserUpdate(BaseModel):
    username: str
    password: str

class UserFull(BaseModel):
    id: UUID
    username: str
    password: str
    email: str
    role: str

class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int
    page: int
    size: int



