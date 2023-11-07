import fastapi
import fastapi.encoders as encoders

from buberdinner.schemas.authentication.loginrequest import LoginRequest
from buberdinner.schemas.authentication.register_request import RegisterRequest

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])

@auth.post("/register")
def register(request: RegisterRequest):
    json = encoders.jsonable_encoder(request)
    return fastapi.responses.JSONResponse(content=json)

@auth.post("/login")
def login(request: LoginRequest):
    json = encoders.jsonable_encoder(request)
    return fastapi.responses.JSONResponse(content=json)
