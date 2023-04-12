# Scrapy settings for jobFinding project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "jobFinding"

SPIDER_MODULES = ["jobFinding.spiders"]
NEWSPIDER_MODULE = "jobFinding.spiders"
LOG_LEVEL = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "jobFinding (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 4
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    ##'Cookie': '__uuid=1677823442071.69; __gc_id=5a141878201f429ab72ec2fcd0c015d9; need_bind_tel=false; c_flag=76a1108ffdaf307e61f9a20e2aa16933; imClientId_2=4522edc9da582c00bb3e4897c8165e6e; imId_2=4522edc9da582c00459a254ada6f4751; imClientId=4522edc9da582c00fec3b4a41e91377d; imId=4522edc9da582c0039bd05f7813ca38a; imClientId_0=4522edc9da582c00fec3b4a41e91377d; imId_0=4522edc9da582c0039bd05f7813ca38a; __tlog=1678003839694.06%7C00000000%7C00000000%7C00000000%7C00000000; __session_seq=1; __uv_seq=11; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1677823458,1677990930,1678003840; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1678003840; acw_tc=2760829916780038396481750e9e65f13d39cebb8ea3e3bd29784f0bdce7ca; XSRF-TOKEN=S8o0tJRiRCawVri_cmHcHA',
    'X-Client-Type': 'web',
    'X-Fscp-Bi-Stat': '{"location": "https://www.liepin.com/zhaopin/?key=%E4%BF%9D%E6%B4%81"}',
    'X-Fscp-Fe-Version': '9bc4a50',
    'X-Fscp-Std-Info': '{"client_id": "40108"}',
    'X-Fscp-Trace-Id': 'cedf6df4-0c33-409d-b638-fde3777848a0',
    'X-Fscp-Version': '1.1',
    'X-Requested-With': 'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "jobFinding.middlewares.JobfindingSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "jobFinding.middlewares.JobfindingDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "jobFinding.pipelines.JobfindingDB": 30,
    "jobFinding.pipelines.JobfindingExcel": 1,
    #"jobFinding.pipelines.JobfindingVision": 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
