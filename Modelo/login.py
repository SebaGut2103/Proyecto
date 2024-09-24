from Modelo.contrasena import encryptContra, insertarContra,guardarContra, cargarContra
archivo = 'datos\usuarios.json'


def sesion(): 
    usuario = input('Ingresa nombre de usuario:\n')
    guardarContra = cargarContra(usuario)
    if guardarContra is None:
        print('>>>Usuario no encontrado')
        return
     
    while True:
        
        contra = input('Ingresa contraseña:\n')
        if encryptContra(contra) == guardarContra:

            print('>>>Ingresando con exito')
            break
        else:
            print('>>>Contraseña incorrecta')
        return contra
sesion()