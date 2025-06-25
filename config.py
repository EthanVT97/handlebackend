# config.py (New File)

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database Configuration
    database_url: str

    # JWT Settings
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int = 30

    # Viber Bot Settings (if used)
    # These can be optional if you provide default values
    viber_bot_token: str = "your_viber_bot_token_here"
    viber_admin_chat_id: str = "your_admin_chat_id_here"

    class Config:
        env_file = ".env"

# Create a single, importable instance of the settings
settings = Settings()
