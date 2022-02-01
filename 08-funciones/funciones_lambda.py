# File: funciones lambda.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Las funciones lambda, son funciones discretas o funciones anonimas, es decir, no tienen un nombre
pre-establecido. Estás son ocupadas para hacer tareas pequeñas que suelen ser muy repetitivas.
Estás funciones no suelen ser complejas en su extructura programática.
"""

"""
Estructura de una función lambda:
    variable = [lambda] parámetro: valor a operar, imprimir...etc.
    imprimir(variable&funcion(valorDelParámetro))
"""

year = lambda year1: f"\nEl año es: {year1}"
print(year(2021))

suma = lambda sumaton: f"\nLa suma es {sumaton + 52.6}"
print(suma(87.77))

