# -*- coding: utf-8 -*-
import subprocess
import os
import time
from common.tools import *
from weixin.weixin import startweixin
from movie.movieflask import startmovie
def isRunning(name):
    pgrep_process = subprocess.Popen('pgrep -l %s'%name, shell=True, stdout=subprocess.PIPE)

    if pgrep_process.stdout.readline() == b'':
        return False
    else:
        return True

def Run(cmd):
    subprocess.Popen(cmd, shell=True)
    pass


def runWeixin():
    cmd = 'python'\
          ' weixin/weixin.py'
    if not isRunning('weixin'):
        Run(cmd)
    else:
        print "weixin has been start"

if __name__ == '__main__':

    # 开始一次
    sync(startweixin,5001)
    sync(startmovie,5002)

    # 循环任务
    count = 1
    SCRAPY_MOVIE = 60 * 60 * 12
    MAX = SCRAPY_MOVIE + 1

    while True:

        if count % SCRAPY_MOVIE == 0:
            print "-"*50
            print "\nstart scrapy\n"
            sync(Run,'scrapy crawl dy2018 >>scrapy.log')

        if count % 2 == 0:
            print "2"

        count =(count + 1) % MAX

        time.sleep(1)

        pass
