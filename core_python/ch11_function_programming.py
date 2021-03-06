#!/usr/bin/env python
from operator import add, sub
from random import randint, choice
from time import sleep, ctime

MAX_TRIES = 2


def easy_math():
    """pass list parameter to function"""
    ops = {'+': add, '-': sub}

    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d%s%d=' % (nums[0], op, nums[1])

    i = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print 'correct'
                break
            if i == MAX_TRIES:
                print 'answer is:\n%s%d\n' % (pr, ans)
            else:
                print 'incorrect...try again'
                i += 1
        except (KeyboardInterrupt, EOFError, ValueError), e:
            print 'invalid input, try again:', e


def tsfunc(func):
    print 'tsfunc is called'
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
    print 'tsfunc_arg1 is called'
    def wrappedFunc(func):
        print 'wrappedFunc is called'
        def _func():
            print '[%s] %s() called,%s' % (
            ctime(), func.__name__,name)
            func()
        return _func
    return wrappedFunc

@tsfunc_arg1('arg1')
def foo_arg1():
    ''' foo_arg1=tsfunc_arg1(name)(foo_arg1)() '''
    print 'in foo_arg1'

def demo_decorator_arg1():
    for i in range(2):
        sleep(1)
        foo_arg1()



####################################
def tsfunc_arg2(name):
    print 'tsfunc_arg2 is called'
    def wrappedFunc(func):
        print 'wrappedFunc is called'
        def _func(i):
            print '[%s] %s() called,%s' % (
          ctime(), func.__name__,name)
            func(i)
        return _func
    return wrappedFunc

@tsfunc_arg2('arg2')
def foo_arg2(i=0):
    ''' foo_arg2=(tsfunc_arg2(name))(foo_arg2)(i) '''
    print 'in foo_arg2, i=%d' % i

def demo_decorator_arg2():
    for i in range(2):
        sleep(1)
        foo_arg2(i)
####################################

if __name__ == '__main__':
    easy_math()
    #demo_decorator()
    # demo_decorator_arg1()
    #demo_decorator_arg2()
