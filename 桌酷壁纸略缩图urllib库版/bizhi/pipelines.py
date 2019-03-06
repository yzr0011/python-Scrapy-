# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request

class BizhiPipeline(object):

    def __init__(self):
        self.path = os.path.dirname(os.path.dirname(__file__))
        self.tp_path = os.path.join(self.path,'images')
        # if not self.tp_path:
        #     os.mkdir(self.tp_path)
        if not os.path.exists(self.tp_path):
            os.mkdir(self.tp_path)


    def process_item(self, item, spider):
        fl = item['fl']
        urls = item['urls']

        fl_path = os.path.join(self.tp_path,fl)
        if not os.path.exists(fl_path):
            os.mkdir(fl_path)
        for url in urls:
            image_name = url.split('/')[-1]
            request.urlretrieve(url,os.path.join(fl_path,image_name))


        return item
