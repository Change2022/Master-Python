# File: Sistema de directorios de Python.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
DOCUMENTACIÓN:

    - [.isdir] = Verificar o evaluar la existencía de un directorio.
    - [.mkdir] = Método para crear un directorio.
    - [.rmdir] = Método para eliminar directorio. 
    - [.copytree] = Método para copiar un directorio.
    - [DnD] = Método o función, ya comprobado.
    - [.listdir] = Método que lista todo lo contenido de un directorio.
"""

# Módulo para manipular ficheros y directorios (archivos y carpetas) / os.
# Módulo para manipular rutas en el sistema / shutil.
import os, shutil   

# *** Crear carpetas ***

if not os.path.isdir("./14-sistema_de_archivos/mi_carpeta"):
    os.mkdir("./14-sistema_de_archivos/mi_carpeta")
else:
    print("Ya existe el directorio.")


# *** Eliminar carpeta ***
# os.rmdir("./14-sistema_de_archivos/mi_carpeta") [DnD]


# *** Copiar un directorio ***

directorio_original = ("./14-sistema_de_archivos/mi_carpeta")
directorio_copiado = ("./14-sistema_de_archivos/mi_carpeta_CARPETA")

# shutil.copytree(directorio_original, directorio_copiado) [DnD]

print("\n### Contenido de mi carpeta ###\n")

contenido = os.listdir("./14-sistema_de_archivos/mi_carpeta")
contenido2 = os.listdir("./14-sistema_de_archivos/mi_carpeta_CARPETA")

print(contenido)
print(contenido2, "\n")   # Lista vacía.

for ficheros in contenido:
    print("Nombre de fichero: " + ficheros)    # Recorrido de elementos en el directorio.

