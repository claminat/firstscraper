# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import psycopg2
import json
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log




class Pipeline(object):
    def process_item(self, item, spider):
        # print('############################################################################################')
        # print('PipelineItem',item)
        # print('############################################################################################')
        return item
class MongoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
    def process_item(self, item, spider):
        valid = True
        for key in item:
            if not key:
                valid = False
                raise DropItem("Missing {0}!".format(key))
            # if key == 'spider':
            #     print('data',key)
            #     print('############################################################################################')
            
        if valid:
            self.collection.insert(dict(item))
            log.msg("Added to MongoDB database!",level=log.DEBUG, spider=spider)
        return item
class PostgresPipeline(object):

    def open_spider(self, spider):
        self.connection = psycopg2.connect(host=settings['POSTGRES_SERVER'], user=settings['POSTGRES_USERNAME'], password=settings['POSTGRES_PASSWORD'], dbname=settings['POSTGRES_DATABASE'], port=settings['POSTGRES_PORT'])
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute('insert into gearvn(content,author) values(%s,%s)', (item['text'], item['text']))
        self.connection.commit()
        log.msg("Added to Postgres database!",level=log.DEBUG, spider=spider)
        return item