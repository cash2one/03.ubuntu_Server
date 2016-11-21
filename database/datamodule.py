# -* - coding: UTF-8 -* -
from common.config import *

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

DATABASE = getmoviedb()

database_object = SqliteDatabase(DATABASE)

def create_table():
    database_object.create_table(tb_links,safe=True)
    database_object.create_table(tb_movies,safe=True)

def before_request_handler():
    database_object.connect()

def after_request_handler():
    database_object.cloes()




class BaseModel(Model):
    class Meta:
        database = database_object


class tb_movies(BaseModel):
    id = IntegerField(primary_key=True)
    title =TextField(default=u'')

    name = TextField(default=u'')
    cate = TextField(default=u'')
    rank = TextField(default=u'')
    actor = TextField(default=u'')
    updatetime = TextField(default=u'')
    img = TextField(default=u'')

class tb_links(BaseModel):
    id = IntegerField(primary_key=True)
    movieinfoid = ForeignKeyField(tb_movies,related_name='links')

    gid = TextField(default=u'')
    status = TextField(default=u'')
    sourceurl=TextField(default=u'')
    downloadpath = TextField(default=u'')
    playpath = TextField(default=u'')


class testdb(BaseModel):
    id = IntegerField(primary_key=True)
    name = TextField(default=u'')
