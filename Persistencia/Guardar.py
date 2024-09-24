from pathlib import Path
import json
def guardar(grup, arch):
    with open(arch,'w') as fd:
        json.dump(grup, fd)
    if not fd.closed():
        fd.close

def cargar (arch):
    archivo = Path(arch)
    grup = {}
    if archivo. is_file():
        try:
            with open(arch,'r') as fd:
                grup = json.load(fd)
            
            if not fd.closed:
                fd.close
        except Exception as e:
            print('>>>ERROR al abrir el archivo.\n' + e)
    else:
        print('>>>ERROR. El archivo no existe.')
        input('>>>Presione cualquier tecla para continuar...')

    return grup