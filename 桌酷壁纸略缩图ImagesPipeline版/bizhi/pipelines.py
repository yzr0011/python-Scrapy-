# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import os
# from urllib import request
import os
from scrapy.pipelines.images import ImagesPipeline
from bizhi import settings



class BZImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):

        ##这个方法是在发送下载请求之前调用
        ##其实这个方法本身就是去发送下载请求的
        request_objs = super(BZImagesPipeline, self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):


        path = super(BZImagesPipeline, self).file_path(request,response,info)
        fl = request.item.get('fl')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store,fl)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace("full/","")           ##########将full/ 替换成空的就拿到了图片的名字，然后我们再把这个拼接到category_path后面


        image_path = os.path.join(category_path,image_name)###############再把这个返回回去，得到的就是真正的分类的路径
        return image_path