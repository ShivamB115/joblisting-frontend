import platform
import asyncio

# Ensure compatibility with Windows
if platform.system() == 'Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Install the AsyncioSelectorReactor
from twisted.internet.asyncioreactor import install
install()

BOT_NAME = "job_scraper"

SPIDER_MODULES = ["job_scraper.spiders"]
NEWSPIDER_MODULE = "job_scraper.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'DEBUG'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

ITEM_PIPELINES = {
    'job_scraper.pipelines.MySqlPipeline': 300,
}

