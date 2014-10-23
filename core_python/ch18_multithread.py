#! /usr/bin/env python

import threading
from random import randint
from Queue import Queue

from time import sleep, ctime

loops = [4,2]

def loop(nloop, nsec):
    print 'before sleep:', nloop, nsec, ctime()
    sleep(nsec)
    print 'after sleep:', ctime()

def main():
    print 'in main:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()
       
    for i in nloops:
        threads[i].join()
    print 'all done', ctime()

class MyThread(threading.Thread):
    def __init__(self, func, args):
        super(MyThread, self).__init__()
        #threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        apply(self.func, self.args)

class ManageQueue(object):
    def __init__(self, sz):
        self.qu = Queue(sz)
        self.wq = MyThread(gWriteQ, (self.qu, 1, 1))
        self.rq = MyThread(gReadQ, (self.qu, 2, 2))
        self.lsq = MyThread(gLsQ, (self.qu, 3, 0.5))
    def start(self):
        self.wq.start()
        self.rq.start()
        self.lsq.start()

def gWriteQ(qu, tid, t):
    print 'writeQ,tid=', tid
    n = 1
    while True:
        print 'write n=', n
        qu.put(n)
        n += 1
        sleep(t)
def gReadQ(qu, tid, t):
    print 'readQ,tid=', tid
    while True:
        print 'read val=', qu.get()
        sleep(t)
def gLsQ(qu, tid, t):
    print 'lsQ,tid=', tid
    while True:
        print 'queue size=', qu.qsize()
        sleep(t)

def createQ(sz = 100):
    qu = Queue(sz)
    wq = MyThread(gWriteQ, (qu, 1, 1))
    rq = MyThread(gReadQ, (qu, 2, 3))
    lsq = MyThread(gLsQ, (qu ,3, 0.5))
    wq.start()
    rq.start()
    lsq.start()


if __name__ == '__main__':
    #main()

    #createQ(10)

    #mq = ManageQueue(10)
    #mq.start()
