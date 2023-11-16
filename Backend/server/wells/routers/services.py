from fastapi import APIRouter, Path
from server.wells.services.well_prod import get_data
from bson import json_util
import json

services = APIRouter(
    prefix="/services",
    tags=["Services"],
    responses={404: {"description": "Not found"}},
)

@services.get('/data/well/{id}',)
async def get_data_join(id: str = Path(... , regex=r'^[0-9a-j]{24}$')):
    data = await get_data(id)
    # data = [Any(**doc) async for doc in cursor]
    response = json.loads(json_util.dumps(data))
    return response
