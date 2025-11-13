from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mysql_user: str
    mysql_password: str
    mysql_host: str
    mysql_port: int
    mysql_db: str

    class Config:
        env_file = ".env"  # указываем файл .env

settings = Settings()
