from fastapi import APIRouter, Response, status, Depends
from connection.models import Sizes
from connection.database import database
from auth.auth import oauth2_scheme
from schemas.schemas import SizesIn, SizesOut

router = APIRouter(tags=["sizes"], prefix="/sizes")


@router.get("/", dependencies=[Depends(oauth2_scheme)])
async def get_all_clothes(response: Response):
    query = Sizes.select()
    get_values = await database.fetch_all(query)
    response.status_code = status.HTTP_200_OK
    return [SizesOut(**item) for item in get_values]


@router.post("/", response_model=SizesOut)
async def create_sizes(request: SizesIn, response: Response):
    query = Sizes.insert().values(**request.dict())
    id_ = await database.execute(query)
    created_value = await database.fetch_one(Sizes.select().where(Sizes.c.id == id_))
    return created_value
