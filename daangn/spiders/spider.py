import string
import scrapy
import requests
from scrapy import Request
from daangn.items import DaangnItem

class DaangnSpider(scrapy.Spider):
    name = 'Daangn'
    page_number = 2
    
    def __init__(self, query='맥북 프로', **kwargs):
        self.query = query
        self.start_urls = ["https://www.daangn.com/search/{}/more/flea_market?page=1".format(self.query)]
        super().__init__(**kwargs)
    
    def parse(self, response):
        xp = "/html/body/article/a/@href"
        urls = response.xpath(xp).extract()
        # get full url
        urls =  list(map(response.urljoin, urls))
        return (Request(url, callback=self.parse_content) for url in urls)
    
    def parse_content(self, response):
        item = DaangnItem()
        item['market'] = '당근마켓'
        item['keyword'] = self.query
        item['title'] = response.xpath('//*[@id="article-title"]/text()')[0].extract().strip()
        item['price'] = response.xpath('//*[@id="article-price"]/text() | //*[@id="article-price-nanum"]/text()')[0].extract().strip()
        desc = response.xpath('//*[@id="article-detail"]/p/text()').extract()
        item['region'] = response.xpath('//*[@id="region-name"]/text()')[0].extract().strip()
        item['desc'] = "".join(desc).replace('\n', '')
        item['link'] = response.xpath('/html/head/link[1]/@href')[0].extract()
        counts = response.xpath('//*[@id="article-counts"]/text()')[0].extract().strip()
        item['view_counts'] = counts.split('∙')[2].strip().split(' ')[1]
       
        yield item
        
        next_page = "https://www.daangn.com/search/{}/more/flea_market?page=".format(self.query) + str(DaangnSpider.page_number)
        if DaangnSpider.page_number <= 5:
            DaangnSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)