from sqlalchemy import select, insert

from models.tables import User
from models.tables.notes import Note
from models.tables.project import Project
from service.base import Manager


class NoteManager(Manager):
    db = None

    @classmethod
    async def get_note_list(cls, page, size):
        return await cls.get_list(Note, page, size)

    @classmethod
    async def get_note_by_id(cls, note_id) -> Note:
        return await cls.get_by_id(Note, note_id)

    @classmethod
    async def create_note(cls, note: Note, current_user: User):
        note_data = note.model_dump()
        note_data["owner_id"] = current_user.id
        note_data["linked_project_id"] = note_data["project_id"]
        await cls.create(Note, note_data)


    @classmethod
    async def update_note(cls, note_id, note_info):
        await cls.update(Note, note_id, note_info)

    @classmethod
    async def delete_note(cls, note_id):
        await cls.delete(Note, note_id)

    @classmethod
    async def get_note_list_by_project(cls, project_id, page, size):
        notes = select(Note).filter(Note.linked_project_id == project_id)
        result = await cls._execute_query_and_close(notes)
        return result.scalars().all()


    @classmethod
    async def get_note_by_title(cls, title):
        query = select(Note).filter(Note.title == title)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()
