import pytest
import os
from src.models.database import DatabaseManager

@pytest.mark.asyncio
async def test_database_manager_init():
    manager = DatabaseManager()
    # Expecting failure without real DB, but verifying class structure
    assert manager.pg_pool is None
    assert manager.redis_client is None
