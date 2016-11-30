# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from database.movieDB import MovieModule
from scrapy.exceptions import DropItem
from database.datamodule import tb_movies,tb_links,create_table,before_request_handler

from oss.oss import OssSDK

class MoviePipeline(object):

    def __init__(self):
        create_table()
        before_request_handler()
        self.oss = OssSDK('x2020-movie')
        pass

    def process_item(self, item, spider):

        for key in item:
            item[key] = item[key].replace("'","")

        if (item['cate'].find(u'综艺') < 0 ) and len(item['link']) > 0  and len(item['title']) > 0:

            # print '-'*100
            # print item['name']
            # print item['title']
            # print item['cate']
            # print item['img']
            # print item['link']
            # print '='*100

            # 如果没有重复
            if tb_movies.select().where(tb_movies.title==item['title']).count() == 0:

                # 下载图片
                item['img'] = self.oss.put_url_auto_name(item['img'])

                # 插入数据库
                tb_movies.create(title=item['title'],cate=item['cate'],img=item['img'],name=item['name'],url=item['url'])

                # 更新链接
                id = tb_movies.get(tb_movies.title==item['title']).id
                for link in item['link'].split('\n'):
                    tb_links.insert(movie=id,sourceurl=link).execute()

                return item
            else:
                raise DropItem(u"重复项: %s" % item['title'])
        else:
            raise DropItem(u"无效项: %s" % item['title'])


    def download_img(self,url):
        pass