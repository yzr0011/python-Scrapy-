# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QiuSpider(scrapy.Spider):
    name = 'qiu'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    h = 'https://www.qiushibaike.com'

    def parse(self, response):
        lis = response.xpath('//div[@id="content-left"]/div')
        for li in lis:
            url = li.xpath('./a/@href').get()
            url = self.h + url
            yield   scrapy.Request(url,callback=self.jx)
        next_url =response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        next_url = str(next_url)
        next_url = self.h + next_url
        if next_url:
            yield scrapy.Request(next_url)

    def jx(self,response):
        # print(response.url)
        name = response.xpath('//div[@class="side-user-top"]/span[@class="side-user-name"]/text()').get()
        nr = ''.join(response.xpath('//div[@id="single-next-link"]/div[@class="content"]//text()').getall()).strip()
        item = QsbkItem(name = name,nr=nr)
        yield item




