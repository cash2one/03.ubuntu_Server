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
        pass

    def process_item(self, item, spider):

        if (item['cate'].find(u'电影') > 0 or item['cate'].find(u'电视剧') > 0 ) and len(item['link']) > 0 :
            if not self.db.search_title_exist(item['title']):
                self.db.insert_movieinfo(title=item['title'],cate=item['cate'],img=item['img'],name=item['name'])
                for link in item['link'].split('\n'):
                    self.db.insert_linkinfo(sourceurl=link)

                return item
            else:
                raise DropItem("Duplicate item found: %s" % item)
        else:
            raise DropItem("Invalue item found: %s" % item)


