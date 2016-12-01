# -*- coding:utf8 -*-
from aria2.pyaria2 import *
from database.datamodule import before_request_handler,after_request_handler,tb_movies,tb_links
import urllib

def init_aria2():
    aria2 = PyAria2()
    return aria2

def download(id,path='/data/download'):
    aria2 = init_aria2()
    data = [dic for dic in  tb_links.select().where(tb_links.id == id).dicts()]
    print data
    result = []
    if len(data) > 0:
        gid = data[0]['gid']

        if len(gid) == 0:
            print urllib.unquote(data[0]['sourceurl'].encode('UTF-8'))
            gid = aria2.addUri([urllib.unquote(data[0]['sourceurl'].encode('UTF-8'))],{"dir":path})
            result = aria2.tellStatus(gid)
        else:
            result = aria2.tellStatus(gid)
        print "-"*100
        print result
        print "-"*100
        query = tb_links.update(gid = gid,status=result['status'],downloadpath=result['files'][0]['path']).where(tb_links.id == id)
        query.execute()

        print result['status']
    return result
    pass


# print gid
#
# while True:
# 	result =  a.tellStatus(gid)
# 	print result
# 	print "speed:%(downloadSpeed)s \tstate:%(status)s\t %(completedLength)s | %(totalLength)s" % result
# 	time.sleep(1)


