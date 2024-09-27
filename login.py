from Persistencia.Contrasenas import guardarContra,cargarContra, encryptContra



def iniciarSesion():
    archivo = 'datos/usuario.json'

    print('>>> ACME.SOFT <<<')
    usuario =  input('Ingrese usuario:\n')
    contra = ('Ingrese contraseña:\n')
    datos = cargarContra(archivo)
    if datos is None:
        datos = {
          'usuario' : usuario,
          'contraseña' : encryptContra(contra)
       }
        guardarContra(archivo, datos)
    else:
        if (datos["usario"]) == usuario and (datos["contraseña"]) == encryptContra(contra):
            print('Ingreso exitoso...')
        else:
            print('Contraseña incorrecta...')
    
iniciarSesion()