from Modelo.contrasena import encryptContra
import json
import os

archivo = 'datos\usuarios.json'

def guardarContra(contra):

    with open('datos\usuarios.json' ,'w') as fd:
        json.dump(encryptContra,fd)
    if not fd.closed():
        fd.close

def cargarContra():
    #Carga las contraseñas encriptadas
    if os.path.exists(archivo):
        with open('datos\usuarios.json', 'r') as fd:
            return json.load(fd)

    return None
