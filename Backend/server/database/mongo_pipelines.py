from datetime import date, timedelta 

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
        "id": {"$last": "$tag"},
        "time": {"$last": "$values.timestamp"},
        "state": {"$last": "$values.estado"},
    }},
    {"$project":{"_id":0}}
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

today_prod = [
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
    {"$match": 
     {"values.timestamp": {"$gte": date.today().isoformat()}},        
    },
    {"$addFields": {"values.flowHours": {"$divide": ["$values.value", 24]}}},
    # {"$project":{"_id": 0, "meters._id": 0, "values._id": 0}},
    # {"$limit": 2}
    { "$group": {"_id": {"tag": "$sigla", },
                 "acumm": { "$sum": "$values.flowHours"}
                 }
    },
    { "$group": {"_id": "today",
                 "accumulated": { "$sum": "$acumm" }
                 }
    },
]

yesterday_prod = [
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
    {"$match": {
        "$and": [
            {"values.timestamp": {"$gte": (date.today() - timedelta(days = 1)).isoformat()}},
            {"values.timestamp": {"$lt": date.today().isoformat()}},
        ]
    }},
    { "$group": {"_id": {"tag": "$sigla"},
                 "promedio": { "$avg": "$values.value" }
                 }
    },
    { "$group": {"_id": "yesterday",
                 "total": { "$sum": "$promedio" }
                 }
    },
]

now_prod = [
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
    { "$sort": { "values.timestamp": 1 }},
    {"$group":{
           "_id": "$sigla",
           "value": { "$last": "$values.value" },
           "last": { "$last": "$values.timestamp" }
    }},
    { "$group": {"_id": "now",
                 "flow": { "$sum": "$value" }
                 }
    }
]