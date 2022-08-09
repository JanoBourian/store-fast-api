from connection.models import Roles
from connection.database import database
from schemas.schemas import RoleIn, RoleOut
from fastapi import Response, APIRouter

router = APIRouter(tags=["roles"], prefix="/roles")

@router.get("/")
async def get_all_roles():
    query = Roles.select()
    get_values = await database.fetch_all(query)
    return get_values

@router.post("/", response_model = RoleOut)
async def create_role(request:RoleIn):
    query = Roles.insert().values(**request.dict())
    id_ = await database.execute(query)
    created_value = await database.fetch_one(Roles.select().where(Roles.c.id == id_))
    return created_value