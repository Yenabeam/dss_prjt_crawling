# mongo id / pw 확인할것 
import requests
import json

#크롤링 함수 
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
    return bunjang_df

# 데이터 크롤링 실행 
bunjang_df = bunjang('맥북프로',3)
bunjang_df['url'] = 'https://m.bunjang.co.kr/products/'+ bunjang_df['pid']
bunjang_df.drop(['pid'], axis=1)


# Mongodb에 데이터 넣기
import pymongo
from datetime import datetime

bunjang = bunjang_df.to_dict("records")
today = datetime.now()

client = pymongo.MongoClient("mongodb://d:d@00.00.00.000:00000")
db = client.joongo
collection = db["D{}".format(today.strftime('%y%m%d%H'))]
collection.insert(bunjang)

# Mongodb에서 데이터 추출

# import pymongo
# from datetime import datetime

# today = datetime.now()

# client = pymongo.MongoClient("mongodb://d:d@00.00.00.000:00000")
# db = client.joongo
# db = client.joongo["D{}".format(today.strftime('%y%m%d%H'))].find()
# joongo_df = pd.DataFrame(db).drop(columns='_id')

# joongo_df.tail(2)