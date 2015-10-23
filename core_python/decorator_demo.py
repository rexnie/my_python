# -*- coding: utf-8
###################################################################
def decoTS(func):
    def wrapF():
        print 'in wrapF, before func() called'
        ret=func()
        print 'in wrapF, after func() called'
        return ret
    return wrapF

@decoTS
def foo():
    '''无参数的装饰器对无参数函数的装饰
    内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
    <==> foo=decoTS(foo)
    '''
    print 'foo() is called'
    return 'foo'

def test_foo():
    for i in range(2):
        print foo()
###################################################################
def decoTSAdd(func):
    def wrapF(a,b):
        print 'in wrapF, before func(%d,%d) called' % (a,b)
        ret=func(a,b)
        print 'in wrapF, after func() called,ret=%d' % (ret)
        return ret
    return wrapF

@decoTSAdd
def foo_add(a,b):
    '''无参数的装饰器对带2个参数的函数的装饰
    内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
    <==> foo_add=decoTSAdd(foo_add)(a,b)
    '''
    print 'foo_add(%d,%d) is called' %(a,b)
    return a+b

def test_foo_add():
    for i in range(2):
        print foo_add(i,i+1)
###################################################################
def decoTSVariableLenPara(func):
    def wrapF(*args,**kwargs):
        print 'in wrapF, before func(args,kwargs) called: ',args,kwargs
        ret=func(*args,**kwargs)
        print 'in wrapF, after func() called,ret=%d' % (ret)
        return ret
    return wrapF

@decoTSVariableLenPara
def foo_add2(a,b):
    '''无参数的装饰器对带2个参数的函数的装饰
    内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
    <==> foo_add2=decoTSVariableLenPara(foo_add2)(a,b)
    '''
    print 'foo_add2(%d,%d) is called' %(a,b)
    return a+b

@decoTSVariableLenPara
def foo_add3(a,b,c):
    '''无参数的装饰器对带可变长的参数的函数的装饰
    内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
    <==> foo_add3=decoTSVariableLenPara(foo_add3)(a,b,c)
    '''
    print 'foo_add3(%d,%d,%d) is called' %(a,b,c)
    return a+b+c

@decoTSVariableLenPara
def foo_add_var_len_para(*args,**kwargs):
    '''无参数的装饰器对带可变长的参数的函数的装饰
    '''
    print 'foo_add_var_len_para called'
    return sum(args)

def test_foo_var_len_para():
    for i in range(2):
        print foo_add2(i,i+1)
        print foo_add3(i, i+1, i+2)
        print foo_add_var_len_para(*(i,i+1))
        print foo_add_var_len_para(*(i,i+1,i+2))

###################################################################
def decoTSDecoPara(decoPara):
    def wrapF(func):
        print 'in wrapF..,decoPara=%s' % decoPara
        def wrapF_():
            print 'in wrapF_, before func() called'
            ret=func()
            print 'in wrapF, after func() called,ret=%s' % ret
            return ret
        return wrapF_
    return wrapF

@decoTSDecoPara('module1')
def foo_deco_para():
    '''带参数的装饰器对无参数函数的装饰
    <==> decoTSDecoPara(decoPara)(foo_deco_para)()
    decoTSDecoPara(decoPara) 返回的是一个函数，参数是foo_deco_para
    decoTSDecoPara(decoPara)(foo_deco_para) 返回的是一个函数，不带参数
    decoTSDecoPara(decoPara)(foo_deco_para)() 返回foo_deco_para(),不带参数
    '''
    print 'foo_deco_para() is called'
    return 'foo_deco_para'

def test_foo_deco_para():
    for i in range(2):
        print foo_deco_para()
###################################################################
class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("  locker.release() called.（不需要对象实例）")

def decoTSDecoParaClass(cls):
    def wrapF(func):
        print 'in wrapF..,func=%s,cls=%s' % (func.__name__,cls)
        def wrapF_():
            print 'in wrapF_, before func() called'
            cls.acquire()
            try:
                ret=func()
                return ret
            finally:
                cls.release()
                print 'in wrapF, after func() called,ret=%s' % ret
        return wrapF_
    return wrapF

@decoTSDecoParaClass(locker)
def foo_deco_para_class():
    '''带一个类作为参数的装饰器对无参数函数的装饰
    '''
    print 'foo_deco_para() is called'
    return 'foo_deco_para'

def test_foo_deco_para_class():
    for i in range(2):
        print foo_deco_para_class()
###################################################################


if __name__== '__main__':
    #test_foo()
    #test_foo_add()
    #test_foo_var_len_para()
    #test_foo_deco_para()
    test_foo_deco_para_class()
