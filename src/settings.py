from pydantic import BaseSettings, EmailStr, SecretStr, validator, AnyHttpUrl


class Settings(BaseSettings):
    USER_BACKEND_SERVICE: AnyHttpUrl = ''
    TASK_BACKEND_SERVICE: AnyHttpUrl = ''

    class Config:
        env_file = '.env'


settings = Settings()
