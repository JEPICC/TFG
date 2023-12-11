from fastapi import APIRouter
from server.database.seed_data import drop_collection, generate_seed_data
from server.wells.services.well_prod import get_data

services = APIRouter(
    prefix="/services",
    tags=["Services"],
    responses={404: {"description": "Not found"}},
)

@services.get('/drop')
async def drop_collection_values():
    await drop_collection()
    return {'message': 'Collections Deleted'}

@services.get('/generate')
async def generate_data_values():
    await generate_seed_data()
    return {'message': 'Seed Values Created'}

# @services.get('/failures')
# async def get_failures():
#     response = await get_antenna_failures()
#     return response

# @services.get('/states')
# async def get_states():
#     response = await get_antenna_states()
#     return response

# @services.get('/daily')
# async def get_daily():
#     response = await get_daily_prod()
#     return response

@services.get('/data')
async def get_all_data():
    response = await get_data('655ffae346cf3a8c69e22378')
    return response