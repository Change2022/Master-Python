# File: listas 2.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
LISTAS (ARRAYS):
    Las listas son colecciones de datos que se almacenan en una variable como valor, de esta forma,
    la lista también es un tipo de dato [list / lista]

Funciones: [List / Lista]

Método: [append / apéndice]
"""

# Recorrido de lista.

pelicula = "Las chicas super mamadoras"
peliculas = ["Polonias calientes", "Zorras de monte", "Puchas pelonas"]

print("\n***** LISTADO DE PELICULAS XXX *****\n")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introuce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

