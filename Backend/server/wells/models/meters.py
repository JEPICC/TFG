from server.database import db
from bson import ObjectId

collection = db.db_wells.meters

async def get_one_meter_id(id):
    meter = await collection.find_one({'_id': ObjectId(id)})
    return meter

async def create_meter(meter):
    new_meter = await collection.insert_one(meter)
    create_meter = await collection.find_one({'_id': new_meter.inserted_id})
    return create_meter

# async def get_all_meter_by_well(id):
#     return collection.find({'idpozo': id})

async def get_all_meter():
    cursor = collection.find()
    return cursor

async def get_meters_by_well(id_well):
    return collection.find({'idpozo': id_well})

async def update_meter(id: str, data: dict):
    if len(data) < 1:
        return False
    meter = await get_one_meter_id(id)
    if meter:
        up_data = {k: v for k, v in data.items() if v is not None}
        updated_meter = await collection.update_one({'_id': ObjectId(id)}, {'$set': up_data})
        if updated_meter:
            return await get_one_meter_id(id)    
    return False

async def delete_meter(id: str):
    id_check = await get_one_meter_id(id)
    if id_check:
        await collection.delete_one({'_id': ObjectId(id)})
        return True
    return False