import logging
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

class MongoManager():
    client: AsyncIOMotorClient = None
    db_wells: AsyncIOMotorDatabase = None
    db_users: AsyncIOMotorDatabase = None

    # def connect_to_database(self):
    def __init__(self):
        logging.info("Connecting to MongoDB.")
        try:
            if self.client is None:
                self.client = AsyncIOMotorClient('mongodb://localhost:32768')
                self.client.server_info()
                self.db_wells = self.client.data_wells
                self.db_users = self.client.data_users

            logging.info("Connected to MongoDB.")
        except:
            raise Exception('Error de conexion de base de datos')

    def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        if self.client is None:
            self.client.close()
            self.db_users= None
            self.db_wells = None
        logging.info("Closed connection with MongoDB.")

    # def get_users_db(self):
    #     if self.db_users is None:
    #         self.connect_to_database()
    #     return self.get_users_db
    
    # def get_wells_db(self):
    #     if self.db_wells is None:
    #         self.connect_to_database()
    #     return self.get_wells_db


