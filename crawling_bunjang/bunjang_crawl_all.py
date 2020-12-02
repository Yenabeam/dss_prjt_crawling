import requests
import json
import pymongo
from datetime import datetime
import pandas as pd 
pd.set_option('mode.chained_assignment',  None)

def bunjang(key_word, pages):
    pid = []
    for page in range(pages):
        url = 'https://api.bunjang.co.kr/api/1/find_v2.json?order=date&n=96&page={}&req_ref=search&q={}&stat_device=w&stat_category_required=1&version=4'.format(page,key_word)
        response = requests.get(url)
        datas = response.json()['list']
        ids = [data['pid'] for data in datas]
        pid.extend(ids)
        items=[]
        for id in pid:
            url = 'https://api.bunjang.co.kr/api/1/product/{}/detail_info.json?version=4'.format(id)
            response = requests.get(url)
            details = response.json()['item_info']
            items.append(details)
        df = pd.DataFrame(items)
        bunjang_df = df[['name','price','location','description_for_detail','num_item_view','pid']]
        bunjang_df['url'] = 'https://m.bunjang.co.kr/products/'+ bunjang_df['pid']
        bunjang_df['market'] = '번개장터'
        bunjang_df['keywords'] = key_word
        bunjang_df.drop(['pid'], axis=1)

        bunjang = bunjang_df.to_dict("records")
        today = datetime.now()

        client = pymongo.MongoClient("mongodb://dss:dss@15.165.128.7:27017")
        db = client.joongo
        collection = db["C{}".format(today.strftime('%y%m%d%H'))]
        collection.insert(bunjang)
        return bunjang_df

categories = ["자전거","패딩","노트북","의자","아이폰","아이패드","캠핑","냉장고","컴퓨터","난로","에어팟","모니터"]

for category in categories:
    bunjang(category,10)