from fastapi import APIRouter, HTTPException
from server.wells.antenna_states.schemas import AntennaStates, AntennaStatesResponse
from server.wells.antenna_states.models import (
    create_antenna_state,
    get_all_states,
    get_all_states_by_antenna)

comm = APIRouter(
    prefix="/comm",
    tags=["Communication"],
    responses={404: {"description": "Not found"}},
)

@comm.get('/')
async def get_antenna_state():
    cursor = await get_all_states()
    states = [AntennaStatesResponse(**doc) async for doc in cursor]
    if states:
        return states
    raise HTTPException(400, 'Somethinh went wrong!!!')

@comm.get('/antenna/{id}', response_model=AntennaStates)
async def get_states_antenna(id : str):
    cursor = await get_all_states_by_antenna(id)
    states = [AntennaStates(**doc) async for doc in cursor]
    if states:
        return states
    raise HTTPException(400, 'Somethinh went wrong!!!')

@comm.post('/', response_model=AntennaStates)
async def create_new_state(antenna: AntennaStates):
    response = await create_antenna_state(antenna.model_dump())
    if response:
        return response
    raise HTTPException(400, 'Somethinh went wrong!!!')
