from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "CareBridge-Demo API"
    app_env: str = "dev"


settings = Settings()
