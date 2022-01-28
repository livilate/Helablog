from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Helablog"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = ""
    DB_NAME: str = "Helablog"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
