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
       # Rule(LinkExtractor(allow=('/[a-zA-Z]+', ),deny=('/tag/.*','/wp-login\.php.*' )),follow= True),

        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('\d+\.html', )), callback='parse_item'),
    )

    def parse_item(self, response):
	print "-"*100
	print response.url
	print "="*100
        sel = Selector(response)
        item = MovieInfo()


        item['title'] =  u''.join(sel.xpath('//span[@class="current"]/text()').extract())
        item['name'] = u''.join(sel.xpath('//meta[@name="description"]/@content').extract())
        item['cate']  = u''.join(sel.xpath('//a[@itemprop="breadcrumb"]/text()').extract())

        item['img'] =  u''.join(sel.xpath('//div[@id="post_content"]/p/a/@href').extract())
        #item['link'] = u'\n'.join(sel.xpath('//td[@bgcolor]/a/text()').extract())

        print '-'*100
       # print  startindex
       # print endindex
        print item['name']
        print item['title']
        print item['cate']
        print item['img']
        print '='*50
        return item

    def closed(self, reason):
        print("HdwanSpider Closed:" + reason)
