

import pymongo
import pandas as pd
import configparser

def mongo_ip():
    config = configparser.ConfigParser()
    config.read('/home/ubuntu/chatbot/chatbot/libs/mongo.ini')
    mongodb_ip = config["mongo"]
    return mongodb_ip["ip_address"]

def count(price):
    client = pymongo.MongoClient(mongo_ip())
    joongo_df = pd.DataFrame(client.joongo["D201130R"].find())
    num = joongo_df[joongo_df['price'] < int(price)*10000]['price'].count()    
    return """
    {}만원 이하 매물은 총 {}개입니다.
    {}
    """.format(price, num, joongo_df[joongo_df['price'] < int(price)*10000]['link'].to_string())

def inch(size):
    client = pymongo.MongoClient(mongo_ip())
    joongo_df = pd.DataFrame(client.joongo["D201130R"].find())
    num = joongo_df[joongo_df['inch'] == size]['inch'].count()
    return """
    {}인치 매물은 총 {}개입니다.
    {}
    """.format(size, num, joongo_df[joongo_df['inch'] == size]['link'].reset_index(drop=True).to_string())

def locate(addr):
    client = pymongo.MongoClient(mongo_ip())
    joongo_df = pd.DataFrame(client.joongo["D201130R"].find())
    df = []
    for _, item in joongo_df[joongo_df['region'].notnull()].iterrows():
        if addr in item["region"]:
            df.append(item["link"])
    df = pd.DataFrame(df, columns=[0])
    return """
    {} 매물은 총 {}개입니다.
    {}
    """.format(addr, df[0].count(), df[0].to_string())
