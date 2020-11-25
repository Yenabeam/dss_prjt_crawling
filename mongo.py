import pymongo
import re
import pandas as pd
import json
from datetime import datetime

def load_db():
    today = datetime.now()

    with open("mongodb_ip.json", "r") as fp:
        mongodb_ip = json.load(fp)

    client = pymongo.MongoClient(mongodb_ip["my_ip"])
    joongo_df = pd.DataFrame(client.joongo["D20112515"].find()).drop(columns='_id')
    # joongo_df = pd.DataFrame(client.joongo["D{}".format(today.strftime('%y%m%d%H'))].find()).drop(columns='_id')

    joongo_df["inch"] = list(re.findall("([1-9]+)\s?[인치inch]", title)[0] if re.findall("([1-9]+)\s?[인치inch]", title) != [] else None for title in joongo_df["title"])
    joongo_df["year"] = list(re.findall("201[1-9]{1}", title)[0] if re.findall("201[1-9]{1}", title) != [] else None for title in joongo_df["title"])

    return joongo_df