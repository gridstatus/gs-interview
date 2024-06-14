from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from backend.main.config import settings


def get_engine():
    ssl_args = {
        "ssl": "require",
        "server_settings": {"application_name": "gs_interview_development"},
    }
    db_url = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_database}"  # noqa

    return create_async_engine(db_url, connect_args=ssl_args)


def get_async_session():
    engine = get_engine()
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    return async_session


async def get_db():
    async with get_async_session() as session:
        # Set a timeout for all statements in this session
        await session.execute(text("SET statement_timeout TO '90s'"))
        yield session


async def run_query(query):
    async_session = get_async_session()
    async with async_session() as session:
        return await session.execute(query)


async def get_data_as_list_of_dicts(query):
    result = await run_query(query)

    return [row.__dict__ for row in result.scalars().all()]
