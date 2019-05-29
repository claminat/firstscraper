# -*- coding: utf-8 -*-
import sys,os
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from scrapy.utils.conf import closest_scrapy_cfg

from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import Request
from time import sleep
from scrapy.spider import Spider
from scrapy import Request

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
ROOT_DIR = os.path.dirname(closest_scrapy_cfg())
print('ROOT_DIR',ROOT_DIR)
CHROME_DIR = '%s\\chromedriver_win32\\chromedriver.exe' % ROOT_DIR
print('CHROME_DIR',CHROME_DIR)
options = webdriver.ChromeOptions()
# options.add_argument('headless')


class FacebookbotSpider(scrapy.Spider):
    
    name = 'facebookbot'
    start_urls = [
        'https://www.facebook.com/gearvnhcm/videos/246895112850145/'
    ]
#
    def scroll_until_loaded(self):
        check_height = self.driver.execute_script("return document.body.scrollHeight;")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: self.driver.execute_script("return document.body.scrollHeight;")  > check_height)
                check_height = self.driver.execute_script("return document.body.scrollHeight;") 
            except TimeoutException:
                break
    # def __init__(self):
    #     html_path='G:\\Qing\\Source\\Python\\firstscraper\\'
    #     self.path_to_html = html_path + 'index.html'
    def __init__(self):
       self.browser = webdriver.Chrome(executable_path=CHROME_DIR,chrome_options=options)

       
    def parse(self, response):
      sel = Selector(response)
      html = self.browser.page_source
      print('html',html)

      print('############################################################################################')






      # with open(self.path_to_html, 'w') as html_file:
      #   html_file.write(response.body)  

      self.log('A response from %s just arrived!' % response.url)
      print('crawling...')

    #   self.scroll_until_loaded()
    #   titles = response.css('title::text').extract()
    #   print ('#titles',titles)

      hxs = HtmlXPathSelector(response)

      SET_SELECTOR = '//a'
    #   SET_SELECTOR = '//div[contains(@id, "comment_js")]'
    #   SET_SELECTOR = 'div[id*=comment_js]'
      SET_SELECTOR = '//div[contains(@id, "comment")]/@id'
    #   SET_SELECTOR = '#comment_js_2an'
    #   SET_SELECTOR = '//img[contains(@src, "scontent.fsgn5-2.fna.fbcdn.net")]'
      print('############################################################################################')
      print ('#comment_js',response.xpath(SET_SELECTOR).extract())
    #   print ('#comment',response.css(SET_SELECTOR))
    #   print ('#comment',response.css(SET_SELECTOR).extract())

    #   print ('#html',response.css('html').extract())
    #   print ('#head',response.xpath('//*[@id="facebook"]/head').extract())
    #   print ('#body',response.xpath('//*[@id="facebook"]/body').extract())
      
      print('############################################################################################')
      yield {'status': 'ok'}


    # #   for item in hxs.select().extract():
    #   for item in response.xpath(SET_SELECTOR).getall():
    # #   for item in response.css(SET_SELECTOR).getall():
    #      print('############################################################################################')
    #      print('#item',item)
    #      print('############################################################################################')

    # #   for item in response.css(SET_SELECTOR):
    # #     #   print('############################################################################################')
    # #     #   print('#item',item)
    # #     #   print('############################################################################################')
    # #       NAME_SELECTOR = 'h1 ::text'
    # #       LINK_SELECTOR='div.meta h1 a::attr(href)'
    # #       yield {
    # #         'name': item.css(NAME_SELECTOR).extract_first(),
    # #         'link': item.css(LINK_SELECTOR).extract_first(),
    # #         'spider': 'brickset'
    # #         }
     
    # # # NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
    # # # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
    # # # if next_page:
    # # #     yield scrapy.Request(
    # # #         response.urljoin(next_page),
    # # #         callback=self.parse
    # # #     )
     


















