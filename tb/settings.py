# -*- coding: utf-8 -*-

# Scrapy settings for tb project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tb'



# IPPOOL=[
#          {"ipaddr":"45.124.24.38:1080"},
#          {"ipaddr":"114.116.75.60:50053"},
#          {"ipaddr":"132.232.173.90:29552"},
         # {"ipaddr":"221.229.227.251:55649"},
         # {"ipaddr":"115.210.69.173:44003"},
         # {"ipaddr":"14.134.184.196:51531"},
         # {"ipaddr":"101.205.161.75:47573"}
# ]


SPIDER_MODULES = ['tb.spiders']
NEWSPIDER_MODULE = 'tb.spiders'


# SPLASH_URL = 'http://localhost:8050'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL ="WARNING"
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tb.middlewares.TbSpiderMiddleware': 543,
# }

#设置去重过滤器
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
   #  'tb.middlewares.MyproxiesSpiderMiddleware': 125,
   # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None    # 关闭默认方法
   'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware':400,# 开启

   # 'tb.middlewares.UseAgentMiddleware': 300,
   'tb.middlewares.TbDownloaderMiddleware': 543,
}
# DOWNLOADER_MIDDLEWARES = {
#      'scrapy_splash.SplashCookiesMiddleware': 723,
#      'scrapy_splash.SplashMiddleware':725,
#      'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,
#  }



#用来支持cache_args（可选）
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
#  }
#
# DUPEFILTER_CLASS ='scrapy_splash.SplashAwareDupeFilter'
# HTTPCACHE_STORAGE ='scrapy_splash.SplashAwareFSCacheStorage'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tb.pipelines.TbPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
# 端口号，默认27017
MONGODB_PORT = 27017
MONGODB_DBNAME ='Tieba'
MONGODB_DOCNAME ='data'
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
