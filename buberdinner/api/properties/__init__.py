import pathlib

from starlette import config as starlette_config
from starlette import datastructures

properties = pathlib.Path(__file__).absolute().parent

env = starlette_config.Config(properties / ".env")

api_title = env.get("TITLE", default="buberdinner")
api_version = env.get("VERSION", default="v1")

host = env.get("HOST", default="127.0.0.1")
port = env.get("PORT", default=5432)
user = env.get("USER", default="postgres")
password = datastructures.Secret(env.get("PASSWORD"))
database = env.get("DATABASE", default=api_title)

dsn = f"postgresql://{user}:{password}@{host}:{port}/{database}"

settings = {"title": api_title, "version": api_version, "dsn": dsn}
