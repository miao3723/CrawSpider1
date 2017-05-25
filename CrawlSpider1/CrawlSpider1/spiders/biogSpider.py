# -*- coding:utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor as le
from jieba import analyse
from goose import Goose
from goose.text import StopWordsChinese
from CrawlSpider1.items import BlogItem
class blogSpider(CrawlSpider):
    name="blog"

    allowed_domains = ['163.com']
    start_urls = [
        'http://blog.163.com/'
    ]

    rules = [
        Rule(le(allow=('^http://blog.163.com/')), follow=True),
        Rule(le(allow=('blog/static/\d*/')),callback='parse_abstract'),

    ]

    def parse_abstract(self, response):
        url = response.url
        g = Goose({'stopwords_class': StopWordsChinese})
        article = g.extract(url=url)
        # 引入TF-IDF关键词抽取接口
        tfidf = analyse.extract_tags

        text=article.cleaned_text
        # 基于TF-IDF算法进行关键词抽取
        tkeywords = tfidf(text)

        allkeyword="/".join(tkeywords)
        item = BlogItem()
        item['keyworld'] = article.cleaned_text[:50]
        item['abstract'] = allkeyword
        return item



