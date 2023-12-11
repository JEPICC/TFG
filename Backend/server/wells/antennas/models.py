from bson import ObjectId
from server.database import db
from server.database.mongo_pipelines import antenna_failures, antenna_states

collection = db.db_wells.antennas

async def get_one_antenna_id(id):
    antenna = await collection.find_one({'_id': ObjectId(id)})
    return antenna

async def create_antenna(antenna):
    new_antenna = await collection.insert_one(antenna)
    create_antenna = await collection.find_one({'_id': new_antenna.inserted_id})
    return create_antenna

async def get_all_antennas():
    cursor = collection.find()
    return cursor

async def get_antenna_by_well(id_well):
    return collection.find({'idpozo': id_well})

async def update_antenna(id: str, data: dict):
    if len(data) < 1:
        return False
    antenna = await get_one_antenna_id(id)
    if antenna:
        up_data = {k: v for k, v in data.items() if v is not None}
        updated_antenna = await collection.update_one({'_id': ObjectId(id)}, {'$set': up_data})
        if updated_antenna:
            return await get_one_antenna_id(id)    
    return False

async def delete_antenna(id: str):
    id_check = await get_one_antenna_id(id)
    if id_check:
        await collection.delete_one({'_id': ObjectId(id)})
        return True
    return False

async def get_antenna_failures():
    data = await collection.aggregate(antenna_failures).to_list(length=None)
    return data

async def get_antenna_states():
    data = await collection.aggregate(antenna_states).to_list(length=None)
    return data