#!/usr/bin/env python
from ConfigParser import SafeConfigParser 
import threading

class MesSubConfig(object):
    def __init__(self, cfg, sec):
        self.__dict__['config'] = cfg #config attribute must be in __dict__
        self.__dict__['section'] = sec

    def __getattr__(self, option):
        '''for getting attribute that not in __dict__'''
        cfg = self.config
        if not cfg.has_option(self.section, option):
            print 'section no option:', self.section, option
        return cfg.get(self.section, option)

    def __setattr__(self, opt, val):
        cfg = self.config    
        sec = self.section
        if not cfg.has_section(sec):
            print 'no section:', sec
            cfg.add_section(sec)
        cfg.set(sec, opt, val)

class MesConfig(object):
    inst = None
    lock = threading.Lock()

    def __init__():#@no self
        '''disable __init__ methold,and this config is not thread safely'''
    @staticmethod
    def get_instance():
        MesConfig.lock.acquire()
        if not MesConfig.inst:
            MesConfig.inst = object.__new__(MesConfig)
            object.__init__(MesConfig.inst)
            MesConfig.inst.init()
        MesConfig.lock.release()
        return MesConfig.inst
    
    def init(self):
        cfg = SafeConfigParser()
        cfg.readfp(open('config.ini'))
        self.__dict__['cfg'] = cfg
        self.__dict__['sec_map'] = {}

    def __getattr__(self, sec):
        cfg = self.__dict__['cfg']
        sec_map = self.__dict__['sec_map']
        if not sec_map.has_key(sec):
            print 'add section:', sec
            sec_map[sec] = MesSubConfig(cfg, sec)
        return sec_map[sec]

    def save_to_file(self):
        cfg = self.__dict__['cfg']
        cfg.write(open('config.bak.ini','w'))

    def dump_config(self):
        cfg = self.__dict__['cfg']
        sec = cfg.sections()
        length = len(sec)
        i = 0
        while i < length:
            print 'section:', sec[i]
            print '==========================='
            print cfg.options(sec[i])
            print
            i += 1

if __name__ == '__main__':
    mcfg = MesConfig.get_instance()
    mcfg.main.nie = "1"
    print mcfg.backend.debug
    mcfg.dump_config()
    mcfg.save_to_file()
