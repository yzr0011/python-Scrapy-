# -*- coding: utf-8 -*-
import scrapy



class JDItem(scrapy.Item):
    name = scrapy.Field()   ##名字
    jg = scrapy.Field()     ##价格
    zy = scrapy.Field()     ##是否自营



