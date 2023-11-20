from server.database import db

collection = db.db_users.users

async def get_user(username: str):
    return await collection.find_one({'username': username})


async def create_new_user(user):
    new_user = await collection.insert_one(user)
    return new_user