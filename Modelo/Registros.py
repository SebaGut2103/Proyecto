import json

# Función para registrar módulos
def modulo():
    codigo = input('Código del Modulo?>>> ')
    nombre = input('Ingrese el nombre del módulo>>> ')
    duracion = input('Ingrese la duración del módulo en semanas>>> ')

    modulo = {
        'codigo': codigo,
        'nombre': nombre,
        'duracion': duracion
    }

    try:
        with open('UTIS/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
    except FileNotFoundError:
        modulos = []

    modulos.append(modulo)

    with open('UTIS/modulos.json', 'w') as archivo:
        json.dump(modulos, archivo, indent=4)
    print('Módulo registrado correctamente.')

# Función para registrar estudiantes
def registrarEstudiante():
    codigo = input('Código del estudiante?>>> ')
    nombre = input('Ingrese el nombre del estudiante>>> ')
    sexo = input('Ingrese el sexo del estudiante (M/F)>>> ')

    while True:
        try:
            edad = int(input('Ingrese la edad del estudiante>>> '))
            if edad <= 0:
                print('La edad debe ser un número positivo.')
                continue
            break
        except ValueError:
            print('Por favor, ingrese un número válido para la edad.')

    estudiante = {
        'codigo': codigo,
        'nombre': nombre,
        'sexo': sexo,
        'edad': edad
    }

    try:
        with open('UTIS/estudiantes.json', 'r') as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        estudiantes = []

    estudiantes.append(estudiante)

    with open('UTIS/estudiantes.json', 'w') as archivo:
        json.dump(estudiantes, archivo, indent=4)
    print('Estudiante registrado correctamente.')

# Función para registrar docentes
def registroDocentes():
    cedula = input('Cédula del docente>>> ')
    nombre = input('Ingrese el nombre del docente>>> ')

    docente = {
        'cedula': cedula,
        'nombre': nombre
    }

    try:
        with open('UTIS/docentes.json', 'r') as archivo:
            docentes = json.load(archivo)
    except FileNotFoundError:
        docentes = []

    docentes.append(docente)

    with open('UTIS/docentes.json', 'w') as archivo:
        json.dump(docentes, archivo, indent=4)
    print('Docente registrado correctamente.')

# Función para listar estudiantes
def consultarEstudiantes():
    try:
        with open('UTIS/estudiantes.json', 'r') as archivo:
            estudiantes = json.load(archivo)
            if not estudiantes:
                print('No hay estudiantes registrados.')
            else:
                for estudiante in estudiantes:
                    print(f'Código: {estudiante["codigo"]}, Nombre: {estudiante["nombre"]}, Sexo: {estudiante["sexo"]}, 
                          Edad: {estudiante["edad"]}')
    except FileNotFoundError:
        print('No hay estudiantes registrados.')

# Función para listar módulos
def consultaModulos():
    try:
        with open('UTIS/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
            if not modulos:
                print('No hay módulos registrados.')
            else:
                for modulo in modulos:
                    print(f'Código: {modulo["codigo"]}, Nombre: {modulo["nombre"]}, 
                          Duración: {modulo["duracion"]} semanas')
    except FileNotFoundError:
        print('No hay módulos registrados.')

# Función para listar docentes
def consultaDocentes():
    try:
        with open('UTIS/docentes.json', 'r') as archivo:
            docentes = json.load(archivo)
            if not docentes:
                print('No hay docentes registrados.')
            else:
                for docente in docentes:
                    print(f'Cédula: {docente["cedula"]}, Nombre: {docente["nombre"]}')
    except FileNotFoundError:
        print('No hay docentes registrados.')

# Función para mostrar el menú principal
def menu():
    print('\n---- Menú Principal ----')
    print('a. Registrar Módulo')
    print('b. Registrar Estudiante')
    print('c. Registrar Docente')
    print('d. Consultar Estudiantes Registrados')
    print('e. Consultar Módulos Registrados')
    print('f. Consultar Docentes Registrados')
    print('g. Salir')

# Función principal del programa
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

# Punto de entrada del programa
if __name__ == '__main__':
    main()
