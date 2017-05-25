# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as le
from scrapely import Scraper
from CrawlSpider1.items import MyItem
class MySpider(CrawlSpider):
    global s
    s= Scraper()
    url1 = 'http://item.yhd.com/item/16489452'
    data1 = {'name': '果仙多维V 冻干雪梨脆片 10g/包', 'price': '6.5'}
    s.train(url1, data1)


        # url1='http://item.yhd.com/item/66395326?tc=3.0.5.66395326.2&tp=52.5176.108.2.1.LjpVJeC-10-ElR`s&ti=2TC1BJ'
        # data1 = {'name': '【京东超市】维达（Vinda) 卫生纸 蓝色经典 卷纸3层180g*30卷', 'price': '113'}
        # s.train(url1, data1)

    name = 'yhd'
    allowed_domains = ['yhd.com']
    start_urls = [
        'http://www.yhd.com/marketing/allproduct.html'
    ]

    rules = [
        Rule(le(allow=('http://www.yhd.com/marketing/allproduct.html')), follow=True),
        Rule(le(allow=('^http://list.yhd.com/c.*//$')), follow=True),
        Rule(le(allow=('^http://list.yhd.com/c.*/b/a\d*-s1-v4-p\d+-price-d0-f0d-m1-rt0-pid-mid0-k/$')), follow=True),
        Rule(le(allow=('^http://item.yhd.com/item/\d+$')), callback='parse_item')
    ]

    def parse_item(self, response):
        dic=s.scrape(response.url)[0]
        self.logger.info('Hi, this is an item page! %s', response.url)

        item = MyItem()
        item['name'] = dic['name'][0]
        item['price'] = dic["price"][0]
        return item