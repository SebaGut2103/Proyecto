#SoftWare de ACME 
from PROYECTO.Sesion import sesion
from Interfaz.Menu import menu
from Persistencia.Guardar import cargar
from Modelo.Registros import  insertarGrupo,modulo,insertarEstud,registroDocentes, registroAsis

registro = {}

archivo = 'PROYECTO\UTIS\Resgistro.json'

registro = cargar(archivo)

while True:
    op = menu()
    match op:
        case 'a':
            registro = insertarGrupo(registro,archivo)
        case 'b':
            registro = modulo(registro,archivo)
        case 'c':
            registro = insertarEstud(registro,archivo)
        case 'd':
            registro = registroDocentes(registro,archivo)
        case 'e':
            registro = registroAsis(registro,archivo)
        case 'f':      
            
