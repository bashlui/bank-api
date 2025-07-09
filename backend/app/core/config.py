from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = "postgresql://user:password@localhost/bankapi"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-here-please-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # App
    APP_NAME: str = "Bank Transaction API"
    DEBUG: bool = True
    
    # Mock data settings
    ENABLE_MOCK_DATA: bool = True
    MOCK_USERS_COUNT: int = 10
    MOCK_TRANSACTIONS_COUNT: int = 50
    
    class Config:
        env_file = ".env"

settings = Settings()
