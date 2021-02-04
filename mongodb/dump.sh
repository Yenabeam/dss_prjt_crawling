#!/bin/sh
mongodump --authenticationDatabase admin --out /home/ubuntu/python3/database --host 127.0.0.1 --port 27017 -u username -p password --db joongo --collection C$(date +%y%m%d%H)

mongorestore --authenticationDatabase admin -h 127.0.0.1:27017 -d joongo -u username -p password python3/database/joongo

rm -r python3/database/joongo/
