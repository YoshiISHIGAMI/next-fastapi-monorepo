from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/login", response_model=AuthResponse, summary="Login with email and password")
def login(request: LoginRequest):
    if request.email == "test@example.com" and request.password == "password":
        return AuthResponse(access_token="fake-token-123")
    raise HTTPException(status_code=401, detail="Invalid credentials")