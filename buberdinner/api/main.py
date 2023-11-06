"""Buber Dinner api."""
import fastapi
import buberdinner.api.properties as properties

config = properties.config

app = fastapi.FastAPI(
    title=config.get('api', 'title'),
    openapi_url=f"/api/{config.get('api','version')}/openapi.json",
)
