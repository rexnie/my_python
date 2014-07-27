#!/usr/bin/env python
import os
import sys

def osPath():
    for tmpdir in ("/tmp",r"c:\temp"):
        if os.path.isdir(tmpdir):
            break
    else:
        tmpdir = os.getcwd() #use cwd

    print "tmpdir=",tmpdir

    if tmpdir:
        os.chdir(tmpdir)
        cwd = os.getcwd()
        print "cwd=",cwd

        os.mkdir("test")
        os.chdir("test")
        cwd = os.getcwd()
        print "cwd=",cwdlessCmd

        print os.listdir(cwd)

        fobj = open("f1.txt","w")
        fobj.write('aaaa\n')
        fobj.write('bbbb\n')
        fobj.close()
        print os.listdir(cwd)

        os.rename("f1.txt", "fnew.txt")

        fullpath = os.path.join(cwd,os.listdir(cwd)[0])
        print "fullpath=",fullpath

        print os.path.split(fullpath)
        print os.path.splitext(os.path.basename(fullpath))

        for eachLine in open(fullpath):
            print eachLine,

        os.remove(fullpath)
        os.chdir(os.pardir)
        os.rmdir("test")

def catFileWithoutComment():
    """cat file without #"""
    for eachLine in open("ch8_if_loop.py"):
        (string_pre_str,str,string_after_str) = eachLine.partition("#")
        if string_pre_str == eachLine: # the line without '#'
            print eachLine,
        else:   # the line has '#'
            print string_pre_str

def lessCmd(fn):
    if not os.path.isfile(fn):
        print "not a file:",fn
    fobj = open(fn,"r",0)
    fobj.seek(0)
    fLines = 0
    try:
        while True:
            print fobj.tell()
            fLines += 1
    except StopIteration,si:
        print fLines

if __name__ == "__main__":
    #osPath()
    #catFileWithoutComment()
    lessCmd(sys.argv[1])
