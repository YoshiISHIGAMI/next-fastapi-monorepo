from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class User(BaseModel):
    id: str
    name: str
    email: str

fake_users = [
    {"id": "1", "name": "Alice", "email": "alice@example.com"},
    {"id": "2", "name": "Bob", "email": "bob@example.com"},
]

@router.get("/", response_model=List[User])
def get_users():
    return fake_users

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    user = next((u for u in fake_users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user