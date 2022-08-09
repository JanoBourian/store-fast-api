from connection.models import Colors
from fastapi import APIRouter, Response, status
from connection.database import database
from schemas.schemas import ColorsIn, ColorsOut

router = APIRouter(tags=["colors"], prefix="/colors")


@router.get("/")
async def get_all_colors():
    query = Colors.select()
    get_values = await database.fetch_all(query)
    return get_values

@router.post("/", response_model = ColorsOut)
async def create_color(response: Response, request:ColorsIn):
    query = Colors.insert().values(**request.dict())
    id_= await database.execute(query)
    created_value = await database.fetch_one(Colors.select().where(Colors.c.id == id_))
    return created_value