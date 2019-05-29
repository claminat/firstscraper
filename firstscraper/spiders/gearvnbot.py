import scrapy, sys, os
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from time import sleep
from scrapy.spider import Spider
from scrapy import Request

class GearvnbotSpider(scrapy.Spider):
    name = 'gearvnbot'
    allowed_domains = ['gearvn.com']
    start_urls = ['https://gearvn.com']

    def parse(self, response):
        print 'crawling...'
        hxs = HtmlXPathSelector(response)
        SET_SELECTOR = '//*[@id="megamenu-nav-main"]/li/a/span'
        SET_SELECTOR = '//span[@class="gearvn-cat-menu-name"]'
        SET_SELECTOR = '//a[@class="gearvn-cat-menu-item"]'
        links = hxs.select(SET_SELECTOR)
        i = 0
        for link in links:
            SPAN_SELECTOR = './/span[@class="gearvn-cat-menu-name"]'
            for span in link.select(SPAN_SELECTOR):
                i = i + 1
                print '############################################################'
                text = span.select('.//text()').extract_first()
                print ('text', text)
                print '%s text %s ' % (i, str(text))
                yield {'text': text}
