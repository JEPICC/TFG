from server.database import db
from datetime import datetime, timedelta
from server.wells.models.meters import get_all_meter
from server.wells.schemas.meters import Meters
import random

config = {'press': [200, 300, 0.1],
          'temp': [550, 700, 0.1],
          'flow': [150,450, 1000.0]}

async def drop_collection():
    await db.db_wells.values.drop()

async def generate_seed_data():
    now = datetime.now()
    cursor = await get_all_meter()
    meters = [Meters(**doc) async for doc in cursor]
    for meter in meters:
        init_datatime = now - timedelta(hours=24)
        meter_values = []
        while (init_datatime < now):
            meter_values.append({
                "estado": True,
                "idmedidor": meter.id,
                "timestamp": init_datatime.isoformat(),
                "value": round(random.randrange(config[meter.tipo][0],config[meter.tipo][1],1)*config[meter.tipo][2],2)
                })
            init_datatime = init_datatime + timedelta(hours=1)
        if len(meter_values) > 0:
            response = await db.db_wells.values.insert_many(meter_values)
            print(response)