#!/usr/bin/env python
# -*- coding: utf-8
import os

class AddrBookEntry(object):
    """Address book document"""
    def __init__(self, nm, ph):
        self.name = nm
        self.phone = ph
        print 'AddrBookEntry __init__:', self.name

    def updatePhone(self, newph):
        print 'AddrBookEntry updatePhone:', self.name
        self.phone = newph

class EmplAddrBookEntry(AddrBookEntry):
    """employee address book class"""
    myVersion = 'v1.1'

    def __init__(self, nm, ph, id, em):
        #call parent's __init__ first
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = id
        self.email = em
        print 'EmplAddrBookEntry __init__:', nm

    def updateEmail(self, newem):
        print 'EmplAddrBookEntry updateEmail', newem
        self.email = newem

def TestAddrBookEntry():
    nie = AddrBookEntry("nie", "123-111")
    dao = EmplAddrBookEntry("dao", "123-112", 'id001', '001@gmail.com')
    print nie.name, nie.phone
    print dao.name, dao.phone, dao.empid, dao.email

    dao.updatePhone('123-113')
    dao.updateEmail('002@gmail.com')
    print dao.name, dao.phone, dao.empid, dao.email

    # to access class atrribute
    print EmplAddrBookEntry.myVersion
    print dir(EmplAddrBookEntry)
    print dir(AddrBookEntry)

    print EmplAddrBookEntry.__dict__
    print EmplAddrBookEntry.__name__, EmplAddrBookEntry.__class__, EmplAddrBookEntry.__bases__
    #it must call with instance, not with class
    #EmplAddrBookEntry.updateEmail("003@gmail.com")
    print dao.__class__

class HotelRoomCalc(object):
    """hotel room calculator"""
    def __init__(self, rt, sales=0.085, rm=0.1):
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        daily = round((self.roomRate*(1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

class RoundFloat(float):
    """具有四舍五入功能的float类型"""
    def __new__(cls, val): # 类方法,在object申明为staticmethod
        print type(cls)
        #return float.__new__(cls, round(val, 2))
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

    def __init__(self, val):
        print 'init, val=', val

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


if __name__ == "__main__":
    #TestAddrBookEntry()

    #print RoundFloat(1.5955)
    test_sorted_key_dict()