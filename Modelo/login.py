from contrasena import encryptContra
from Persistencia.Contrasenas import guardarContra,cargarContra, none


def iniciarSesion(): 
    archivo = 'usuario.json'
    contra = cargarContra(archivo)
    if contra is none:
        contra = {
           
           'usuario': input('Ingresa nombre de usuario:\n'),
           'contrasena': encryptContra = ('SISGESA')
        }

        guardarContra(archivo,contra)
    else:
        usuario = input('Ingresa nombre de usuario:\n')
        contrasena = input('Ingresa contraseña:\n')
    if (contra["usuario"] == usuario and
        contra["contrasena"] == encryptContra(contrasena)):
        print('>>>Ingreso exitoso')
    else:
        print('>>>Contraseña incorrecta')
iniciarSesion()