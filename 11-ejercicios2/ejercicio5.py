# File: Ejecicio 5.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
EJERCICIO 5:

    - Crear una lista con el contenido de la siguiente tabla...
    - ACCIÓN   AVENTURAS      DEPORTES
    -  GTA      ASSASSINS      FIFA
    -  COD      ZELDA          NFL
    -  PUBG     TWTCHER        MOTO GP

    - Guardar la tablaa en un diccionarió multidimensional.
"""

tabla = [
    {
        "Categoría" : "ACCIÓN",
        "Juegos" : ["GTA", "PUBG", "Call Of Duty"]
    },
    {
        "Categoría" : "AVENTURAS",
        "Juegos" : ["ASSASSINS CREED", "ZELDA", "The Witcher"]
    },
    {
        "Categoría" : "DEPORTES",
        "Juegos" : ["FIFA", "NFL", "MOTO GP"]
    }
]

print(f"\n{tabla}\n")

for categoria in tabla:
    print(f"----------{categoria['Categoría']}----------")

    for juego in categoria['Juegos']:
        print(juego)

