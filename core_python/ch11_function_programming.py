#!/usr/bin/env python
from operator import add, sub
from random import randint, choice
from time import sleep, ctime

def easy_math():
    '''pass list parameter to function'''
    ops = { '+':add, '-':sub }
    MAXTRIES = 2
    op = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    ans=ops[op](*nums)
    pr='%d%s%d=' % (nums[0],op,nums[1])

    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if i == MAXTRIES:
                print 'answer is:\n%s %d\n' % pr,ans
            else:
                print 'incorrect...try again'
                i += 1
        except (KeyboardInterrupt,EOFError,ValueError), e:
            print 'invalid input, try again'

################################
def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (
          ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    ''' foo=tsfunc(foo) '''
    print 'in foo()'

def demo_decorator():
    for i in range(5):
        sleep(1)
        foo()


#################################
def tsfunc_arg1(name):
    def wrappedFunc(func):
        print '[%s] %s() called,%s' % (
          ctime(), func.__name__,name)
        return func
    return wrappedFunc

#@tsfunc_arg1('arg1')
def foo_arg1():
    ''' foo_arg1=tsfunc_arg1(name)(foo_arg1)() '''
    print 'in foo_arg1'

def demo_decorator_arg1():
    for i in range(5):
        sleep(1)
        #foo_arg1()



####################################
def tsfunc_arg2(name):
    def wrappedFunc(func):
        print '[%s] %s() called,%s' % (
          ctime(), func.__name__,name)
        return func
    return wrappedFunc

#@tsfunc_arg2('arg2')
def foo_arg2(i=0):
    ''' foo_arg2=(tsfunc_arg2(name))(foo_arg2)(i) '''
    print 'in foo_arg2, i=%d' % i

def demo_decorator_arg2():
    for i in range(3):
        sleep(1)
        foo_arg2(i)
####################################

if __name__ == '__main__':
    #easy_math()
    #demo_decorator()
    #demo_decorator_arg1()
    #demo_decorator_arg2()
