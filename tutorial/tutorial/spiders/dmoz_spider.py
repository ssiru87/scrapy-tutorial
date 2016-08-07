import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="site-item "]'):
            item = DmozItem()

            item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div[@class="site-title"]/text()').extract()
            item['desc'] = sel.xpath('div[@class="title-and-desc"]/div[@class="site-descr "]/text()').extract()
            item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract()

            yield item

