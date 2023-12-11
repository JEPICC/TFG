import random
from server.database import db
from datetime import datetime, timedelta
from server.wells.antennas.models import get_all_antennas
from server.wells.antennas.schemas import Antennas
from server.wells.meters.models import get_meters_by_well
from server.wells.meters.schemas import Meters

config = {'press': [200, 300, 0.1],
          'temp': [550, 700, 0.1],
          'flow': [150,450, 1000.0]}

errors = {
    1: 'Baja tensión',
    2: 'Alta tasa de pérdidas de paquetes',
    3: 'Pérdida de comunicación con dispositivos',
    4: 'Alta ganancia de trasnsmisión',
    5: 'Alto nivel de ruido en la trasnsmisión',
}

async def drop_collection():
    await db.db_wells.values.drop()
    await db.db_wells.antenna_states.drop()

async def generate_seed_data():
    now = datetime.now()
    cur = await get_all_antennas()
    antennas = [Antennas(**doc) async for doc in cur]
    for antenna in antennas:
        cursor = await get_meters_by_well(antenna.idpozo)
        meters = [Meters(**doc) async for doc in cursor]
        init_datatime = now - timedelta(days=7)
        meter_values = []
        while (init_datatime < now):
            #Antenna Failed 3% ratio
            antenna_failed = random.random() < 0.03
            if antenna_failed:
                error_code = random.randrange(1,5)
                await db.db_wells.antenna_states.insert_one({
                    "codigo_error": error_code,
                    "descripcion": errors[error_code],
                    "id_antenna": antenna.id,
                    "timestamp": init_datatime.isoformat()
                })
            for meter in meters:                
                meter_values.append({
                    "estado": not antenna_failed,
                    "idmedidor": meter.id,
                    "timestamp": init_datatime.isoformat(),
                    "value": None if antenna_failed else round(random.randrange(config[meter.tipo][0],config[meter.tipo][1],1)*config[meter.tipo][2],2)
                    })
            
            init_datatime = init_datatime + timedelta(hours=1)
        if len(meter_values) > 0:
            response = await db.db_wells.values.insert_many(meter_values)

# async def generate_seed_data():
#     now = datetime.now()
#     cur = await get_all_antennas()
#     antennas = [Antennas(**doc) async for doc in cur]
#     for antenna in antennas:            
#         cursor = await get_meters_by_well(antenna.idpozo)
#         meters = [Meters(**doc) async for doc in cursor]
#         for meter in meters:
#             init_datatime = now - timedelta(days=7)
#             meter_values = []
#             while (init_datatime < now):
#                 meter_values.append({
#                     "estado": True,
#                     "idmedidor": meter.id,
#                     "timestamp": init_datatime.isoformat(),
#                     "value": round(random.randrange(config[meter.tipo][0],config[meter.tipo][1],1)*config[meter.tipo][2],2)
#                     })
#                 init_datatime = init_datatime + timedelta(hours=1)
#             if len(meter_values) > 0:
#                 response = await db.db_wells.values.insert_many(meter_values)