from fastapi import APIRouter, HTTPException
from server.wells.schemas.meters import Meters, MetersUpdate
from server.wells.models.meters import get_all_meter, get_one_meter_id, create_meter, update_meter, delete_meter

meters = APIRouter(
    prefix="/meters",
    tags=["Merters"],
    responses={404: {"description": "Not found"}},
)

@meters.get('/')
async def get_meters():
    cursor = await get_all_meter()
    meters = [Meters(**doc) async for doc in cursor]
    return meters

@meters.get('/{id}', response_model=Meters)
async def get_well(id:str):
    meter = await get_one_meter_id(id)
    if meter:
        return meter
    raise HTTPException(404, f'well not found {id}')

@meters.post('/', response_model=Meters)
async def save_meters(meter: Meters):
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