from fastapi import APIRouter
from connection.database import database
from connection.models import Users
from schemas.schemas import UsersSignIn, UsersSignOut
from passlib.context import CryptContext
from auth.auth import create_access_token

router = APIRouter(tags=["users"], prefix="/users")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/")
async def get_all_users():
    query = Users.select()
    get_values = await database.fetch_all(query)
    return [UsersSignOut(**item) for item in get_values]


@router.post("/register/")  # , response_model = UsersSignOut)
async def create_user(request: UsersSignIn):
    request.password = pwd_context.hash(request.password)
    query = Users.insert().values(**request.dict())
    id_ = await database.execute(query)
    created_value = await database.fetch_one(Users.select().where(Users.c.id == id_))
    token = create_access_token(created_value)
    return {"token": token}
    # return created_value
