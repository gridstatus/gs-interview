from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, text

from backend.main.database import get_data_as_list_of_dicts, run_query
from backend.main.sql_models import table_name_to_model

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"message": "Grid Status Technical Interview"}


@app.get("/data")
async def get_data(table_name: str, limit: int = 10):
    if not table_name:
        return
    model = table_name_to_model(table_name)
    query = select(model).limit(limit)
    result = await get_data_as_list_of_dicts(query)
    return result


@app.get("/tables")
async def get_tables():
    query = text(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        "ORDER BY table_name;"
    )
    result = await run_query(query)
    return {"tables": result.scalars().all()}
