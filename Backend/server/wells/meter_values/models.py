from server.database import db
from bson import ObjectId
from datetime import datetime

collection = db.db_wells.values

async def get_all_values_by_meter(id_meter):
    return collection.find({'idmedidor': id_meter})

async def get_one_value_id(id):
    value = await collection.find_one({'_id': ObjectId(id)})
    return value

async def create_value(values):
    new_values = await collection.insert_one(values)
    create_values = await collection.find_one({'_id': new_values.inserted_id})
    return create_values

async def get_interval_values_by_meter(id_meter, start_time, end_time):
    if end_time is None:
        return collection.find({'idmedidor': id_meter, 'timestamp': {'$gte': start_time}})
    if end_time > datetime.now():
        end_time = datetime.now()
    return collection.find({'idmedidor': id, 'timestamp': {'$gte': start_time, '$lt': end_time}})

async def get_all_values():
    cursor = collection.find()
    return cursor