import asyncpg
from config import settings

pool = None

async def connect_to_db():
    global pool
    pool = await asyncpg.create_pool(
       dsn = settings.database_url,
       min_size = 1,
       max_size = 10
    )

async def close_db():
    if pool:
        await pool.close()