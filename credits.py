class DB:
    PASSWORD = '1337420'
    USER = 'chopa'
    HOST = 'localhost'
    DRIVER = 'postgresql+asyncpg'
    PORT = 5433
    DB_NAME = 'postgres'

    POOL_SIZE = 10
    MAX_OVERFLOW = 10
    POOL_TIMEOUT = 30

class AUTH:
    SECRET_KEY = '1337420'
    ALGORITHM = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
