# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from database.movieDB import MovieModule
from scrapy.exceptions import DropItem
from database.datamodule import tb_movies,tb_links,tb_doubans,create_table,before_request_handler
from douban import DoubanMovie
from celery_app.task_movie import upload_image
from oss.oss import OssSDK

class MoviePipeline(object):

    def __init__(self):
        create_table()
        before_request_handler()
        self.oss = OssSDK('x2020-movie')
        self.douban = DoubanMovie()
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

            # 如果没有重复
            if tb_movies.select().where(tb_movies.title==item['title']).count() == 0:

                if len(item['img']) > 0:
                    # 下载图片
                    upload_image.delay(item['img'],item['title'])
                    pass

                # 插入数据库
                tb_movies.insert(title=item['title'],cate=item['cate'],img=item['img'],name=item['name'],org_url=item['url']).execute()

                # 更新链接
                id = tb_movies.get(tb_movies.title==item['title']).id
                for link in item['link'].split('\n'):
                    tb_links.insert(movie=id,sourceurl=link).execute()

                # search douban by name
                i = self.douban.searchMovie(item['name'])
                if i.has_key('url'):
                    data = self.douban.detailInfo(i['url'])
                    # get detial info
                    if data.has_key('title'):
                        # 将电影保存到豆瓣数据库中
                        tb_doubans.insert(movie=id,title=data['title'],year=data['year'],douban_url=data['alt'],rating=data['rating'],directors=data['directors'],genres=data['genres'],pubdates=data['pubdates'],rating_betterthan=data['rating_betterthan'],summary=data['summary'],info=data['info']).execute()
                return item
            else:
                raise DropItem(u"重复项: %s" % item['title'])
        else:
            raise DropItem(u"无效项: %s" % item['title'])


    def download_img(self,url):
        pass