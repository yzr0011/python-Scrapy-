# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 8
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'cookie': 'thw=cn; cna=COx/FBETOxMCAX16iv5x1Rom; t=e755ba807cd569f4f4e051010b13eca5; tg=0; miid=1076012989469566204; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=n7UEOypja0WU3uWuzGL9IWRX9LHVtkQ1WdBTo4yTRcI5d8v5L0ZH11RUvrNXzkd%2BOeZli7RWSLA%2FcyPYVnE%2Fow%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; _m_h5_tk=01ed4cd8b20c8d35cbff811e66293907_1551859940089; _m_h5_tk_enc=33f82864b762422e3b29da7d21a90b25; _uab_collina=155195288910465906797741; cookie2=37a412e5183506355c0cd7c2830ee6cd; _tb_token_=e68a87eb43d36; v=0; unb=2930320353; sg=x3e; _l_g_=Ug%3D%3D; skt=6795d1de75c91926; cookie1=BqeF%2By3FPxap%2BlJ3xT00ZKZD9%2Fr%2BDfysTTxhaSlYBkU%3D; csg=7e78dd3c; uc3=vt3=F8dByEvyaphA6vSpWL4%3D&id2=UUGhbPer2Jg1Iw%3D%3D&nk2=p2NI8WJt&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; existShop=MTU1MjAxOTYwMQ%3D%3D; tracknick=%5Cu58A8%5Cu975Eyx; lgc=%5Cu58A8%5Cu975Eyx; _cc_=UtASsssmfA%3D%3D; dnk=%5Cu58A8%5Cu975Eyx; _nk_=%5Cu58A8%5Cu975Eyx; cookie17=UUGhbPer2Jg1Iw%3D%3D; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=UtASsssme%2BBq&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTZ5iV5abRdRw%3D%3D&tag=8&lng=zh_CN; mt=ci=-1_1; x5sec=7b227365617263686170703b32223a226465333761353837303464353339646131316431343866663135643064323238434a2f68682b5146454b69462b34714f3674664e6c774561444449354d7a417a4d6a417a4e544d374e673d3d227d; swfstore=18166; JSESSIONID=F92760C8CF68A5A980595B5B0D1BF41D; l=bBxNdjmuvI9VeYVBBOCNKRuVA8bOSIRAguuZ3ox6i_5Qb6YsmobOlsaAcFv6Vj5RsPYB4ATie6e9-etks; isg=BMLCu0wKKhxZKzE_QlGSmBhzE8hZ6U1PHHW5ugzb7jXgX2LZ9CMWvUiVDxuGDz5F; whl=-1%260%260%261552019899797'

            }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.SeleniumDownloadMiddleware': 543,
#
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao.pipelines.TaobaoPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
