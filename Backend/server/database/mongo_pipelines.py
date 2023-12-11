antenna_failures = [
        { "$addFields": { "antennasID": { "$toString": "$_id" }}},
        {"$lookup": {
            "from": "antenna_states",
            "foreignField": "id_antenna",
            "localField": "antennasID",
            "as": "states"
        }},
        {"$project":{
            "_id": 0,
            "tag": 1, 
            "states.codigo_error" : 1,
            "states.descripcion" : 1,
            "states.timestamp": 1}},
        {"$unwind": "$states"},
        {"$sort": {"states.timestamp":-1}},
        { "$limit" : 10 }
    ]

antenna_states = [
    # { "$addFields": { "wellsID": { "$toString": "$_id" }}},
    { "$lookup": {
        "from": "meters",
        "foreignField": "idpozo",
        "localField": "idpozo",
        "as": "meters"}},
    {"$unwind": "$meters"},
    { "$match" : { "meters.tipo" : "flow" } },
    { "$addFields": { "meterID": { "$toString": "$meters._id" }}},
    { "$lookup": {
        "from": "values",
        "foreignField": "idmedidor",
        "localField": "meterID",
        "as": "values"}},
    {"$unwind": "$values"},
    {"$sort": {"timestamp": -1}},
    {"$group": {
        "_id": {"ant": "$tag"},
        "id": {"$first": "$tag"},
        "time": {"$first": "$values.timestamp"},
        "state": {"$first": "$values.estado"},
    }},
    {"$project":{"_id": 0}},
    ]

daily_prod = [
    { "$addFields": { "wellsID": { "$toString": "$_id" }}},
    { "$lookup": {
        "from": "meters",
        "foreignField": "idpozo",
        "localField": "wellsID",
        "as": "meters"}},
    { "$unwind": "$meters"},
    { "$match" : { "meters.tipo" : "flow" } },
    { "$addFields": { "meterID": { "$toString": "$meters._id" }}},
    { "$lookup": {
        "from": "values",
        "foreignField": "idmedidor",
        "localField": "meterID",
        "as": "values"}},
    { "$unwind": "$values"},

    { "$group": {"_id": {"tag": "$sigla", 
                         "dia": { "$dateToString": {
                             "format":"%d-%m-%Y", 
                             "date" : {"$toDate" : "$values.timestamp"}}}},
                 "promedio": { "$avg": "$values.value" }
                 }
    },
    { "$group": {"_id": "$_id.dia",
                 "daily": { "$sum": "$promedio" }
                 }
    },
    {"$sort": {"_id":-1}},
]