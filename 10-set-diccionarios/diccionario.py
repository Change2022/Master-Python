# File: diccionario.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
DICCIONARIÓ:

    Un diccionario es una colección de datos, el cual, utiliza índices alfanuméricos, los cuales, llevan
    una palabra clave, para acceder al valor del índice.

    Es conocido en otros lenguajes de programación como Array asociativo u objetos Json.
"""

persona = {
    "Nombre" : "Roberto",
    "Apellidos" : "Rico Sandoval",
    "Edad" : 22
}

print("")
print(type(persona))
print(persona)
print(persona["Apellidos"])
print(persona["Edad"])

