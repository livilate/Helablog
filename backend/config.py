from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Helablog"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://Livilate:96M8aSLtedE9pISi@cluster0.2qxhs.mongodb.net/Helablog?retryWrites=true&w=majority"
    DB_NAME: str = "Helablog"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()
