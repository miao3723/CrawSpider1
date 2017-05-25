# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawlspider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MyItem(scrapy.Item):
    name=scrapy.Field()
    price=scrapy.Field()


class BlogItem(scrapy.Item):
    keyworld=scrapy.Field()
    abstract=scrapy.Field()


