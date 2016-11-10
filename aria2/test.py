# -*- coding: utf-8 -*-

from pyaria2 import PyAria2
import time
a = PyAria2()
#print a.getGlobalOption()
gid = a.addUri([u'ftp://a:a@dygod18.com:21/[电影天堂www.dy2018.com]名侦探柯南：纯黑的噩梦BD日语中字.mkv'],{"dir":"/downloads"})

print gid

while True:
	result =  a.tellStatus(gid)
	print result
	print "speed:%(downloadSpeed)s \tstate:%(status)s\t %(completedLength)s | %(totalLength)s" % result
	time.sleep(1)