from db import AsyncSessionLocal


def get_async_db_session():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()