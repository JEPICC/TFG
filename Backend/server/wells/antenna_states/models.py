from server.database import db

collection = db.db_wells.antenna_states

async def create_antenna_state(state):
    new_state = await collection.insert_one(state)
    created_state = await collection.find_one({'_id': new_state.inserted_id})
    return created_state

async def get_all_states():
    cursor = collection.find()
    return cursor

async def get_all_states_by_antenna(id_antenna):
    return collection.find({'id_antenna': id_antenna})