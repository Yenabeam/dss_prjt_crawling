import pymongo
import re
import pandas as pd
import json
from datetime import datetime
from kakao_msg import send_msg

# load data from mongodb
def load_db():
    today = datetime.now()

    with open("mongodb_ip.json", "r") as fp:
        mongodb_ip = json.load(fp)
    
    # load database
    client = pymongo.MongoClient(mongodb_ip["my_ip"])
    joongo_df = pd.DataFrame(client.joongo["D20112515"].find()).drop(columns='_id')
    # joongo_df = pd.DataFrame(client.joongo["D{}".format(today.strftime('%y%m%d%H'))].find()).drop(columns='_id')
    
    # preprocessing
    joongo_df["price"] = joongo_df["price"].str.replace("원","").str.replace(",","").astype('int')
    joongo_df["inch"] = list(re.findall("([1-9]+)\s?[인치inch]", title)[0] if re.findall("([1-9]+)\s?[인치inch]", title) != [] else None for title in joongo_df["title"])
    joongo_df["year"] = list(re.findall("20[0-1]{1}[0-9]{1}", title)[0] if re.findall("20[0-1]{1}[0-9]{1}", title) != [] else None for title in joongo_df["title"])
    idx = joongo_df[joongo_df['price'] < 100000].index
    joongo_df.drop(index=idx, inplace=True)
    joongo_df.sort_values(by="price", inplace=True)
    joongo_df.reset_index(inplace=True, drop=True)
    
    if (joongo_df['price'] < 500000).sum():
        send_msg()
    
    return joongo_df