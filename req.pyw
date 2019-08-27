import requests
from requests.exceptions import HTTPError

print("Hola")
base_url = "https://ed2ku4egij.execute-api.us-west-1.amazonaws.com/Prod/"
res = requests.get(base_url)
print(res.text)

name = 'Hestia'
endpoint = '{0}evento/{1}'.format(base_url,name)
print(endpoint)
contenido = {
    'MessageName':'Hestia',
    'Message':'Diosa del hogar, del correcto orden de lo doméstico y de la familia',
    'Time':'Hoy',
    'Window':'Test',
    'WindowName':'Vesta',
    'ASCII':'no',
    'Key':'up',
    'KeyID':'1',
    'ScanCode':'0',
    'Extended':'0',
    'Injected':'0',
    'Alt':'0',
    'Transition':'0'
}
print(contenido)

try:
    res = requests.put(endpoint,json=contenido)
    res.raise_for_status()
except HTTPError as http_err:
    print(f'Error HTTP: {http_err}')
except Exception as err:
    print(f'Error: {err}')
else:
    print('Correcto')

'''
if res:
    print("Correcto")
    print('Borrar el registro de la pila')
else:
    print("Error")
    print('No se borra el registro de la pila')
    print(res.status_code)
'''