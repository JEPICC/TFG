#!/bin/bash

#sleep 30
mongoimport --host mongo --db data_wells --collection wells --type json --file /wells.json --jsonArray
mongoimport --host mongo --db data_wells --collection meters --type json --file /meters.json --jsonArray