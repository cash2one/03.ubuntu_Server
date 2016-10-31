# -*- coding: utf-8 -*-
import scrapy


class LoldyttSpider(scrapy.Spider):
    name = "loldytt"
    allowed_domains = ["loldytt.com"]
    start_urls = (
        'http://www.loldytt.com/',
    )

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.body)
        pass
    def closed(self,reason):
        pass
