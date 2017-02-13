import time
from celery_app import app
from common.tools import *
from oss.oss import OssSDK
from database.datamodule import *

@app.task
def scrapy_movie(spider):
    Run("scrapy crawl %s >%s_scrapy.log"%(spider,spider))
    pass


@app.task
def upload_image(url,title):
    oss = OssSDK('x2020-movie')
    new_url = oss.put_url_auto_name(url)
    print new_url
    time.sleep(5)
    create_table()
    before_request_handler()
    tb_movies.update(img=new_url).where(tb_movies.title==title).execute()
    after_request_handler()
    pass

@app.task
def test(x,y):
    print "hello"
    pass