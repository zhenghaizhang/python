from scrapy.spiders import Spider


class FirstSpider(Spider):
    name = 'first'
    allow_domains = ['baidu.com']
    allow_url = ['http://www.baidu.com', ]

    def parse(self, response):
        pass
