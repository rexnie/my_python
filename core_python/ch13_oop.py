#!/usr/bin/env python
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


if __name__ == "__main__":
    TestAddrBookEntry()
