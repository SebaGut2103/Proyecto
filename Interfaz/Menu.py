from ..Opciones import 


def menu():
    while True:
        print('<***MENU***>')
        print('<---a.Registro de grupos.--->')
        print('<---b.Registro de módulos.--->')
        print('<---c.Registro de estudiantes.--->')
        print('<---d.Registro de docentes.--->')
        print('<---e.Registro de asistencia.--->')
        print('<---f.Consultas de información.--->')
        print('<---g.Generación de informes.--->')
        print('<---h.Cambio de contraseña.--->')
        print('<---i.Salida del sistema..--->')

        print('>>>Opción? ', end='')
        try:
            opcion = input()
            if opcion < 'a' or opcion >'i':
                print('>>ERROR. Opción no valida.\n')
                input('Presione cualquier tecla para volver al menú...')
                continue
            return opcion 
        except ValueError:
            print('>>>ERROR. Opción no valida.\n')
            input('Presione cualquier tecla para volver al menu...')
