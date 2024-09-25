import hashlib
import json
import os

def encryptContra(contra):
    return hashlib.sha256(contra.encode()).hexdigest

def cargarContra():
    if not os.path.exists('datos\\usuario.json'):
        guardarContra('SISGESA')
        return 'SISGESA'
    
    with open('datos\usuario.json', 'r') as fd:
        dato = json.load(fd)
        return dato['contraseña']
    
def guardarContra(contra):
    with open('datos\\usuario.json', 'w') as fd:
        json.dump({'contraseña': encryptContra(contra)}, fd)
        
