from fastapi import APIRouter, HTTPException
from server.wells.meters.schemas import Meters, MetersUpdate
from server.wells.meters.models import get_all_meter, get_meters_by_well, get_one_meter_id, create_meter, update_meter, delete_meter

meters = APIRouter(
    prefix="/meters",
    tags=["Merters"],
    responses={404: {"description": "Not found"}},
)

@meters.get('/')
async def get_meters():
    cursor = await get_all_meter()
    meters = [Meters(**doc) async for doc in cursor]
    if meters:
        return meters
    raise HTTPException(400, 'Somethinh went wrong!!!')

@meters.get('/well/{id}')
async def get_all_meters_well(id : str):
    cursor = await get_meters_by_well(id)
    meters = [Meters(**doc) async for doc in cursor]
    if meters:
        return meters
    raise HTTPException(400, 'Somethinh went wrong!!!')

@meters.get('/{id}', response_model=Meters)
async def get_meter(id:str):
    meter = await get_one_meter_id(id)
    if meter:
        return meter
    raise HTTPException(404, f'well not found {id}')

@meters.post('/', response_model=Meters)
async def create_new_meter(meter: Meters):
    response = await create_meter(meter.model_dump())
    if response:
        return response
    raise HTTPException(400, 'Somethinh went wrong!!!')

@meters.patch('/{id}', response_model=Meters)
async def modify_meters(id, meter: MetersUpdate ):
    meter = await update_meter(id, meter.model_dump())
    if meter:
        return meter
    raise HTTPException(404, f'well not found {id}')

@meters.delete('/{id}')
async def remove_meters(id):
    response = await delete_meter(id)
    if response:
        return dict(detail=f'Object {id} eliminated')
    raise HTTPException(404, f'well not found {id}')