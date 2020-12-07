from itemadapter import ItemAdapter
from .mongodb import collection
import configparser
import requests
import numpy as np


class DaangnPipeline(object):
    def process_item(self, item, spider):
        self.config = configparser.ConfigParser()
        self.config.read('/home/ubuntu/python3/project/daangn/daangn/api_key.ini')
        self.rest_api = self.config["rest_api"]
        self.rest_api_key = self.rest_api["rest_api_key"]
        self.app_key = self.rest_api_key
        headers = { "Authorization": "KakaoAK {}".format(self.app_key) }
        addr = item['region']
        url = "https://dapi.kakao.com/v2/local/search/address.json?query={}".format(addr)
        response = requests.get(url, headers=headers).json()
        try: 
            item['lat'] = response['documents'][0]['y']
            item['lon'] = response['documents'][0]['x']
        except:
            item['lat'] = np.nan
            item['lon'] = np.nan
        columns = ["market","keyword","title","price","desc","link","region","view_counts", 'lat','lon']
        data = {column: item[column] for column in columns}
        collection.insert(data)

        return item