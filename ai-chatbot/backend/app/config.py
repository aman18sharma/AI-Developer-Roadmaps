from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    xkiro_openai_api_key: str
    xkiro_model_name: str
    xkiro_base_url: str
    database_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()