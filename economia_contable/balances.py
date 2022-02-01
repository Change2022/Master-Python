# Fille: Balances.
# Purpose: Funciones económicas-contables.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

1- Simular cómo funciona la operación para saber el estado de la liquidez de una empresa.
2- Simular cómo funciona la operación para saber el estado de la solvencia de una empresa.

"""

import random

print("\n***BIENVENIDO AL SISTEMA DE BALANCE***\n\nBotón 1 = Liquidez\nBotón 2 = Solvencia ecónomica")

eleccion = int(input("\nInserta aquí tú opción elegída: "))

while eleccion < 1 or eleccion >= 3:
    print("\nDato invalido. Vuelve a intentarlo.")
    eleccion = int(input("\nInserta aquí tú opción elegída: "))

def liquidez():
    
    activos_C = random.randrange(100000, 1000000)
    pasivos_C = random.randrange(100000, 1000000)

    liqui = (activos_C / pasivos_C)

    print("\n-----------------------------")
    print("\nHaz elegido la opción de liquidez económica.")
    
    print("\nLa liquidez de tú empresa es de: %", round(liqui, 2))

    if liqui <= 0.9:
        print("\nNo existe liquidez económica en la empresa.")
    elif liqui >= 1.0 and liqui < 2.0:
        print("\nExiste una solvencia económica en la empresa.")
    elif liqui >= 2.0:
        print("\nExiste una solvencia económica en la empresa y hay capital disponible sin uso.")

def solvencia():
    
    activos_T = random.randrange(100000, 1000000)
    pasivos_T = random.randrange(100000, 1000000)

    solven = (activos_T / pasivos_T)

    print("\n-----------------------------")
    print("\nHaz elegido la opción de solvencia económica.")

    print("\nLa solvencia de tú empresa es de: %", round(solven, 2))

    if solven <= 0:
        print("\nNo hay solvencia económica en la empresa.")
    elif solven >= 1.0:
        print("\nExiste una solvencia económica.")


if eleccion == 1:
    liquidez()
elif eleccion == 2:
    solvencia()

