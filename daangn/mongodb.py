import pymongo
import configparser
from datetime import datetime

today = datetime.now()

config = configparser.ConfigParser()
config.read('/home/ubuntu/python3/project/daangn/daangn/mongo.ini')
mongodb_ip = config["mongo"]

client = pymongo.MongoClient(mongodb_ip["ip_address"])
db = client.daangn
collection = db["C{}".format(today.strftime('%y%m%d%H'))]
