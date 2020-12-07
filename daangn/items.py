# '''
# region = 거래지역; ~구~ 동까지 표기됨
# temperature = 거래 온도; 좋은 거래를 할수록 온도가 높아짐
# chat_counts = 판매자와 구매 관심자의 채팅이 오고 간 횟수
# watch_counts = 찜한 횟수
# some of the above features are removed to in synced with 
# other fleamarket data
# '''
import scrapy


class DaangnItem(scrapy.Item):


    market = scrapy.Field()
    keyword = scrapy.Field()
    title = scrapy.Field() 
    price = scrapy.Field()
    region = scrapy.Field() 
    link = scrapy.Field()
    desc = scrapy.Field() 
    lat = scrapy.Field() 
    lon = scrapy.Field() 
    view_counts = scrapy.Field()
    
