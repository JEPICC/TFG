from server.database import db
from bson import ObjectId

async def get_data(id):
    data = await db.db_wells.wells.aggregate([
    {
        "$match": {
        "_id": ObjectId(id)
        }
    },
    {
        "$lookup": {
        "from": "meters",
        "let": {
            "well_id": "$_id"#"collA_id": "$_id"
        },
        "pipeline": [
            {
            "$addFields": {
                "meter_well": { #"collB_Aid": {
                "$toObjectId": "$idpozo"
                }
            }
            },
            {
                "$match": {
                    "$expr": {
                        "$eq": [
                            "$meter_well",
                            "$$well_id"
                        ]
                    }   
                }
            }
        ],
        "as": "meters"
        }
    },
    {
        "$unwind": "$meters"
    },
    {
        '$project': 
            {'_id': 1, 'meters._id':1, 'meters.tag':1, 'values.timestamp':1, 'values.value': 1}
    },
    {
        "$lookup": {
        "from": "values",
        "let": {
            "meter_id": "$meters._id"
        },
        "pipeline": [
            {
            "$addFields": {
                "value_meter": {
                "$toObjectId": "$idmedidor" #2do mtere 6552b8f86cce0f7471aa6876
                }
            }
            },
            {
            "$match": {
                "$expr": {
                "$eq": [
                    "$value_meter",
                    "$$meter_id"
                ]
                }
            }
            }
        ],
        "as": "values"
        }
    },
    # {"$unwind": "$values"} 
    ]).to_list(None)


    return data



    