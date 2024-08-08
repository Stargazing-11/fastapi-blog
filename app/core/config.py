from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Blog"
    admin_email: str = "admin@example.com"
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
