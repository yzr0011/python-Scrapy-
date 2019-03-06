# -*- coding: utf-8 -*-
import scrapy
from bizhi.items import BizhiItem

class BzSpider(scrapy.Spider):
    name = 'bz'
    allowed_domains = ['zhuoku.com']
    start_urls = ['http://www.zhuoku.com/zhuomianbizhi/computer-pcother/index-1.htm']

    def parse(self, response):
        lis = response.xpath('//div[@id="liebiao"]/div[@class="bizhiin"]')
        for li in lis:
            name = li.xpath('./a[@class="title"]/text()').get()
            url = li.xpath('./a[@class="title"]/@href').get()
            url = response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.tp,meta={'info':name})


        next_url = response.xpath('//div[@id="liebiao"]/div[@class="turn"]/a[text()="下一页"]/@href').get()
        next_url = response.urljoin(next_url)
        # print(next_url)
        if next_url:
            yield scrapy.Request(url=next_url,callback=self.parse)

    def tp(self,response):
        fl = response.meta.get('info')
        urls = response.xpath('//div[@id="liebiao"]/div[@class="bizhiin"]')
        # for url in urls:
        #     url = url.xpath('./a/img/@src')
        urls = list(map(lambda url:(url.xpath('./a/img/@src')).get(),urls))
        item = BizhiItem(fl=fl,image_urls=urls)
        yield item

