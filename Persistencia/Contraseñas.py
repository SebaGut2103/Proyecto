import hashlib
import json
import os
contra_archivo = 'UTIS\contra_archivo.json'

#Este es archivo donde se almacena la contraseña

def encryptContra (contra):
    #Esta linea encripta la contraseña usando SHA256.
    return hashlib.sha256(contra.encode()).hexdigest()

def guardarContra(contra):

    with open('UTIS\contra_archivo.json' ,'w') as fd:
        json.dump(encryptContra,fd)
    if not fd.closed():
        fd.close

def cargarContra():
    #Carga las contraseñas encriptadas
    if os.path.exists(contra_archivo):
        with open('UTIS\contra_archivo.json', 'r') as fd:
            return json.load(fd)

    return None
    
def cambiarContra():
    
    nuevo_contra = input ('Ingrese una nueva contraseña:\n')
    encryptContra = encryptContra(nuevo_contra)
    guardarContra (encryptContra)
    print('Cambio de contraseña exitosa.')
