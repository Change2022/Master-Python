# File: Parámetros opcionales.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Colocar parámetros u argumentos opcionales dentro de una función.
"""

def getEmpleado(nombre, ID=None):
    print("\nEmpleado.")
    print(f"Nombre: {nombre}")

    if ID != None:
        print(f"ID: {ID}")
    else:
        print(f"ID: {ID}")

getEmpleado("Roberto Sandoval")

"""
NOTA: El valor [None/Nada], declara un valor vacío o sin valor, para "pasar" y poder seguir ejecutando el programa
      sin que se generen errores de programación.
"""
