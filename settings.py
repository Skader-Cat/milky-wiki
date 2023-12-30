import credits

class BaseSettingsClass:
    @classmethod
    def get_properties(cls):
        return {key.lower(): getattr(cls, key) for key in dir(cls)
                if not key.startswith('__') and hasattr(cls, key)}

class DatabaseSettings(BaseSettingsClass):
    DRIVER = credits.DB.DRIVER
    HOST = credits.DB.HOST
    PORT = credits.DB.PORT
    USER = credits.DB.USER
    PASSWORD = credits.DB.PASSWORD
    DB_NAME = credits.DB.DB_NAME
    DB_POOL_SIZE = credits.DB.POOL_SIZE
    DB_MAX_OVERFLOW = credits.DB.MAX_OVERFLOW
    DB_POOL_TIMEOUT = credits.DB.POOL_TIMEOUT

    @property
    def GET_DB_URL(self):
        return f'{self.DRIVER}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB_NAME}'

class DevelopmentSettings(BaseSettingsClass):
    DEBUG = True
    RELOAD = True

class AppSettings(BaseSettingsClass):
    TITLE = 'Milky Wiki'
    DESCRIPTION = 'Backend корпоративной базы знаний на FastAPI '
    VERSION = '0.0.1'
    DOCS_URL = '/docs'
    REDOC_URL = '/redoc'
    OPENAPI_URL = '/openapi.json'
    CONTACT = {
        'name': 'Лунь Архипов',
        'url': 'https://vk.com/johnnyfrom602',
        'team': 'MilkHunters'
    }
    LICENSE_INFO = {
        'name': 'MIT License',
        'url': 'https://opensource.org/licenses/MIT'
    }
    SERVER_NAME = 'Milky'
    SERVER_HOST = 'localhost'
    SERVER_PORT = 8000


class CORSSettings(BaseSettingsClass):
    ALLOW_ORIGINS = ['*']
    ALLOW_METHODS = ['*']
    ALLOW_HEADERS = ['*']
    ALLOW_CREDENTIALS = True
    ALLOW_ORIGIN_REGEX = None
    EXPOSE_HEADERS = []
    MAX_AGE = 600

class CookieSettings(BaseSettingsClass):
    COOKIE_DOMAIN = None
    COOKIE_NAME = 'access_token'
    COOKIE_PATH = '/'
    COOKIE_HTTPONLY = True
    COOKIE_SECURE = False
    COOKIE_SAMESITE = 'lax'

class ALLOWED_ROLES(BaseSettingsClass):
    ADMIN = 'admin'
    USER = 'user'
    MANAGER = 'manager'
    WRITER = 'writer'
    MODERATOR = 'moderator'