from typing import List

from fastapi import APIRouter, Depends, HTTPException

from models.schemas.notes import NoteResponse, NoteCreate
from service import UserManager
from service.auth import AuthManager
from service.note import NoteManager

notes_router = APIRouter()

@notes_router.get("/list", response_model=List[NoteResponse])
async def get_notes_list(project_id, page: int = 1, size: int = 10, current_user=Depends(AuthManager.get_current_user)):
    if current_user.role == "admin":
        return await NoteManager.get_note_list(page, size)
    else:
        if project_id in UserManager.get_user_projects(current_user.id):
            return await NoteManager.get_note_list_by_project(project_id, page, size)
        else:
            return HTTPException(status_code=401, detail="Unauthorized")
@notes_router.get("/list_by_user")
async def get_notes_list_by_user(user_id: str, page: int = 1, size: int = 10):
    return await NoteManager.get_note_list_by_user(user_id, page, size)

@notes_router.get("/list_by_project")
async def get_notes_list_by_project(project_id: str, page: int = 1, size: int = 10):
    return await NoteManager.get_note_list_by_project(project_id, page, size)

@notes_router.get("/create")
async def create_note(note: NoteCreate, current_user=Depends(AuthManager.get_current_user)):
    return await NoteManager.create_note(note, current_user)

@notes_router.get("/update")
async def update_note():
    pass

