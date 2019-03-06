# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BizhiItem(scrapy.Item):

    fl = scrapy.Field()
    image_urls = scrapy.Field()



    ##要加一个images
    images = scrapy.Field()
