from datetime import datetime

from backend.main.database import run_query
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/time")
async def get_current_time():
    current_time = datetime.utcnow()
    return {"current_time": current_time.isoformat()}


@app.get("/data")
async def get_data(params: str):
    query = f"SELECT * FROM ercot_load_forecast WHERE interval_start_utc = '{params}'"
    result = await run_query(query)
    return result
