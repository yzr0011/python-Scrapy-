# -*- coding: utf-8 -*-

BOT_NAME = 'jd_xlwb'
SPIDER_MODULES = ['jd_xlwb.spiders']
NEWSPIDER_MODULE = 'jd_xlwb.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2

DEFAULT_REQUEST_HEADERS = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
'Referer': 'https://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=https%3A%2F%2Fweibo.com%2F&domain=.weibo.com&sudaref=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DNTrPiwAkIpQb8RjakHhvajeBdUQfFytyTi2M97YzLUa%26wd%3D%26eqid%3Dd5322a2e0001b500000000045c7b1e9b&ua=php-sso_sdk_client-0.6.28&_rand=1551572639.1591',
    'Cookie': 'SINAGLOBAL=7307331493222.744.1543980518857; UM_distinctid=1687031f3cc380-034c06050d384-6313363-144000-1687031f3cd275; UOR=www.baidu.com,weibo.com,www.baidu.com; SCF=AotCX7xlEMe-FFfYHJQ1Pi32jlE7OYyYP_N7QmQi220s3ixT49J7c7CpRTO9sE0m8cLMb4Q-lgvkaQL1hmNwTfU.; SUHB=09Pt3J1pihuo87; Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5igOpFEFT9F46ucG7AHINI; login_sid_t=8bbe78366f3354e21752f68bb577bd2a; cross_origin_proto=SSL; YF-V5-G0=a9b587b1791ab233f24db4e09dad383c; _s_tentry=passport.weibo.com; wb_view_log=1536*8641.25; Apache=1691881967508.302.1551572616170; ULV=1551572616184:14:2:1:1691881967508.302.1551572616170:1551487048369; YF-Page-G0=d0adfff33b42523753dc3806dc660aa7; SUB=_2AkMrJ63pf8NxqwJRmPoWzGLhaY5-zAzEieKde1wyJRMxHRl-yj83qnQ6tRB6AKeDBrw3hXPY_ysfs8CUgAYX06pPYG4R'
}

DOWNLOADER_MIDDLEWARES = {
    'jd_xlwb.middlewares.QQT': 100,
    'jd_xlwb.middlewares.TestDownloaderMiddleware': 200,
    }


ITEM_PIPELINES = {
   'jd_xlwb.pipelines.YBmysql': 300,

    }
