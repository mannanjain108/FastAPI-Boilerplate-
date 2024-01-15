from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    version: str
    is_prod: bool
    auth_jwt_expire_validity: int
    secret_key: str
    algorithm: str
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"
