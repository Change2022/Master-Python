# File: Sistema de ficheros de Python.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
ELEMENTOS ÚTILIZADOS EN ESTE PROYETO:

    - [io] = Package.
    - [open] = Módulo proveniente de IO, para abrir y crer ficheros en Python.
    - [pathlib] = Módulo para rutas en ficheros y carpetas.
    - [.absolute()] = Función para crear rutas absolutas.
    - [.close()] = Función para cerrar el fichero.
    - [.read()] = Método para leer el contenido de un fichero desde la consola.
    - [.write()] = Método para escribir contenido en un fichero; desde el código de programación.
    - [.readlines()] = Método para generar listas dentro del contenido de un fichero.
    - [.is] = Función para verificar o comprobar en una condición a un elemento en especifíco.
    - [.copyfile] = Método predeterminada, para copiar archivos.
    - [.move] = Método predeterminado, para mover a otra ruta a un fichero.
"""

from io import open
import pathlib   # Módulo para manejo de ficheros en ruta.
import shutil    # Módulo para copiar, cortar, borrar y mover ficheros.
import os        # Módulo para eliinar archivos.
import os.path   # Módulo para verificar la existencia de un fichero.

# ***** Abrir archivo *****

# Genera un fichero dentro de una ruta especificada dentro de una carpeta
archivo = open("./14-sistema_de_archivos/fichero_textos.txt", "a+")  # Permiso "a+".
archivo.write("\n**** Hola, creamos un fichero desde el código de Python ****\n")
archivo.close()

# Genera un fichero (archivo), al hazar dentro de alguna parte del almacenamiento de la PC.
archivo = open("fichero_textos.txt", "a+")

# Genera un fichero dentro de una ruta especificada dentro de una carpeta (forma 2).
ruta = str(pathlib.Path().absolute()) + "/fichero_textos.txt"
archivo = open(ruta, "a+")

# Escribir dentro de un fichero.
archivo.write("\n**** Hola, creamos un fichero desde el código de Python ****\n")

# Cerrar el archivo.
archivo.close()


# ***** Leer un fichero *****

ruta = str(pathlib.Path().absolute()) + "/fichero_textos.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido del fichero.
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en una lista.
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:

    if not frase.isnumeric():
        print("- ", frase.upper())


# ***** Copiar archivos *****

ruta_original = str(pathlib.Path().absolute()) + "/fichero_textos.txt"              # Fichero a copiar.
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_textos_copiado.txt"         # Fichero copiado.

# Fichero copiado con una ruta alterna a la ruta (carpeta) original.
ruta_alternativa = "./07-ejercicios/fichero_textos_copiado2.txt"  

shutil.copyfile(ruta_original, ruta_alternativa)   # Orden para copiar fichero.


# ***** Mover archivos *****

ruta_original = str(pathlib.Path().absolute()) + "/fichero_textos_copiado.txt"     # Ruta original del fichero.
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_textos_copiado_NUEVO.txt"  # Nueva ruta del fichero.

#shutil.move(ruta_original, ruta_nueva)          # Orden para mover fichero.


# ***** Eliminar ficheros *****

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_textos_copiado_NUEVO.txt"  # fichero a eliminar.

#os.remove(ruta_nueva)

print(os.path.abspath("../"))

ruta_a_comprobar = os.path.abspath("./") + "./fichero_textos.txt"
ruta_a_comprobar = "./modulo.py"
print(ruta_a_comprobar)

if os.path.isfile(ruta_a_comprobar):
    print("El fichero si se encontro en el sistema.")
else:
    print("El archivo no se encontro en el sistema")

