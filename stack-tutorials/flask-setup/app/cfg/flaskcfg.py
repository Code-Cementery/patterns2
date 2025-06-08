import functools
from typing import Optional, Dict, Any

from flask import Flask
from pydantic import BaseSettings, Field


class FlaskSettings(BaseSettings):
    SECRET_KEY: str = Field(env="SECRET_KEY")
    WTF_CSRF_SECRET_KEY: str = Field(env="WTF_CSRF_SECRET_KEY")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "."


@functools.cache
def get_flask_cfg() -> FlaskSettings:
    return FlaskSettings()



def init_flask_cfg(app: Flask):
    """
    Applies configuration for flask from relevant .env file entries

    :param app:
    :return:
    """
    # todo: perhaps refactor .env to .toml files?

    settings = get_flask_cfg()

    for _key, _val in iter(settings):
        app.config[_key] = _val
