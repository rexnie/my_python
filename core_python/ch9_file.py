#!/usr/bin/env python
import os

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
        print "cwd=",cwd
        
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


if __name__ == "__main__":
    osPath()
