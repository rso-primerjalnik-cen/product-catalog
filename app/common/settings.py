from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str = None

    class Config:
        env_file = '.env'


def get_settings() -> Settings:
    return Settings()
