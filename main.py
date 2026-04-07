from fastapi import FastAPI
from database import connect_to_db, close_db
from router import router
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_db()
    yield
    await close_db()    

app = FastAPI(lifespan=lifespan)
app.include_router(router)
