# -*- coding: utf-8 -*-
import scrapy
from bosszp.items import MubanItem
import json
import re
import urllib
from urllib import request
from PIL import Image
from base64 import b64decode
import requests
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time




###########################################  Spider爬虫    ######################################



class MbSpider(scrapy.Spider):
    name = 'zp'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=%E5%AE%9E%E4%B9%A0%E7%94%9F&scity=101210100&industry=&position=']
    h = 'https://www.zhipin.com'

    def parse(self, response):
        # print(response.text)
        lis = response.xpath('//div[@class="job-list"]/ul/li')

        for li in lis:
            url = li.xpath('.//h3/a/@href').get()

            url = self.h + str(url)
            yield scrapy.Request(url,callback=self.jx,meta={'info':url})
            time.sleep(3)

        next_url = response.xpath('//div[@class="page"]/a[last()]/@href').get()
        next_url = self.h + str(next_url)
        # print(next_url)
        if next_url :
            time.sleep(1)
            yield scrapy.Request(url=next_url,callback=self.parse)


    def jx(self,response):

        name = response.xpath('//div[@class="name"]/h1/text()').get()
        gs = response.xpath('//div[@class="company-info"]/a[last()]/text()').get().strip()
        nr =(''.join(response.xpath('//div[@class="job-sec"]/div//text()').getall())).replace(' ','').strip()
        url = response.meta.get('info')

        item = MubanItem(name=name,gs=gs,nr=nr,url=url)
        yield item











