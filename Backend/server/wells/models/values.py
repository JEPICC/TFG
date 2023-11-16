from server.database import db
from bson import ObjectId
from datetime import datetime

collection = db.db_wells.values

async def get_one_value_id(id):
    value = await collection.find_one({'_id': ObjectId(id)})
    return value

async def create_value(values):
    new_values = await collection.insert_one(values)
    create_values = await collection.find_one({'_id': new_values.inserted_id})
    return create_values

async def get_interval_values(id, start_time, end_time):
    if end_time is None:
        return collection.find({'idmedidor': id, 'timestamp': {'$gte': start_time}})
    if end_time > datetime.now():
        end_time = datetime.now()
    return collection.find({'idmedidor': id, 'timestamp': {'$gte': start_time, '$lt': end_time}})


async def get_all_values():
    cursor = collection.find()
    # valuess = [valuess(**doc) async for doc in collection.find()]
    return cursor

# async def update_values(id: str, data: dict):
#     if len(data) < 1:
#         return False
#     values = await get_one_values_id(id)
#     if values:
#         up_data = {k: v for k, v in data.items() if v is not None}
#         updated_values = await collection.update_one({'_id': ObjectId(id)}, {'$set': up_data})
#         if updated_values:
#             return await get_one_values_id(id)    
#     return False

# async def delete_values(id: str):
#     id_check = await get_one_values_id(id)
#     if id_check:
#         await collection.delete_one({'_id': ObjectId(id)})
#         return True
#     return False

