import asyncio
import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import redis.asyncio as redis
from fastapi import FastAPI, APIRouter

redis_client: redis.Redis | None = None  # Type hint for global variable


async def connect_redis() -> None:
    """Connect to the Redis database."""
    global redis_client
    try:
        redis_client = redis.Redis(host='redis', port=6379)
        await redis_client.ping()
    except redis.RedisError as e:
        logging.error("Failed to connect Redis: %s", e)
        raise e


async def get_hit_count() -> int:
    """Increment the hit count in Redis and return the new count."""
    retries = 5
    while True:
        try:
            return await redis_client.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            await asyncio.sleep(0.5)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan context manager to manage Redis connection."""
    await connect_redis()
    yield
    await redis_client.close()


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        debug=True,
        docs_url='/api/docs',
        title='Package services',
        lifespan=lifespan
    )
    app.include_router(ping_router)
    app.include_router(redis_router)
    return app


ping_router = APIRouter(prefix='/ping', tags=['ping app and db'])
redis_router = APIRouter(prefix='/redis', tags=['redis count'])


@ping_router.get('/app')
def ping_app() -> dict[str, str]:
    """Ping endpoint to check if the app is working."""
    return {"text": "App is working"}


@redis_router.get("/")
async def hello() -> dict[str, str]:
    """Get the hit count from Redis."""
    count = await get_hit_count()
    return {"text": f"I have been seen {count} times"}
