from Persistencia.Guardar import cargar
from Persistencia.Contraseñas import encryptContra

archivoCon = 'datos\contra_archivo.json'


def sesion(): 
    usuario = input('Ingrese su nombre de usuario:\n ')
    while True:
        contra= input('Ingrese contraseña:\n')
        mostrar = encryptContra(contra)
        print (mostrar)
        guardarContra(contra)
sesion()
        # try:    
        #     if contra == 
        #     :
        #         print('Abrir sesión>>>')
        #         usuarioSesion = True
        #     else:
        #         print('>>>Contraseña inconrrecta')
        #         print('Intente nuevamente.')
        # except Exception as e:
        #     print('>>>Contraseña inconrrecta')
        #     print('Intente nuevamente.')
        # return contra            