# Fille: ejercicio2.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- imprimir todos los números pares del 1 al 120
    2- imprimir todos los números impares del 1 al 120

"""

num = 2
num2 = 1

while num <=120:
    print(f"Este número es par: {num}")
    num += 2

print("\n--------------------\n")

while num2 <= 120:

    if num2%2 != 0:
        print(f"Este número es impar: {num2}")
    num2 += 1

