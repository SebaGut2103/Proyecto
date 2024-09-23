from Interfaz.Menu import menu
from Persistencia.Guardar import cargar

def sesion(): 
    usuario = input('Ingrese su nombre de usuario:\n ')
    while True:
        contra= input('Ingrese contraseña:\n')
    
        try:    
            if contra == 
            :
                print('Abrir sesión>>>')
                usuarioSesion = True
            else:
                print('>>>Contraseña inconrrecta')
                print('Intente nuevamente.')
        except Exception as e:
            print('>>>Contraseña inconrrecta')
            print('Intente nuevamente.')
        return contra            