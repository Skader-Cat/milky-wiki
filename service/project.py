import datetime

from fastapi import HTTPException
from sqlalchemy import select, insert, delete, update

from models.tables import User
from models.tables.project import Project, Project_User
from service import UserManager
from service.base import Manager


class ProjectManager(Manager):
    db = None

    @classmethod
    async def get_project_list(cls, page, size):
        return await cls.get_list(Project, page, size)

    @classmethod
    async def get_project_by_id(cls, project_id) -> Project:
        return await cls.get_by_id(Project, project_id)

    @classmethod
    async def create_project(cls, project: Project, current_user: User):
        if project.title in [project.title for project in await cls.get_project_list(1, 1000)]:
            raise HTTPException(status_code=400, detail="Проект с таким названием уже существует")
        elif project.title.strip() == "" or project.title is None or project.title is False:
            raise HTTPException(status_code=400, detail="Название проекта не может быть пустым")
        else:
            project_data = project.model_dump()
            project_data["owner_id"] = current_user.id
            await cls.create(Project, project_data)
            project_id = (await cls.get_project_by_title(project.title)).id
            await cls.add_user_to_project(project_id, current_user.id)

    @classmethod
    async def update_project(cls, project_id, project_info):
        projects = await cls.get_project_list(1, 1000)
        for project in projects:
            if (project.title == project_info.title) and (str(project.id) != str(project_id)):
                raise HTTPException(status_code=400, detail="Проект с таким названием уже существует")

        # Обновление проекта
        updated_project_info = project_info.model_dump()
        updated_project_info["updated_at"] = datetime.datetime.now()
        await cls.update(Project, project_id, updated_project_info)

    @classmethod
    async def delete_project(cls, project_id):
        #у этой таблицы есть связные таблицы, из которых тоже нужно удалить все сведения
        project_users = await cls.get_project_users(project_id)
        for user in project_users:
            await cls.remove_user_from_project(project_id, user.id)
        await cls.delete(Project, project_id)


    @classmethod
    async def get_project_list_by_user(cls, user_id, page, size):
        projects = select(Project).join(Project_User).filter(Project_User.user_id == user_id).offset((page - 1) * size).limit(size)
        result = await cls._execute_query_and_close(projects)
        return result.scalars().all()

    @classmethod
    async def get_project_by_title(cls, title) -> Project:
        query = select(Project).filter(Project.title == title)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_project_users(cls, project_id):
        users = select(User).join(Project_User).filter(Project_User.project_id == project_id)
        result = await cls._execute_query_and_close(users)
        return result.scalars().all()

    @classmethod
    async def add_user_to_project(cls, project_id, user_id):
        query = insert(Project_User).values({"project_id": project_id, "user_id": user_id})
        await cls._execute_query_and_close(query)




    @classmethod
    async def remove_user_from_project(cls, project_id, user_id):
        query = delete(Project_User).where(Project_User.project_id == project_id).where(Project_User.user_id == user_id)
        await cls._execute_query_and_close(query)


    @classmethod
    async def get_total_projects(cls):
        query = select(Project)
        result = await cls._execute_query_and_close(query)
        return len(result.scalars().all())


