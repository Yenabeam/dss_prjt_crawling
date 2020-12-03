import pymongo
import re
import pandas as pd
import boto3
import configparser
import sys
from datetime import datetime
from kakao_msg import send_msg
from slack_msg import send_msg2

# load data from mongodb
def load_db():
    today = datetime.now()

    config = configparser.ConfigParser()
    config.read('/home/ubuntu/masterpiece/mongo.ini')
    mongodb_ip = config["mongo"]
    
    # load database
    client = pymongo.MongoClient(mongodb_ip["ip_address"])
    joongo_df = pd.DataFrame(client.joongo["D{}".format(today.strftime('%y%m%d'))].find()).drop(columns='_id')
    
    # preprocessing
    joongo_df["price"] = joongo_df["price"].str.replace("원","").str.replace(",","").astype('int')
    joongo_df["inch"] = list(re.findall("([1-9]+)\s?[인치inch]", title)[0] if re.findall("([1-9]+)\s?[인치inch]", title) != [] else None for title in joongo_df["title"])
    joongo_df["year"] = list(re.findall("20[0-1]{1}[0-9]{1}", title)[0] if re.findall("20[0-1]{1}[0-9]{1}", title) != [] else None for title in joongo_df["title"])
    idx = joongo_df[joongo_df['price'] < 100000].index
    joongo_df.drop(index=idx, inplace=True)
    joongo_df.sort_values(by="price", inplace=True)
    joongo_df.reset_index(inplace=True, drop=True)
    
    # insert into database
    items = joongo_df['title'].count()
    if items:
        send_msg()
        send_msg2("""
        매물 {}건 득템 기회!! 지금 바로 잡자! 
        http://fleafully.com/
        """.format(items))
    
    collection = client.joongo["D{}R".format(today.strftime('%y%m%d'))]
    collection.insert(joongo_df.to_dict("records"))
    
    print("Update db")
    
    return joongo_df