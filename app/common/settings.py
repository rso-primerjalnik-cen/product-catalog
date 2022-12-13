from pydantic import BaseSettings


class Settings(BaseSettings):
    POSTGRESQL_HOST: str = 'localhost'
    POSTGRESQL_PWD: str = '123456789'
    POSTGRESQL_USER: str = 'postgres'
    POSTGRESQL_DB: str = 'postgres'

    PAGINATION_DEFAULT_LIMIT: int = 20
    PAGINATION_DEFAULT_OFFSET: int = 0

    @property
    def postgres_conn(self):
        return dict(provider="postgres",
                    host=self.POSTGRESQL_HOST,
                    password=self.POSTGRESQL_PWD,
                    user=self.POSTGRESQL_USER,
                    database=self.POSTGRESQL_DB)

    class Config:
        env_file = '.env'


def get_settings() -> Settings:
    return Settings()
