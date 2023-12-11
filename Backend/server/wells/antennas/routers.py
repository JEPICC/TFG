from fastapi import APIRouter, HTTPException
from server.wells.antennas.schemas import Antennas, AntennasUpdate
from server.wells.antennas.models import (
    create_antenna, 
    get_all_antennas, 
    get_one_antenna_id, 
    update_antenna,
    delete_antenna,
    get_antenna_by_well,
    get_antenna_states,
    get_antenna_failures)

antennas = APIRouter(
    prefix="/antennas",
    tags=["Antennas"],
    responses={404: {"description": "Not found"}},
)

@antennas.get('/')
async def get_antennas():
    cursor = await get_all_antennas()
    antennas = [Antennas(**doc) async for doc in cursor]
    if antennas:
        return antennas
    raise HTTPException(400, 'Somethinh went wrong!!!')

@antennas.get('/failures')
async def get_failures():
    response = await get_antenna_failures()
    return response

@antennas.get('/states')
async def get_states():
    response = await get_antenna_states()
    return response

@antennas.get('/well/{id}', response_model=Antennas)
async def get_antenna_well(id : str):
    antenna = await get_antenna_by_well(id)
    if antenna:
        return antenna
    raise HTTPException(400, 'Somethinh went wrong!!!')

@antennas.get('/{id}', response_model=Antennas)
async def get_antenna(id:str):
    antenna = await get_one_antenna_id(id)
    if antenna:
        return antenna
    raise HTTPException(404, f'well not found {id}')

@antennas.post('/', response_model=Antennas)
async def create_new_antenna(antenna: Antennas):
    response = await create_antenna(antenna.model_dump())
    if response:
        return response
    raise HTTPException(400, 'Somethinh went wrong!!!')

@antennas.patch('/{id}', response_model=Antennas)
async def modify_antenna(id, antenna: AntennasUpdate ):
    antenna = await update_antenna(id, antenna.model_dump())
    if antenna:
        return antenna
    raise HTTPException(404, f'well not found {id}')

@antennas.delete('/{id}')
async def remove_antenna(id):
    response = await delete_antenna(id)
    if response:
        return dict(detail=f'Object {id} eliminated')
    raise HTTPException(404, f'well not found {id}')

