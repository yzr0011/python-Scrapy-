# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
import pymysql

from pymysql import cursors
import json
from twisted.enterprise import adbapi

import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from taobao import settings

class TaobaoPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': '*******************************',
            'database': 'taobao',  ##数据库名
            'port': 3306,  ##端口号
            'charset': 'utf8',  ##编码格式
            'cursorclass': cursors.DictCursor  #####定义游标的类   如果不声明，那么底层就不知道使用哪个游标了

        }
        ############接下来定义一个连接池

        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:  ###如果没有_sql这个对象  就创建
            self._sql = """
                insert into tb(id,title,view_price,view_sales) values(null,%s,%s,%s)
                """  ###id是设置自动增长的  传入null
            return self._sql
        return self._sql  ####如果有的话就直接执行返回_sql

    def process_item(self, item, spider):  ###再定义处理item的函数
        defer = self.dbpool.runInteraction(self.insert_item,item)  ###括号内指定“插入item”函数  底层会调用  底层调用可以使用异步      这样会返回defer对象
        ###再为defer添加错误处理，就是说如果调用“插入item”函数出现错误就去执行另外一个函数
        defer.addErrback(self.handle_error, item, spider)

    def insert_item(self, cursor, item):  ####传入游标及item的对象    “插入item”函数
        cursor.execute(self.sql, (item['title'], item['view_price'], item['view_sales']))

    def handle_error(self, error, item,
                     spider):  ####首先会有错误参数，别的在上面传入上面addErrback传入什么参数这里就有什么参数   item,spider在处理什么item和什么爬虫时出现问题
        print('=' * 10 + '错误' + '=' * 10)  #####ss这样会更方便观察错误
        print(error)
        print('=' * 10 + '错误' + '=' * 10)
