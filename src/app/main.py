from fastapi import FastAPI

from app.api import notes, test
from app.db import database, engine, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(test.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
