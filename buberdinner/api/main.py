"""Buber Dinner api."""
import fastapi

from buberdinner.api.properties import settings
from buberdinner.api.v1 import Authcontroller

app = fastapi.FastAPI(
    title=settings.get("title"),
    openapi_url=f"/api/{settings.get('version')}/openapi.json",
)
app.include_router(Authcontroller, prefix=f"/{settings.get('version')}")
