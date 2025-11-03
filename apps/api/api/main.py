from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.routers import auth, users

app = FastAPI(title="Next-FastAPI Monorepo API", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI backend!"}