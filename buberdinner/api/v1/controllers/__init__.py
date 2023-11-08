import fastapi

from buberdinner.api.v1.controllers.authetication_controller import auth

Authcontroller = fastapi.APIRouter()
Authcontroller.include_router(auth, tags=["auth"])
