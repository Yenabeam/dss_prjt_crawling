import scrapy


class DaangnItem(scrapy.Item):
    category = scrapy.Field() 
    title = scrapy.Field() 
    price = scrapy.Field() 
    region = scrapy.Field() 
    user_id = scrapy.Field() 
    desc = scrapy.Field() 
    chat_counts = scrapy.Field() 
    watch_counts = scrapy.Field() 
    view_counts = scrapy.Field()
