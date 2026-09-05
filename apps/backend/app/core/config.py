from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "CareBridge Platform API"
    app_env: str = "dev"


settings = Settings()
