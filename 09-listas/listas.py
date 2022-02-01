# File: listas.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
LISTAS (ARRAYS):
    Las listas son colecciones de datos que se almacenan en una variable como valor, de esta forma,
    la lista también es un tipo de dato [list / lista]

Funciones: [List / Lista]

Método: [append / apéndice]
"""

pelicula = "\nBatman"

# Definición de listas.
peliculas = ["Superman", "Viejas cachondas", "Vaqueras rikolinas"]
variada = ["Roberto", 123, 12.555, ["Hola"]]
cantantes = list(("Zoe", "Enjambre", "Camilo VII"))
year = list(range(1, 2021))

print(pelicula)
print(variada)
print(peliculas)
print(cantantes)
print(year)

print("\n### Índices ####\n")

print(peliculas[1])
print(peliculas[-2])

print(cantantes[0:1])
print(cantantes[1:3])
print(variada[1:])     # Empezar a imprimir desde el índice 1

# Modificar índices.
peliculas[1] = "Star Wars y panochas calientes"
peliculas[2] = "Bob Esponja XXX"
print(peliculas)

# Añadir elementos a la lista.
cantantes.append("Justin Sierreño")
cantantes.append("La Sailorfag")
print(cantantes)

