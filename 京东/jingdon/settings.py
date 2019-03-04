# -*- coding: utf-8 -*-

BOT_NAME = 'jingdon'
SPIDER_MODULES = ['jingdon.spiders']
NEWSPIDER_MODULE = 'jingdon.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 0.3

DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

DOWNLOADER_MIDDLEWARES = {
    'jingdon.middlewares.QQT': 100,

    }


ITEM_PIPELINES = {
   'jingdon.pipelines.YBmysql': 300,

    }
