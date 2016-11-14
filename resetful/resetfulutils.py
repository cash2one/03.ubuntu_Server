# -*- coding:utf8 -*-
from aria2.pyaria2 import *
from database.movieDB import MovieModule,connect,close,movieinfo as Movie_tb,links as Links_tb
import urllib

aria2 = PyAria2()
print aria2.getGlobalOption()

def download(id,path='/data/download'):
    data = [dic for dic in  Links_tb.select().where(Links_tb.id == id).dicts()]
    print data
    result = []
    if len(data) > 0:
        gid = data[0]['gid']

        if gid == None:
            print data[0]['sourceurl']
            print urllib.unquote(data[0]['sourceurl'])
            print urllib.unquote(data[0]['sourceurl']).decode("utf8","ignore")
            gid = aria2.addUri([urllib.unquote(data[0]['sourceurl'])],{"dir":path})
            result = aria2.tellStatus(gid)
        else:
            result = aria2.tellStatus(gid)
        query = Links_tb.update(gid = gid,status=result['status'],downloadpath=result['files'][0]['path']).where(Links_tb.id == id)
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


