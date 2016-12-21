# -*- coding:utf8 -*-
import multiprocessing

def sync(targget,args):
    p = multiprocessing.Process(target = targget, args = args)
    p.daemon = False
    p.start()