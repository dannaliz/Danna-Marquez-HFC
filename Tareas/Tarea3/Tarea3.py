def modificar(palabra):
    posiblesContraseñas = []
    posiblesContraseñas.append(palabra.lower())  # Minúsculas
    posiblesContraseñas.append(palabra.upper())  # Mayúsculas
    posiblesContraseñas.append(palabra+"21") # Concatenar simbolos
    # Cambiar letras a numeros
    reemplazos = {
        'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
        'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5'
    }
    # letras a números
    modificada = ''.join(reemplazos.get(char, char) for char in palabra)
    posiblesContraseñas.append(modificada)

    return posiblesContraseñas

# Función principal para generar las contraseñas y escribirlas en un archivo
def generarContraseñas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as archivo:
        palabras = archivo.readlines()
        
    todas_contraseñas = []

    # Procesar cada palabra en el archivo
    for palabra in palabras:
        palabra = palabra.strip()  # Eliminar saltos de línea o espacios extra
        todas_contraseñas.extend(modificar(palabra))

    # Escribir contraseñas en el archivo de salida
    with open(archivo_salida, 'w') as archivo_out:
        for contraseña in todas_contraseñas:
            archivo_out.write(contraseña + '\n')
        
    print(f"Se generaron {len(todas_contraseñas)} posibles contraseñas en {archivo_salida}.")

        
archivo_entrada = 'palabras.txt'  # Archivo que contiene las palabras
archivo_salida = 'contraseñas_generadas.txt'  # Archivo donde se guardarán las contraseñas

generarContraseñas(archivo_entrada, archivo_salida)
