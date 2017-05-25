# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymongo
from CrawlSpider1.items import MyItem,BlogItem


class Crawlspider1Pipeline(object):
    # 调用scrapy提供的json export导出json文件
    def __init__(self):
        self.client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        # 数据库登录需要帐号密码的话
        # self.client.admin.authenticate(settings['MINGO_USER'], settings['MONGO_PSW'])


    def open_spider(self, spider):
        if spider.name=="yhd":
            self.db = self.client[settings['MONGO_DB1']]  # 获得数据库的句柄
            self.coll = self.db[settings['MONGO_COLL1']]  # 获得collection的句柄
        elif spider.name=="blog":
            self.db = self.client[settings['MONGO_DB2']]  # 获得数据库的句柄
            self.coll = self.db[settings['MONGO_COLL2']]  # 获得collection的句柄


    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写


