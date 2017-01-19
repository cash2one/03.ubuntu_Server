# -*- coding:utf8 -*-
import multiprocessing
import subprocess

pid_list = []

def sync(targget,args):
    p = multiprocessing.Process(target = targget, args = args)
    p.daemon = False
    p.start()

def isRunning(name):
    pgrep_process = subprocess.Popen('pgrep -l %s'%name, shell=True, stdout=subprocess.PIPE)
    pid = pgrep_process.stdout.readline().split(" ")

    if len(pid)  < 0:
        return False
    else:
        print "Append pid %s" %pid[0]
        pid_list.append(pid[0])
        return True

def KillAll():
    for pid in pid_list:
        print "杀死进程 %s" % pid
        subprocess.Popen("kill -9 %s" % pid,shell=True)

def Run(cmd,log="",kill=True):
    pid = subprocess.Popen(cmd, shell=True).pid
    print "启动%s 进程id:%s" %(log,pid)
    if kill:
        pid_list.append(pid)
    pass
