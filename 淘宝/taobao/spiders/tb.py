# -*- coding: utf-8 -*-
import scrapy
import re
import json
from taobao.items import TaobaoItem


class TbSpider(scrapy.Spider):

    name = 'tb'
    allowed_domains = ['www.taobao.com']
    start_urls = ['*************']

    def start_requests(self):
        for i in range(0, 8888888, 44):  ###试试看能爬几页    大概30页左右
            url = 'https://s.taobao.com/search?spm=a230r.1.0.0.15a63c6bAZuAry&q=笔记本电脑&rs=up&rsclick=1&preq=电脑&bcoffset=4&p4ppushleft=%2C48&ntoffset=4&style=list&s={}'.format(i)
            y = int(i)/44

            yield scrapy.Request(url,callback=self.parse,meta={'info':y})

    def parse(self, response):
        y = response.meta.get('info')
        html = response.text

        date = (re.findall(r'g_page_config =(.+?)g_srp_loadCss', html, re.S)[0]).strip(' ;\n')
        date = json.loads(date)
        date = date['mods']['itemlist']['data']['auctions']
        for i in date:
            title = i['title']
            view_price = i['view_price']
            view_sales = i['view_sales']
        #     print('***标题： '+title)
        #     print('***人数： '+view_sales)
        #     print('***价格： '+view_price)
            item = TaobaoItem(title=title, view_price=view_price, view_sales=view_sales)
            yield item

        print('='*60)
        print('第%d页'%y)
        print('=' * 60)

