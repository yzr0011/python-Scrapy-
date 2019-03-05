# -*- coding: utf-8 -*-
import scrapy



class MubanItem(scrapy.Item):
    name = scrapy.Field()
    gs = scrapy.Field()
    nr = scrapy.Field()
    url = scrapy.Field()
