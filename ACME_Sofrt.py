from Modelo.contrasena import encryptContra

archivo = 'datos\contra_archivo.json'


def sesion(): 
    usuario = input('Ingrese su nombre de usuario:\n ')
    while True:
        contra= input('Ingrese contraseña:\n')
        mostrar = encryptContra(contra)
        print (mostrar)    
sesion()