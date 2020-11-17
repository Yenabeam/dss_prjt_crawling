import scrapy
from daangn.items import DaangnItem

class DaangnSpider(scrapy.Spider):
    name = "Daangn"
    allow_domain = ["daangn.com"]
    start_urls = ["https://www.daangn.com/search/macbook"]
    
    def parse(self, response):
        links = dom.xpath('//*[@id="flea-market-wrap"]/article/a/@href').extract()
        links = dom.urljoin(links)
        for link in links:
            yield scrapy.Request(link, callback=self.parse_content)
            
    def parse_content(self, response):
        item = DaangnItem()
        item['category'] = dom.xpath('//*[@id="article-category"]/text()')[0].extract().replace('∙', '').strip()
        item['title'] = dom.xpath('//*[@id="article-title"]/text()')[0].extract().strip()
        item['price'] = dom.xpath('//*[@id="article-price"]/text()')[0].extract().strip()
        desc = dom.xpath('//*[@id="article-detail"]/p/text()').extract()
        item['desc'] = "".join(desc).replace('\n', '')
        item['user_id'] = dom.xpath('//*[@id="nickname"]/text()')[0].extract().strip()
        item['region'] = dom.xpath('//*[@id="region-name"]/text()')[0].extract().strip()
        counts = dom.xpath('//*[@id="article-counts"]/text()')[0].extract().strip()
        item['chat_counts'] = counts.split('∙')[0].strip().split(' ')[1]
        item['watch_counts'] = counts.split('∙')[1].strip().split(' ')[1]
        item['view_counts'] = counts.split('∙')[2].strip().split(' ')[1]
       
        yield item
