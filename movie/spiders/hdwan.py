# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from movie.items import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class HdwanSpider(CrawlSpider):
    name = "hdwan"
    allowed_domains = ["hdwan.net"]
    start_urls = ['http://www.hdwan.net/']

    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        Rule(LinkExtractor(allow=('[a-zA-Z]*/page/\d+', ),deny=('/tag/.*','/wp-login\.php.*' )),follow= True),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('\d+\.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = MovieInfo()

        print response.url
        item['title'] =  u''.join(sel.xpath('//span[@class="current"]/text()').extract())
        item['name'] = u''.join(sel.xpath('//meta[@name="description"]/@content').extract()).replace(u"影片名：", u"")
        
        if item['name'].find(u"。") > 0:
            item['name'] = item['title']
            
        if len(sel.xpath('//a[@itemprop="breadcrumb"]/text()').extract()) > 1:
            item['cate']  = u''.join(sel.xpath('//a[@itemprop="breadcrumb"]/text()').extract()[1])
        else:
            item['cate'] = u''

        if len(sel.xpath('//div[@id="post_content"]/p/a/@href').extract()) > 0:
            item['img'] =  u''.join(sel.xpath('//div[@id="post_content"]/p/a/@href').extract()[0])
        else:
            item['img'] = u''

        item['link'] = u''.join(sel.xpath('//div[@class="dw-box dw-box-download"]/a/@href').extract())


        return item

    def closed(self, reason):
        print("HdwanSpider Closed:" + reason)


