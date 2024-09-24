from Modelo.contrasena import encryptContra, insertarContra,guardarContra, cargarContra

contra = {}
archivo = 'usuario.json'
contra = cargarContra(archivo)

def sesion(): 
    usuario = input('Ingresa nombre de usuario:\n')    
    while True:
        
        contra = input('Ingresa contraseña:\n')
        if encryptContra(contra) == contra(archivo):

            print('>>>Ingresando con exito')
            break
        else:
            print('>>>Contraseña incorrecta')
        return contra
sesion()