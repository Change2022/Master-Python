# Fille: ejercicio5.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Introducir 2 números.
    2- Mostrar el rango que hay en distancía de un número a otro.

"""

num1 = (int(input("\n¿Cuál es tu primer número? - ")))
num2 = (int(input("\n¿Cuál es tu segundo número? - ")))

if num1 < num2:
    
    for contador in range(num1, (num2) + 1):
        print(f"Estamos en el número: {contador}")
else:
    print("\nEl primer número, debe ser mayor al segundo número.")

