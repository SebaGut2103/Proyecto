from bodymodel.Registros import modulo, registrarEstudiante, registroDocentes,consultaDocentes, consultaModulos, consultarEstudiantes

from bodymodel.login import iniciarSesion
from Interfaz.Menu import menu
def main():
    while True:
            menu()
            print('>>> BIENVENIDO A ACEM.SOFT <<<')
            opcion = input('*Seleccione una opción: ')

            if opcion == 'a':
                modulo()
            elif opcion == 'b':
                registrarEstudiante()
            elif opcion == 'c':
                registroDocentes()
            elif opcion == 'd':
                consultarEstudiantes()
            elif opcion == 'e':
                consultaModulos()
            elif opcion == 'f':
                consultaDocentes()
            elif opcion == 'g':
                print('>>>Gracias por usar el software<<<')
                break
            else:
                print('>>>ERROR.Opción inválida. Intente de nuevo.')

iniciarSesion()
