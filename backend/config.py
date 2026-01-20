from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Default keeps the app startable even if env is missing
    backend_cors_origin: str
    mongo_uri: str
    client_secret: str
    client_id: str
    oauth_redirect_uri: str
    frontend_url: str


    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()