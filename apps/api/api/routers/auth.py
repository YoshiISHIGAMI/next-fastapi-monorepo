from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest):
    if payload.email != "test@example.com" or payload.password != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": "fake-token-123", "token_type": "bearer"}


@router.post("/register", response_model=dict)
def register(payload: RegisterRequest):
    # 実際はDBで重複チェックなど
    return {"id": "new_user_1", "name": payload.name, "email": payload.email}