from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

# Use environment variable for database URL,
# defaulting to a standard PostgreSQL URL
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:password@db:5432/ai_agent_db"
)

# Create an async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a custom session class
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
