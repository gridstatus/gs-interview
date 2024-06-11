import os

from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from backend.main.config import settings


def get_engine():
    application_name = "gs_demo_development"

    if settings.production:
        application_name = "gs_demo_production"

    ssl_args = {
        "ssl": "require",
        "server_settings": {"application_name": application_name},
    }
    db_url = f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_database}"  # noqa

    # set echo to True to log all SQL statements
    log_sql = os.getenv("LOG_SQL", "").lower() in ["true", "1"]

    return create_async_engine(db_url, echo=log_sql, connect_args=ssl_args)


def get_async_session():
    engine = get_engine()
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    return async_session


async def get_db():
    timeout = os.environ.get("STATEMENT_TIMEOUT", "180s")
    async with get_async_session() as session:
        # Set a timeout for all statements in this session
        await session.execute(text(f"SET statement_timeout TO '{timeout}'"))
        yield session


async def run_query(query):
    async_session = get_async_session()

    async with async_session() as session:
        async with session.begin():
            result = await session.execute(query)
            return result
