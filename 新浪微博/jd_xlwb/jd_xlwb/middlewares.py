# -*- coding: utf-8 -*-


from scrapy import signals
import random
import requests
import json

from twisted.internet.defer import DeferredLock
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse
import base64

from time import sleep
from scrapy.http import HtmlResponse  # 用于生成响应对象


# 下载中间件
class TestDownloaderMiddleware(object):

    def process_response(self, request, response, spider):
        """
        此方法用于拦截响应
        :param request: 当前响应对应的请求
        :param response: 响应
        :param spider: 爬虫类对象
        :return:
        """
        # 获取在爬虫类中创建好的浏览器对象
        LLQ = spider.LLQ
        LLQ.get(url=request.url)
        sleep(1)
        js = 'window.scrollTo(0, document.body.scrollHeight);'
        for i in range(10):  ###滚动10页的数据     如需爬取全部则使用while ture
            LLQ.execute_script(js)
            sleep(1)
            # 获取页面源码，这里有我们需要的动态加载的数据
            source = LLQ.page_source
            # 创建一个新的响应对象，并将动态加载到的数据存入该对象中，然后返回该对象

        return HtmlResponse(url=LLQ.current_url, body=source, encoding='utf-8', request=request)
            # bro.current_url：请求的url




class QQT(object):

    USER_AGENTS = [
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'


    ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENTS)
        request.headers['User-Agent'] = user_agent

