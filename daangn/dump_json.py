import pymongo
import configparser
from bson.json_util import dumps, loads 
from datetime import datetime


# load data from mongodb
today = datetime.now()
config = configparser.ConfigParser()
config.read('/home/ubuntu/python3/projects/daangn/mongo.ini')
mongodb_ip = config["mongo"]

client = pymongo.MongoClient(mongodb_ip["ip_address"])
db = client.daangn
collection = db["D{}".format(today.strftime('%y%m%d%H'))]

# Now creating a Cursor instance 
# using find() function
# select only necessary columns
cursor = collection.find({},{'_id':0,'keyword':0, 'desc':0, 'region':0, 'view_counts':0})

# Converting cursor to the list of dictionaries 
list_cur = list(cursor) 

# Converting to the JSON 
json_data = dumps(list_cur, indent = 2, ensure_ascii=False)  
   
# Writing data to file data.json 
with open('data.json', 'w') as file: 
    file.write(json_data)