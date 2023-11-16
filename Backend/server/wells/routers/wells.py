from fastapi import APIRouter, HTTPException, Path
from server.wells.schemas.wells import Wells, WellsUpdate
from server.wells.models.wells import create_well, get_all_well, delete_well, get_one_well_id, update_well

wells = APIRouter(
    prefix="/wells",
    tags=["Well"],
    responses={404: {"description": "Not found"}},
)

@wells.get('/')
async def get_wells():
    cursor = await get_all_well()
    wells = [Wells(**doc) async for doc in cursor]
    return wells

@wells.get('/{id}', response_model=Wells)
async def get_well(id: str = Path(... , regex=r'^[0-9a-j]{24}$')):
    well = await get_one_well_id(id)
    if well:
        return well
    raise HTTPException(404, f'well not found {id}')

@wells.post('/', response_model=Wells)
async def save_well(well: Wells):
    response = await create_well(well.model_dump())
    if response:
        return response
    raise HTTPException(400, 'Somethinh went wrong!!!')

@wells.patch('/{id}', response_model=Wells)
async def modify_well(id, well: WellsUpdate ):
    well = await update_well(id, well.model_dump())
    if well:
        return well
    raise HTTPException(404, f'well not found {id}')

@wells.delete('/{id}')
async def remove_well(id):
    response = await delete_well(id)
    if response:
        return dict(detail=f'Object {id} eliminated')
    raise HTTPException(404, f'well not found {id}')