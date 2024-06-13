from datetime import datetime

from fastapi import FastAPI
from sqlalchemy import select, text

from backend.main.database import get_data_as_dict, run_query
from backend.main.sql_models import table_name_to_model

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/time")
async def get_current_time():
    current_time = datetime.utcnow()
    return {"current_time": current_time.isoformat()}


@app.get("/data")
async def get_data(table_name: str, limit: int = 10):
    model = table_name_to_model(table_name)
    query = select(model).limit(limit)
    result = await get_data_as_dict(query)
    return result


@app.get("/tables")
async def get_tables():
    query = text(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
    )
    result = await run_query(query)
    return {"tables": result.scalars().all()}
