from sqlalchemy import select, insert, delete

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
    async def create_project(cls, project, current_user: User):
        project_data = project.model_dump()
        project_data["owner_id"] = current_user.id
        await cls.create(Project, project_data)

    @classmethod
    async def update_project(cls, project_id, project_info):
        await cls.update(Project, project_id, project_info)

    @classmethod
    async def delete_project(cls, project_id):
        await cls.delete(Project, project_id)

    @classmethod
    async def get_project_by_name(cls, name) -> Project:
        query = select(Project).filter(Project.name == name)
        result = await cls._execute_query_and_close(query)
        return result.scalars().first()

    @classmethod
    async def get_project_users(cls, project_id):
        projects = select(Project_User).filter(Project_User.project_id == project_id)
        result = await cls._execute_query_and_close(projects)
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


