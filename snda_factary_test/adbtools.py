#!/usr/bin/env python
from commandwrapper import WrapCommand
import os
import time

# absolute path of adb bin
ADB = "/bin/adb"

def connect_and_check():
    '''check adb devices connect or not'''
    adb = WrapCommand('%s devices' % ADB,shell=True)
    adb.start()
   
    i = 3
    while i > 0 and adb.is_alive():
        i -= 1
        time.sleep(0.5)
    if adb.is_alive():
        adb.stop()
   
    adb.join()
    #print adb.results
    for line in adb.results[0].split('\n'):
        if line.endswith("device"):
            return True 
    return False

def adb_kill_server():
    ''' adb kill-server'''
    cmd=WrapCommand('%s kill-server' % ADB,shell=True)
    cmd.start()
    cmd.join()

def connect_devices():
    '''check adb devices connect or not,with retry action'''
    if not connect_and_check():
        adb_kill_server()
        time.sleep(0.5)
        return connect_and_check() 
    return True 

if __name__ == '__main__':
    print connect_devices()
