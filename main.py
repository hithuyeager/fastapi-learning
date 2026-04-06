from pydantic import BaseModel
from fastapi import FastAPI 

app = FastAPI()

class User(BaseModel):
    username: str
    age: int

db = {}

@app.post("/")
async def create_user(user: User):
    if user.username in db:
        return {"error": "Username already exists"}
    db[user.username] = user
    return {"message": "User created successfully", "user": user} 