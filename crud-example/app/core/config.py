from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CRUD_example"

    # DATABASE: str = "sqlite" 
    DATABASE: str = "postgres"

    # SQLALCHEMY_DATABASE_URI: str = f"sqlite://./{PROJECT_NAME}.db"
    # SQLALCHEMY_DATABASE_URI: str = "sqlite://"
    SQLALCHEMY_DATABASE_URI: str = "postgresql://postgres:secret@127.0.0.1:5432/mydb"

settings = Settings()