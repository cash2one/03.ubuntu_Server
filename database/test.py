from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

database = SqliteDatabase('movie.db')
database.connect()

import json
class BaseModel(Model):
    class Meta:
        database = database

class links(BaseModel):
    id = IntegerField()
    movieinfoid = IntegerField()

    gid = TextField()
    status = TextField()
    sourceurl=TextField()
    localpath = TextField()
    remotepath = TextField()

class movieinfo(BaseModel):

    id = IntegerField()
    title =TextField()

    name = TextField()
    cate = TextField()
    rank = TextField()
    actor = TextField()
    updatetime = TextField()
    img = TextField()



print json.dumps([dic for dic in movieinfo.select().dicts()])