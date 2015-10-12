#-------------------------------------------------------------------------------
# Name:        
# Purpose: produce double click when press 1, press other key to stop
#
# Author:
#
# Created:     02/10/2012
# Copyright:   (c) Administrator 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import win32gui, win32api, win32con
import time
import threading
import pythoncom
import pyHook

flag = '1'

def click_event():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 )

def double_click_event():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0 )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0 )
    
def get_flag(event):
    global flag
    flag = event.GetKey()

def start_hook():
    hm = pyHook.HookManager()
    hm.KeyDown = get_flag
    hm.HookKeyboard()
    pythoncom.PumpMessages()

def start_mouse():
    interval = 1
    while True:
        time.sleep(interval)
        if '1' == flag:
            double_click_event()
        
def main():
    t1 = threading.Thread(target = start_hook)
    t1.start()

    t2 = threading.Thread(target = start_mouse)
    t2.start()

if __name__ == '__main__':
    main()
