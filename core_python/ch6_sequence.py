#!/usr/bin/env python

import os
import string
import keyword
from random import choice

def idcheck():
    """Identifier checker """

    alphas = string.letters + "_"
    num_alphas = string.digits + alphas
    vid = True

    myIpt = raw_input("Identifier to test:")
    if len(myIpt) >= 1:
        if myIpt in keyword.kwlist:
            print "invalid ID,it is keyword"
            vid = False
        if vid == True:
            if myIpt[0] not in alphas:
                print "invalid ID,should begin with a-z/A-Z/_"
                vid = False
            else:
                for otherch in myIpt[1:]:
                    if otherch not in num_alphas:
                        print "invalid ID,should in a-z/A-Z/_/0-9"
                        vid = False
                        break
    else:
        print "invalid ID,length < 1"
        vid = False

    if vid == True:
        print "'%s' is a valid ID" % myIpt
    else:
        print "'%s' is an invalid ID" % myIpt

def huiWen():
    s = raw_input("Input str:")
    for t in reversed(s):
        s += t
    print s

def huiWen2():
    s = raw_input("Input str:")
    s += s[::-1]
    print s

def printFrontBack():
    "Print a Front and a Back char a time"
    s = raw_input("Input str:")
    length = len(s)
    l = length / 2 - 1
    i = 0
    while(i <= l ):
        print s[i],s[-i-1]
        i += 1
    if length % 2 != 0:
        print s[i]

def uniFile():
    CODEC = "utf-16"
    fn = "nie.txt"
    str_out = u"Hello World\n"
    bytes_out = str_out.encode(CODEC)
    print len(str_out),len(bytes_out)
    f = open(fn,"w")
    f.write(bytes_out)    
    f.close()

    f = open(fn,"r")
    bytes_in = f.read()
    f.close()

    str_in = bytes_in.decode(CODEC)
    print len(bytes_in),len(str_in)

"""Stack """
stack = []
def pushit():
    item = raw_input("Input item:")
    if item != None:
        stack.append(item)

def popit():
    if len(stack) == 0:
        print "stack is empty"
    else:
        print stack.pop(-1)

def viewStack():
    print stack

def stackUseList():
    Menu = """
    p(U)ush
    p(O)op
    (V)iew
    (Q)uit
    enter your choice:"""
    CMDs ={'u' : pushit,'o' : popit,'v' : viewStack}
    while True:
        while True:
            try:
                ch = raw_input(Menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError),reason:
                print "input error",reason
                ch = 'q'
            if ch not in 'uovq':
                print "input error,must be in uovq"
            else:
                break

        if ch == 'q':
            break
        CMDs[ch]()
""" END of Stack"""                      

"""Queue"""
queue = []
def enQ():
    item = raw_input("Input item:")
    if item != None:
        queue.append(item)

def deQ():
    if len(queue) == 0:
        print "queue is enpty"
    else:
        print queue.pop(0)

def viewQ():
    print queue

def queueUseList():
    Menu = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit
    enter your choice:"""
    CMDs ={'e' : enQ,'d' : deQ,'v' : viewQ}
    while True:
        while True:
            try:
                ch = raw_input(Menu).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError),reason:
                print "input error",reason
                ch = 'q'
            if ch not in 'edvq':
                print "input error,must be in edvq"
            else:
                break

        if ch == 'q':
            break
        CMDs[ch]()
"""END of Queue"""

def stoneScissorCloth():
    winRule = ['stone','scissors','cloth','stone']
    computer = choice(winRule[0:3])
    people = raw_input("Input u select:stone, scissors, cloth").strip()
    print 'Computer:%s' % computer
    if computer == people:
        print "No-win"
    elif winRule[winRule.index(people) + 1] == computer:
        print "U win"
    else:
        print "Computer Win"

def columnDisplay():
    for i,j in enumerate(range(100)):
        if (i + 1) % 3 == 0:
            print j
        else:
            print j,

if __name__ == "__main__":
    #idcheck()
    #huiWen()
    #huiWen2()
    #printFrontBack()
    #uniFile()
    #stackUseList()
    #queueUseList()
    #columnDisplay()
    stoneScissorCloth()