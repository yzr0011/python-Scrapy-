# -*- coding: utf-8 -*-
import scrapy
from jingdon.items import JDItem
import json
import re
import requests




###########################################  Spider爬虫    ######################################



class JDSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','c.3.cn']
    start_urls = ['https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main']
    hender = 'https:'
    def parse(self, response):
        lis = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        for li in lis:
            id = li.xpath('.//div/@data-sku').get()
            url = 'https://c.3.cn/recommend?methods=accessories&sku='+id+'&cat=670%2C671%2C6'
            yield scrapy.Request(url=url,callback=self.parse_xq)


    def parse_xq(self,response):
        shuju = str(response.body.decode('gbk'))
        a =json.loads(shuju)
        name = a['accessories']['data']['wName']
        jg= a['accessories']['data']['wMaprice']
        print(name,jg)
