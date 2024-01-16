class DB:
    DB_NAME = 'postgres'
    USER = 'chopa'
    HOST = 'localhost'
    PORT = '5433'
    PASSWORD = '1337420'
    DRIVER = 'postgresql+asyncpg'
    POOL_SIZE = 10
    MAX_OVERFLOW = 2
    POOL_TIMEOUT = 30