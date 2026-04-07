from fastapi import APIRouter
from schema import User


router = APIRouter()

@router.post("/users/")
async def create_user(user: User):
    return {"username": user.username}