from pydantic import BaseSettings, EmailStr, SecretStr, validator, AnyHttpUrl


class Settings(BaseSettings):
    USER_BACKEND_SERVICE: AnyHttpUrl = ''
    TASK_BACKEND_SERVICE: AnyHttpUrl = ''

    SECRET_KEY: SecretStr = 'some_secret'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5

    class Config():
        env_file = '.env'


settings = Settings()
