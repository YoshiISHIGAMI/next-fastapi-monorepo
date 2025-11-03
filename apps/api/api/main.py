from fastapi import FastAPI
from api.routers import auth, users

app = FastAPI(title="Next-FastAPI Monorepo API", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI backend!"}