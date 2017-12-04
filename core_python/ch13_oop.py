#!/usr/bin/env python
# -*- coding: utf-8


from random import choice
from time import time, ctime, sleep


class AddrBookEntry(object):
    """Address book document"""
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'AddrBookEntry __init__:', self.name

    def update_phone(self, new_ph):
        print 'AddrBookEntry update_phone:', self.name
        self.phone = new_ph


class EmplAddrBookEntry(AddrBookEntry):
    """employee address book class"""
    myVersion = 'v1.1'

    def __init__(self, nm, ph, id_, em):
        # call parent's __init__ first
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id_
        self.email = em
        print 'EmplAddrBookEntry __init__:', nm

    def update_email(self, newem):
        print 'EmplAddrBookEntry update_email', newem
        self.email = newem


def test_addr_book_entry():
    nie = AddrBookEntry('nie', '123-111')
    dao = EmplAddrBookEntry('dao', '123-112', 'id001', '001@gmail.com')
    print nie.name, nie.phone
    print dao.name, dao.phone, dao.empid, dao.email

    dao.update_phone('123-113')
    dao.update_email('002@gmail.com')
    print dao.name, dao.phone, dao.empid, dao.email

    # to access class attribute
    print EmplAddrBookEntry.myVersion
    print dir(EmplAddrBookEntry)
    print dir(AddrBookEntry)

    print EmplAddrBookEntry.__dict__
    print EmplAddrBookEntry.__name__, EmplAddrBookEntry.__class__, EmplAddrBookEntry.__bases__
    # it must call with instance, not with class
    # EmplAddrBookEntry.update_email("003@gmail.com")
    print dao.__class__


class HotelRoomCalc(object):
    """hotel room calculator"""
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calc_total(self, days=1):
        daily = round((self.roomRate*(1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily


class RoundFloat(float):
    """ 具有四舍五入功能的float类型 """
    def __new__(cls, val):
        # 类方法,在object申明为staticmethod
        # return float.__new__(cls, round(val, 2))
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

    def __init__(self, val):
        print 'init, val=', val
        super(RoundFloat, self).__init__(val)


class SortedKeyDict(dict):
    """实现按key排序的字典类型"""
    def keys(self):
        print 'call keys()'
        return sorted(super(SortedKeyDict, self).keys())

    def __iter__(self):
        print 'call __iter__()'
        return super(SortedKeyDict, self).__iter__()


def test_sorted_key_dict():
    d = SortedKeyDict((('zheng-cai', 67), ('hui-jun', 68), ('xin-yi', 2)))

    print 'by iterator:'.ljust(12), [key for key in d]
    print 'by keys():'.ljust(12), d.keys()


class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), 'value must be a float'
        self.value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.value

    __repr__ = __str__


class Time60(object):
    """ 定制Time60类,跟踪时间 """

    UNIT = 60

    def __init__(self, *time):
        self.hr = self.min = -1

        for each in time:
            if isinstance(each, str):
                hr1, min1 = each.split(':')
                self.hr = int(hr1.strip())
                self.min = int(min1.strip())
            elif isinstance(each, (list, tuple)):
                self.hr = int(each[0])
                self.min = int(each[1])
            elif isinstance(each, int):
                if self.hr == -1:
                    self.hr = each
                else:
                    self.min = each
            else:
                print 'input err:', each, type(each)
        if self.hr == -1 or self.min == -1:
            print 'input hr/min err:', self.hr, self.min
            return

        self.turing_time()

    def __str__(self):
        return '%02d:%02d' % (self.hr, self.min)

    __repr__ = __str__

    def __add__(self, other):
        """ overloading + op """
        return self.__class__(self.hr + other.hr,
                              self.min + other.min)

    def __iadd__(self, other):
        """ overloading += op(in-place op) """
        self.hr += other.hr
        self.min += other.min
        self.turing_time()
        return self

    def __sub__(self, other):
        minuend = self.min + self.hr * self.__class__.UNIT
        subtrahend = other.min + other.hr * self.__class__.UNIT

        if minuend < subtrahend:
            print 'error, minuend less than subtrahend'
            return None

        return self.__class__(0, minuend - subtrahend)

    def turing_time(self):
        # print 'turing_time', self.hr, self.min
        while self.min >= self.__class__.UNIT:
            self.min -= self.__class__.UNIT
            self.hr += 1


def test_time60():
    a = Time60(10, 45)
    b = Time60(6, 25)
    c = Time60(1, 50)
    d = Time60('12:05')
    e = Time60([12, 05])
    f = Time60((12, 05))

    print a, b, c, d, e, f
    print a + b
    a += b
    print a

    print b - c


class RandSeq(object):
    def __init__(self, seq):
        self.data = seq

    def __iter__(self):
        print 'in __iter__'
        return self

    def next(self):
        print 'in next'
        try:
            return choice(self.data)
        except StopIteration, e:
            print 'exception:', e


def test_rand_seq():
    for item in RandSeq(('rock', 'paper', 'scissors')):
        print item


class AnyIter(object):
    def __init__(self, data, safe=False):
        self.safe = safe
        self.iter = iter(data)

    def __iter__(self):
        return self

    def next(self, how_many=1):
        ret = []
        for item in range(how_many):
            try:
                ret.append(self.iter.next())
            except StopIteration, e:
                if self.safe:
                    break
                else:
                    raise e
        return ret


def test_any_iter():
    a = AnyIter(range(10), True)

    for j in range(1, 6):
        print j, ':', a.next(j)


class NumStr(object):
    def __init__(self, num=0, string=''):
        """把__num/__string定义定义为私有成员，子类和外部不可见"""
        self.__num = num
        self.__string = string

    def __str__(self):
        return '%d :: %r' % (self.__num, self.__string)

    __repr = __str__

    def __add__(self, other):  # for s+o
        if isinstance(other, NumStr):
            return self.__class__(
                self.__num + other.__num,
                self.__string + other.__string
            )
        else:
            raise(TypeError, 'Illegal argument type for + op')

    def __mul__(self, num):  # for o*n
        if isinstance(num, int):
            return self.__class__(self.__num * num, self.__string * num)
        else:
            raise (TypeError, 'Illegal argument type for * op')

    def __nonzero__(self):
        return self.__num or len(self.__string)

    def __cmp__(self, other):
        num_cmp = cmp(self.__num, other.__num)
        str_cmp = cmp(self.__string, other.__string)

        if num_cmp < 0 and str_cmp < 0:
            return -1
        elif num_cmp > 0 and str_cmp > 0:
            return 1
        else:
            return 0


def test_num_str():
    a = NumStr(3, 'foo')
    print a

    # 访问NumStr类的私有成员
    # print a._NumStr__num, a._NumStr__string


class WrapMe(object):
    def __init__(self, obj):
        self.__data = obj  # 保存原始对象的副本

    # 获得原始对象
    def get(self):
        return self.__data

    def __repr__(self):
        print 'in __repr__'
        return repr(self.__data)

    def __str__(self):
        print 'in __str__'
        return str(self.__data)

    def __getattr__(self, attr):
        print 'in __getattr__,', attr
        return getattr(self.__data, attr)


def test_wrap_me():
    wc = WrapMe(3.5+4.2j)
    print repr(wc)
    print repr(wc.real)
    print repr(wc.imag)
    print repr(wc.conjugate())

    wl = WrapMe([123, 'foo', 45.67])
    wl.append('bar')
    wl.append(123)
    print repr(wl)
    print wl.index(45.67)
    print wl.count(123)
    print wl.get()[3]


class TimedWrapMe(object):
    def __init__(self, obj):
        self.__data = obj  # 保存原始对象的副本
        self.__ctime = self.__mtime = self.__atime = time()

    # 获得原始对象
    def get(self):
        print 'in get()'
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or t_type[0] not in 'cma':
            raise(TypeError, 't_type must be "c" or "m", "a"')
        return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))

    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def __repr__(self):
        self.__atime = time()
        return repr(self.__data)

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)


def test_timed_wrap_me():
    twm = TimedWrapMe(932)
    print repr(twm.gettimestr('c'))
    print repr(twm.gettimestr('m'))
    print repr(twm.gettimestr('a'))

    sleep(2)
    print repr(twm)

    print repr(twm.gettimestr('c'))
    print repr(twm.gettimestr('m'))
    print repr(twm.gettimestr('a'))


class CapOpen(object):
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def __str__(self):
        return str(self.file)

    def __repr(self):
        return repr(self.file)

    def write(self, data):
        self.file.write(data.upper())

    def __getattr__(self, attr):
        return getattr(self.file, attr)


def test_cap_open():
    filename = '/tmp/xxx'
    fw = CapOpen(filename, 'w')
    fw.write('delegation example\n')
    fw.write('faye is good\n')
    fw.write('at delegating\n')
    fw.close()

    for each_line in open(filename, 'r'):
        print each_line,


if __name__ == '__main__':
    # test_addr_book_entry()

    # print RoundFloat(1.5955)

    # test_sorted_key_dict()

    # print RoundFloatManual(3.1415), RoundFloatManual(2.556)

    # test_time60()

    # test_rand_seq()

    # test_any_iter()

    # test_num_str()

    # test_wrap_me()

    # test_timed_wrap_me()

    test_cap_open()
