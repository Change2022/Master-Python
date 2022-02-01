# File: Ejecicio 4.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
EJERCICIO 4:

    - Hacer una variable de tipo str.
    - Hacer una variable de tipo int.
    - Hacer una variable de tipo list.
    - Hacer una variable de tipo bool.
    - Imprime cada tipo de dato de las variables.
    - Verificalo con una función.
"""

cadena = ""
num = 0
lista = []
boli = True

print(f"\nTipos de datos encontrados: \n{type(cadena)}, \n{type(num)}, \n{type(lista)}, \n{type(boli)}")

def tipos(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = (f"\nEste dato es de tipo: {traducirTipo(tipo)}")
    else:
        result = None

    return result

def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "Lista"
    elif tipo == str:
        result = "Cadena de texto"
    elif tipo == int:
        result = "Entero"
    elif tipo == bool:
        result = "Booleano"
    
    return result

print(tipos(lista, list))
print(tipos(cadena, str))
print(tipos(num, int))
print(tipos(boli, bool))

