#!/bin/bash
sleep 2
mongoimport --host mongo --db data_wells --collection wells --type json --file /wells.json --jsonArray
mongoimport --host mongo --db data_wells --collection meters --type json --file /meters.json --jsonArray
mongoimport --host mongo --db data_wells --collection antennas --type json --file /antennas.json --jsonArray