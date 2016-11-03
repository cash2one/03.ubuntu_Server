# -*- coding:utf8 -*-
import sys,os
sys.path.append("../")
from common.config import *
from common.dbhelper import Table

DATABASE = getmoviedb()

class MovieInfo_tb(Table):

    def __init__(self, data_file=DATABASE):
        super(MovieInfo_tb, self).__init__(data_file, 'movieinfo',
                                   ['ID INTEGER PRIMARY KEY AUTOINCREMENT', 'title TEXT','name TEXT','cate TEXT','rank TEXT','actor TEXT','updatetime TEXT','img TEXT'])

    def select(self, *args, **kwargs):
        cursor = super(MovieInfo_tb, self).select(*args, **kwargs)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, *args):
        self.free(super(MovieInfo_tb, self).insert(*args))

    def update(self, set_args, **kwargs):
        self.free(super(MovieInfo_tb, self).update(set_args, **kwargs))

    def delete(self, **kwargs):
        self.free(super(MovieInfo_tb, self).delete(**kwargs))

    def delete_all(self):
        self.free(super(MovieInfo_tb, self).delete_all())

    def drop(self):
        self.free(super(MovieInfo_tb, self).drop())

    def exists(self, id):
        results = self.select('*', id=id)
        return len(results) > 0


class DownloadLink_tb(Table):

    def __init__(self, data_file=DATABASE):
        super(DownloadLink_tb, self).__init__(data_file, 'links',
                                   ['ID INTEGER PRIMARY KEY AUTOINCREMENT', 'movieinfoid INTEGER NOT NULL','gid TEXT','status TEXT','sourceurl TEXT','localpath TEXT','remotepath TEXT'])

    def select(self, *args, **kwargs):
        cursor = super(DownloadLink_tb, self).select(*args, **kwargs)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, *args):
        self.free(super(DownloadLink_tb, self).insert(*args))

    def update(self, set_args, **kwargs):
        self.free(super(DownloadLink_tb, self).update(set_args, **kwargs))

    def delete(self, **kwargs):
        self.free(super(DownloadLink_tb, self).delete(**kwargs))

    def delete_all(self):
        self.free(super(DownloadLink_tb, self).delete_all())

    def drop(self):
        self.free(super(DownloadLink_tb, self).drop())

    def exists(self, id):
        results = self.select('*', id=id)
        return len(results) > 0

class MovieModule():

    def __init__(self):
        self.movieinfo = MovieInfo_tb()
        self.link = DownloadLink_tb()
        self.id = 0

    def insert_movieinfo(self,**kwargs):
        self.movieinfo.insert_key(**kwargs)
        self.id = self.movieinfo.select_top('ID')


    def insert_linkinfo(self,**kwargs):
        self.link.insert_key(movieinfoid=self.id,**kwargs)


    def test(self):
        self.insert_movieinfo(title='a')
        self.insert_linkinfo(sourceurl='wwww.baidu.com')
        cursor =  self.movieinfo.select_all('*')
        print cursor.fetchall()
        cursor.close()