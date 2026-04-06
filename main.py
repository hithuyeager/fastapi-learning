from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    username: str

@app.post("/users/")
async def create_user(user: User):
    return {"username": user.username}