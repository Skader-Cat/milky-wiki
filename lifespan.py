from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from db import DatabaseManager, DB_Manager
import settings
from service import UserManager
from service.project import ProjectManager


@asynccontextmanager
async def main_app_lifespan(app: FastAPI):
    await DB_Manager.create_db_engine(settings)
    app.state.engine = DB_Manager.engine
    app.state.db = await DB_Manager.get_session()

    UserManager.db = app.state.db
    ProjectManager.db = app.state.db

    try:
        yield
    finally:
        await app.state.conn.close()
        await app.state.engine.dispose()