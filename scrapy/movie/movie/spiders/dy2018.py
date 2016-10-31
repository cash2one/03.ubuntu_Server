# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Dy2018Spider(CrawlSpider):
    name = "dy2018"
    allowed_domains = ["dy2018.com"]
    start_urls = (
        'http://www.dy2018.com/html/gndy/dyzz/',
    )

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('/index.*\.html', )),follow= True),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('/i/\d+.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
        print response
        pass