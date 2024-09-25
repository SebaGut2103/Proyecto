from Persistencia.Contrasenas import guardarContra, encryptContra

def cambiarContra(archivo):
    
    nuevo_contra = input ('Ingrese una nueva contraseña:\n')
    encryptContra = encryptContra(nuevo_contra)
    if guardarContra(encryptContra(archivo)):
        print('Cambio de contraseña exitosa.')


def insertarContra():
    contra = input('Ingresa Contraseña: ')
    if encryptContra(contra):
        print('>>>Contraseña guardada correctamente')    
    guardarContra(contra)  