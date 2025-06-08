import functools
from typing import Optional, Dict, Any

from pydantic import BaseSettings, Field
from sqlalchemy.engine import URL


class DatabaseSettings(BaseSettings):
    host: str = Field(default="localhost", env="DB_HOST")
    port: int = Field(default=5432, env="DB_PORT")  # noqa: WPS432
    username: str = Field(default="postgres", env="DB_USER")
    password: Optional[str] = Field(env="DB_PASSWORD")
    database: str = Field("postgres", env="DB_DATABASE")
    db_schema: str = Field(default="public", env="DB_SCHEMA")
    drivername: str = Field("postgresql")

    @property
    def url(self) -> URL:
        params: Dict[str, Any] = {
            "drivername": self.drivername,
            "host": self.host,
            "database": self.database,
            "username": self.username,
        }

        if self.password is not None:
            params["password"] = self.password

        port_opt = self.port
        if port_opt is not None:
            params["port"] = port_opt

        return URL.create(**params)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "."


@functools.cache
def get_db_cfg():
    return DatabaseSettings()
