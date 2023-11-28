from fastapi import APIRouter
from server.database.seed_data import drop_collection, generate_seed_data

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