import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@app.get("/time")
async def get_current_time():
    current_time = datetime.utcnow()
    return {"current_time": current_time.isoformat()}
