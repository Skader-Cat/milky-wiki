from fastapi import Depends, exceptions, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status
from starlette.requests import Request
