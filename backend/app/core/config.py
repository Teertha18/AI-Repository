"""
Application Configuration

Loads application settings from environment variables (.env)
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Application Settings
    APP_NAME: str = "Cloud Resource Optimization Copilot"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"

    # AI Configuration
    gemini_api_key: str
    gemini_model: str = "gemini-2.5-flash"

    # GCP Configuration
    gcp_project_id: str = ""
    gcp_region: str = "asia-south1"

    google_application_credentials: str = ""

    provider: str = "mock"

    # Tell Pydantic where to load environment variables from
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()