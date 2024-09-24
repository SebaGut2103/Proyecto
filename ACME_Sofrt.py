from Modelo.Registros import modulo, registrarEstudiante, registroDocentes,consultaDocentes, consultaModulos, consultarEstudiantes
from Interfaz.Menu import menu



def main():
    while True:
            menu()
            opcion = input('Seleccione una opción: ')

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
                print('Gracias por usar el software...')
                break
            else:
                print('>>>ERROR.Opción inválida. Intente de nuevo.')

if __name__ == '__main__':
    main()
