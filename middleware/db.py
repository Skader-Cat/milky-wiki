from starlette.requests import Request
from starlette.responses import JSONResponse

from db import AsyncSessionLocal


async def db_session_middleware(request: Request, call_next) -> JSONResponse:
    db = AsyncSessionLocal()
    try:
        request.state.db = db
        response = await call_next(request)
        return response
    finally:
        db.close()