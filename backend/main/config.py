import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    Throws an exception if a required environment variable is missing.
    """

    load_dotenv()

    production: bool = False

    postgres_host: str = os.getenv("POSTGRES_HOST")

    postgres_port: str = os.getenv("POSTGRES_PORT", "5432")

    postgres_user: str = os.getenv("POSTGRES_USER")

    postgres_password: str = os.getenv("POSTGRES_PASSWORD")

    postgres_database: str = os.getenv("POSTGRES_DATABASE")


settings = Settings()
