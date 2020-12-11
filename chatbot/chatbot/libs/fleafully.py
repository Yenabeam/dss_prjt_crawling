

import pymongo
import pandas as pd
import configparser
from datetime import datetime


def mongo_ip():
    config = configparser.ConfigParser()
    config.read('/home/ubuntu/chatbot/chatbot/libs/mongo.ini')
    mongodb_ip = config["mongo"]
    return mongodb_ip["ip_address"]


def count(price):
    client = pymongo.MongoClient(mongo_ip())
    today = datetime.now()
    joongo_df = pd.DataFrame(
        client.joongo["C{}R".format(today.strftime('%y%m%d%H'))].find())
    num = joongo_df[joongo_df['price'] < int(price)*10000]['price'].count()
    return """
    {}만원 이하 매물은 총 {}개입니다. :blush:
    {}
    """.format(price, num, joongo_df[joongo_df['price'] < int(price)*10000]['link'][:10].to_string())


def inch(size):
    client = pymongo.MongoClient(mongo_ip())
    today = datetime.now()
    joongo_df = pd.DataFrame(
        client.joongo["C{}R".format(today.strftime('%y%m%d%H'))].find())
    num = joongo_df[joongo_df['inch'] == str(size)]['inch'].count()
    return """
    {}인치 매물은 총 {}개입니다. :blush:
    {}
    """.format(size, num, joongo_df[joongo_df['inch'] == size]['link'][:10].reset_index(drop=True).to_string())


def locate(addr):
    client = pymongo.MongoClient(mongo_ip())
    today = datetime.now()
    joongo_df = pd.DataFrame(
        client.joongo["C{}R".format(today.strftime('%y%m%d%H'))].find())
    df = []
    for _, item in joongo_df[joongo_df['region'].notnull()].iterrows():
        if addr in item["region"]:
            df.append(item["link"])
    df = pd.DataFrame(df, columns=[0])
    return """
    {} 매물은 총 {}개입니다. :blush:
    {}
    """.format(addr, df[0].count(), df[0][:10].to_string())


def suggest():
    client = pymongo.MongoClient(mongo_ip())
    today = datetime.now()
    joongo_df = pd.DataFrame(
        client.joongo["C{}R".format(today.strftime('%y%m%d%H'))].find())
    good_items = joongo_df[['title', 'price', 'link', 'inch', 'year']].dropna()
    good_items[['inch', 'year']] = good_items[['inch', 'year']].astype('int')
    good_items['points'] = round(
        good_items['price'] / ((good_items['inch'] - 10) * (good_items['year'] - 2004) ** 2))
    good_items = good_items.sort_values(by='points').reset_index(drop=True)
    return """
    오늘의 추천 매물입니다. :smile:
    {}
    """.format(good_items[['title', 'price', 'link']][:5].to_markdown(tablefmt="pretty"))
