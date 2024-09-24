import json
from Persistencia.Guardar import guardar 
from Interfaz.Menu import menu

# Función para registrar módulos
def modulo(grup, arch):
    codigo = leerCodigo
    if modulo not in grup:
        nombre = leerNombre
        duracion = leerDuracion

        modulo = {
            'codigo': codigo,
            'nombre': nombre,
            'duracion': duracion
        }

        grup[codigo] = modulo

        grup = dict(sorted(grup.items()))
    guardar(grup, arch)

def leerCodigo():
        while True:
            try:
                codigo = input('Código del Modulo: ')
                if len(codigo.strip())== 0:
                    print('>ERROR. Código invalido')
                    continue
            except Exception as e:
                print('ERROR al ingresar el codigo.\n' + e)
def leerNombre():    
    while True:
        try:
            nombre = input('Ingrese nombre del modulo: ')
            if len(nombre.strip()) == 0:
                print('>ERROR. Al ingresar nombre.' )
                continue
            return nombre
        except Exception as e:
            print('ERROR al Ingresar el nombre.\n' + e)
def leerDuracion():
        while True:
            try:
                duracion = input('Duración del modulo?: ')
                if len(duracion.stip())== 0:
                    print('>ERROR. Al ingresar la duración del modulo')
                    continue
                return duracion
            except Exception as e:
                print('ERROR al ingresar la duración del modulo')

# Función para registrar estudiantes
def registrarEstudiante(grup, arch):
    cod = leerCod() 
    if cod not in grup:
        nombre = leerNom
        sexo = leerSex
        edad = leerEdad
        estudiante = {
            'nombre': nombre,
            'sexo': sexo,
            'edad': edad
        }

    grup[cod] = estudiante
    grup = dict(sorted(grup.items()))
    guardar(grup,arch)
def leerCod():
    while True:
        try:
            cod = input('Ingrese código del estudiante: ')
            if len(cod.strip()) == 0:
                print('>ERROR. Código inválido')
                continue
            return cod
        except Exception as e:
            print('ERROR Al Ingresar el código.\n' + e)

def leerNom():
    while True:
        try:
            nombre = input ('Nombre del estudiante: ')
            if len(nombre.strip()) == 0:
                print('>ERROR. Al ingresar el nombre')
                continue
            return nombre
        except Exception as e:
            print('ERROR Al ingresar el nombre.\n' + e)

def leerSex():
    while True:
        try:
            sexo = input('Ingrese el sexo del estudiante (M/F): ')
            if len(sexo.strip())== 0:
                print('>ERROR. Al ingresar el Sexo')
                continue
        except Exception as e:
            print('ERROR Al ingresar el sexo.\n' + e)

def leerEdad():
        while True:
            try:
                edad = int(input('Ingrese la edad del estudiante>>> '))
                if edad <= 0:
                    print('La edad debe ser un número positivo.')
                    continue
                break
            except ValueError:
                print('Por favor, ingrese un número válido para la edad.')

# Función para registrar docentes
def registroDocentes(grup,arch):
    cedula = leerCedula
    if cedula not in grup:       
        nombre = leerNomb
        docente = {
            'cedula': cedula,
            'nombre': nombre
        }

        grup[cedula] = docente
        grup = dict(sorted(grup.items()))

        guardar(grup,arch)

def leerCedula():
    while True:
        try:
            cedula = input('Cedula del docente: ')
            if len(cedula.strip()) == 0:
                print('>ERROR. Al ingresar la cedula')
                continue
        except Exception as e:
            print('ERROR Al ingresar la cedula.\n' + e)

def leerNomb():
    while True:
        try:
            nombre = input('Nombre del docente: ')
            if len(nombre.strip()) == 0:
                print('>>>ERROR. Al ingresar nombre')
        except Exception as e:
            print('ERROR al Ingresar nombre\n' + e)
 
# Función para listar estudiantes
def consultarEstudiantes():
    try:
        with open('datos\sistema.json', 'r') as archivo:
            estudiantes = json.load(archivo)
            if not estudiantes:
                print('No hay estudiantes registrados.')
            else:
                for estudiante in estudiantes:
                    print(f'Código:{estudiante["cod"]},
                           Nombre: {estudiante["nombre"]}, Sexo: {estudiante["sexo"]}, Edad: {estudiante["edad"]}')
    except FileNotFoundError:
        print('No hay estudiantes registrados.')

# Función para listar módulos
def consultaModulos():
    try:
        with open('datos/sistema.json', 'r') as archivo:
            modulos = json.load(archivo)
            if not modulos:
                print('No hay módulos registrados.')
            else:
                for modulo in modulos:
                    print(f'Código: {modulo["codigo"]}')
                    print(f'Nombre: {modulo["nombre"]}')
                    print(f'Duración: {modulo["duracion"]} de semanas')
    except FileNotFoundError:
        print('No hay módulos registrados.')

# Función para listar docentes
def consultaDocentes():
    try:
        with open('datos\sistema.json', 'r') as archivo:
            docentes = json.load(archivo)
            if not docentes:
                print('No hay docentes registrados.')
            else:
                for docente in docentes:
                    print(f'Cédula: {docente["cedula"]}, Nombre: {docente["nombre"]}')
    except FileNotFoundError:
        print('No hay docentes registrados.')
