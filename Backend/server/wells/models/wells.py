from server.database import db
from bson import ObjectId

collection = db.db_wells.wells

async def get_one_well_id(id):
    well = await collection.find_one({'_id': ObjectId(id)})
    return well

async def create_well(well):
    new_well = await collection.insert_one(well)
    create_well = await collection.find_one({'_id': new_well.inserted_id})
    return create_well

async def get_all_well():
    cursor = collection.find()
    # wells = [Wells(**doc) async for doc in collection.find()]
    return cursor

async def update_well(id: str, data: dict):
    if len(data) < 1:
        return False
    well = await get_one_well_id(id)
    if well:
        up_data = {k: v for k, v in data.items() if v is not None}
        updated_well = await collection.update_one({'_id': ObjectId(id)}, {'$set': up_data})
        if updated_well:
            return await get_one_well_id(id)    
    return False

async def delete_well(id: str):
    id_check = await get_one_well_id(id)
    if id_check:
        await collection.delete_one({'_id': ObjectId(id)})
        return True
    return False

