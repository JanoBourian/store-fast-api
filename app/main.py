from fastapi import FastAPI
from connection.database import database
from .routers import colors, users

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def index():
    return {"message": "hello world"}


# Router
app.include_router(colors.router)
app.include_router(users.router)
