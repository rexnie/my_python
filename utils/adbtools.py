#!/usr/bin/env python
from commandwrapper import WrapCommand
import os
import time

# absolute path of adb bin
if os.name == 'posix':
    ADB = "/bin/adb"
else:
    ADB='adb\\adb.exe'

def connect_and_check():
    '''check adb devices connect or not'''
    adb = WrapCommand('%s devices' % ADB,shell=True)
    adb.start()
    i = 5
    while i > 0 and adb.is_alive():
        i -= 1
        time.sleep(1)
    if adb.is_alive():
        adb.stop()
   
    print 'adb111'
    adb.join()
    print adb.results
    for line in adb.results[0].split(os.linesep):
        if line.endswith("device") or line.endswith("recovery"):
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
        print 'adb112'
        #time.sleep(1)
        return connect_and_check() 
    return True 

def execute_adb_cmd(cmd='adb devices'):
    ''' execute adb command
        return a tuple (stdoutdata, stderrdata)
    '''
    idx=cmd.find('adb')
    if idx == -1:
       print 'must contain adb in cmd'
       return False,False
    cmd=cmd[idx+3 :]
    print ADB,cmd
    cmd2=WrapCommand('%s %s' % (ADB,cmd))
    cmd2.start()
    cmd2.join()
    return cmd2.results

if __name__ == '__main__':
    print connect_devices()
    #print execute_adb_cmd(' adb pull /sdcard/t.wa .')
