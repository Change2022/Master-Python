# Fille: ejercicio3.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Elevar al cuadrado los numeros naturales del 1 al 60 con el bucle for.
    2- Elevar al cuadrado los numeros naturales del 1 al 60 con el bucle while.

"""

cuaF = 1
cuaW = 1

for cuaF in range(1, 61):
    print(f"El número al cuadrado de {cuaF} es: {cuaF * cuaF}")
    cuaF += 1

print("\n--------------------\n")

while cuaW <= 60:
    print(f"El número al cuadrado de {cuaW} es: {cuaW * cuaW}")
    cuaW += 1

