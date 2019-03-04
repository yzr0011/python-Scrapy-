# -*- coding: utf-8 -*-
import scrapy
from jd_xlwb.items import XlwbItem
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

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import scrapy
from selenium import webdriver
# from aip import AipNlp  # pip install baidu-aip
from jd_xlwb.items import XlwbItem


###########################################  CrawlSpider爬虫###############################################################


class XlwbSpider(scrapy.Spider):
    name = 'xlwb'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/p/index?containerid=231051_-_fans_-_5643112633']

    def __init__(self):
        # 实例化一个谷歌浏览器对象
        self.LLQ = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")

    def parse(self, response):


        lis = response.xpath('//div[@class="card m-panel card28 m-avatar-box"]')

        for li in lis:
            name = li.xpath('.//div[@class="m-text-box"]/h3/span/text()').get()
            fensi = li.xpath('.//div[@class="m-text-box"]/h4[last()]/text()').get()



            item = XlwbItem(name=name,fensi=fensi)

            yield item


    # 重写父类方法，用于关闭浏览器
    def closed(self, spider):
        """此方法在爬虫程序结束时执行，注意：只会执行一次"""
        self.LLQ.quit()
        print('爬取结束')


