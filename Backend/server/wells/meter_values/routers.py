from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId
from server.wells.meter_values.schemas import Values, ValuesResponse
from server.wells.meter_values.models import get_all_values_by_meter, get_one_value_id, get_all_values, get_interval_values_by_meter, create_value
from server.wells.services.well_prod import get_data

values = APIRouter(
    prefix="/values",
    tags=["Values"],
    responses={404: {"description": "Not found"}},
)

@values.get('/')
async def get_values():
    cursor = await get_all_values()
    values = [Values(**doc) async for doc in cursor]
    return values

@values.get('/{id}', response_model=Values)
async def get_value(id: str):
    value = await get_one_value_id(id)
    if value:
        return value
    raise HTTPException(404, f'value not found {id}')

@values.get('/time/{id}')
async def get_value_by_meter_timed(id:str, init_time: str, end_time: str | None = None):
    cursor = await get_interval_values_by_meter(id, init_time, end_time)
    values = [Values(**doc) async for doc in cursor]
    print(values)
    if values:
        return values
    raise HTTPException(404, f'value not found {id}')

@values.get('/meter/{id}')
async def get_value_by_meter(id:str):
    cursor = await get_all_values_by_meter(id)
    values = [Values(**doc) async for doc in cursor]
    if values:
        return values
    raise HTTPException(404, f'value not found {id}')


@values.post('/', response_model=Values)
async def create_new_values(value: Values):
    response = await create_value(value.model_dump())
    if response:
        return response
    raise HTTPException(400, 'Somethinh went wrong!!!')



# @values.patch('/{id}', response_model=Meters)
# async def modify_meters(id, value: MetersUpdate ):
#     value = await update_meter(id, value.model_dump())
#     if value:
#         return value
#     raise HTTPException(404, f'well not found {id}')

# @values.delete('/{id}')
# async def remove_meters(id):
#     response = await delete_meter(id)
#     if response:
#         return dict(detail=f'Object {id} eliminated')
#     raise HTTPException(404, f'well not found {id}')