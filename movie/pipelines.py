# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from database.movieDB import MovieModule
from scrapy.exceptions import DropItem

class MoviePipeline(object):

    def __init__(self):
        self.db = MovieModule()
        self.sets = self.db.select_all("title")
        print self.sets
        pass

    def process_item(self, item, spider):

        for key in item:
            item[key] = item[key].replace("'","")

        if (item['cate'].find(u'综艺') < 0 ) and len(item['link']) > 0  and len(item['title']) > 0:

            print '-'*100
            print item['name']
            print item['title']
            print item['cate']
            print item['img']
            print item['link']
            print '='*100

            if not self.db.search_title_exist(item['title']):
                self.db.insert_movieinfo(title=item['title'],cate=item['cate'],img=item['img'],name=item['name'])
                for link in item['link'].split('\n'):
                    self.db.insert_linkinfo(sourceurl=link)
                return item
            else:
                raise DropItem(u"重复项: %s" % item['title'])
        else:
            raise DropItem(u"无效项: %s" % item['title'])


