"""Buber Dinner api."""
import fastapi

from buberdinner.api.properties import config
from buberdinner.api.v1 import Authcontroller

app = fastapi.FastAPI(
    title=config.get("api", "title"),
    openapi_url=f"/api/{config.get('api','version')}/openapi.json",
)
app.include_router(Authcontroller, prefix=f"/{config.get('api', 'version')}")
