from Persistencia.Contraseñas import guardarContra
import hashlib

def encryptContra(contra):
    #Esta linea encripta la contraseña usando SHA256.
    return hashlib.sha256(contra.encode()).hexdigest()

def cambiarContra():
    
    nuevo_contra = input ('Ingrese una nueva contraseña:\n')
    encryptContra = encryptContra(nuevo_contra)
    guardarContra(encryptContra)
    print('Cambio de contraseña exitosa.')


def insertarContra():
    contra = input('Ingresa Contraseña: ')
    if encryptContra(contra):
        print('>>>Contraseña guardada correctamente')    
    guardarContra(contra)