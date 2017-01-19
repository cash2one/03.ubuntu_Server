import time
from celery_app import app
from common.tools import *

@app.task
def scrapy_movie(spider):
    Run("scrapy crawl %s >%s_scrapy.log"%(spider,spider))
    pass

@app.task
def oss_upload():
    pass


@app.task
def test(x,y):
    print "hello"
    pass