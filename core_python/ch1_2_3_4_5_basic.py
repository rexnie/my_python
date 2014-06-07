#!/usr/bin/env python
import os
import types
import random

def makeTextFile():
    """read chars from console and write to file"""
    while True:
        fname = raw_input('enter filename to create:')
        if os.path.exists(fname):
            print "file exists"
        else:
            break
    #get file contents
    contents=[]
    print "\nEnter lines,'.' to quit\n"
    while True:
        entry = raw_input('> ')
        if entry =='.':
            break
        else:
            contents.append(entry)
        # write lines to file
    fobj = open(fname,'w')
    fobj.write("\n".join(contents))
    fobj.close()
    print 'Done'

def readTextFile():
    fn = raw_input("enter file name:")
    print
    try:
        fobj=open(fn,'r')
    except IOError,e:
        print "file open error:",e
    else:
        for el in fobj:
            print el,
        fobj.close()

def readTextFile2():
    fn = raw_input("enter file name:")
    print
    try:
        fobj=open(fn,'r')
    except IOError,e:
        print "file open error:",e
    else:
        for el in fobj:
            el = el.rstrip("\n")
            print el
        fobj.close()            

def displayNumType(num):
    print num, 'is ',
    "type(num) == type(0L)"
    "type(num) == types.IntType"
    if isinstance(num, (int,long,float,complex)):
        print 'a number of type:',type(num).__name__
    else:
        print 'not a number'

def getScore(sco=60.0):
    level = "D"
    if sco >= 90 and sco <= 100:
        level = "A"
    elif sco >= 80 and sco <= 89:
        level = "B"
    elif sco >= 70 and sco <= 79:
        level = "C"
    elif sco >= 60 and sco <= 69:
        level ="D"
    elif sco < 60 and sco >=0:
        level = "E"
    else:
        print "input error",sco

    print sco,level

def isLeapYear(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 == 0) and (year % 100 == 0)):
        leap = "yes"
    else:
        leap = "no"

    print leap

def randTest():
    list_num = 100
    lst = []
    MIN_NUM = 0
    MAX_NUM = pow(2,31) - 1
    i = 1

    while i <= list_num:
        ret = random.randint(MIN_NUM,MAX_NUM)
        #print i,ret
        lst.append(ret)
        i += 1
    lst.sort()
    print lst
    print random.choice(lst)

if __name__ == "__main__":
    #makeTextFile()
    #readTextFile()
    #readTextFile2()
    #displayNumType(10L)
    #getScore(86.4)
    #isLeapYear(1900)
    randTest()