import os
import asyncpg
import redis.asyncio as redis
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.pg_pool = None
        self.redis_client = None

    async def initialize(self):
        """Initialize connection pools for PostgreSQL and Redis."""
        self.pg_pool = await asyncpg.create_pool(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 5432))
        )
        
        self.redis_client = redis.Redis(
            host=os.getenv('REDIS_HOST', 'localhost'),
            port=int(os.getenv('REDIS_PORT', 6379)),
            decode_responses=True
        )

    async def close(self):
        """Close all connection pools."""
        if self.pg_pool:
            await self.pg_pool.close()
        if self.redis_client:
            await self.redis_client.close()

class LogEntry:
    def __init__(self, message, source_id, level, metadata=None):
        self.message = message
        self.source_id = source_id
        self.level = level
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "message": self.message,
            "source_id": self.source_id,
            "level": self.level,
            "metadata": self.metadata
        }
