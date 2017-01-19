# -*- coding: utf-8 -*-

import time


from common.tools import *
from resetful.resetfulapi import startresetful
import os
from weixin.weixin import startweixin
from celery_app.task_movie import scrapy_movie

if __name__ == '__main__':

    try:
        # start celery
        Run("celery -B -A celery_app worker --loglevel=warning","启动celery",kill=True)
        scrapy_movie.delay('hdwan')
        function_list=  [startresetful, startweixin]
        print "主程序进程id: %s" %(os.getpid())
        pool=multiprocessing.Pool(2)
        for func in function_list:
            pool.apply_async(func)

        print '等待所有进程结束'
        pool.close()
        pool.join()

    except (KeyboardInterrupt, SystemExit):
        # 异常退出,关闭用run启动的进程
        KillAll()
