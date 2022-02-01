# File: ejercicio 12.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Programar la ley de Ohm.
"""

import random

def ohm():
    print("\n##### LEY DE OHM #####")

    V = random.randrange(10, 500)
    I = random.randrange(10, 500)
    R = random.randrange(10, 500)

    voltios = (round(I*R,2))
    ohmnios = (round(V/I,2))
    amperes = (round(V/R,2))
    
    print(f"\n(V) = {V}\n(R) = {R}\n(I) = {I}")

    print(f"\n\nEl voltaje es de: {voltios}V")
    print(f"\nLa resistencia es de: {ohmnios}Ω")
    print(f"\nLa corriente es de: {amperes}A")


ohm()

