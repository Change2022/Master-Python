# File: Tablas de múltiplicar en función.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Realizar una función con parámetros.
    2-. Generar una tabla de multiplicación con datos externos sobre la función.
"""

def tabla(num):
    print(f"\nTabla de múltiplicar del número: {num}\n")

    for contador in range(1, 11):
        operacion = num * contador

        print(f"{num} x {contador} = {operacion}")

num = (int(input("\nIntroduce aquí la tabla de múltiplicar que deseas saber: ")))
tabla(num)

# Misma función, pero cambia el tipo de parámetro.
print("\n*****Ejemplo 2*****\n")
for ntabla in range(1,11):
        tabla(ntabla)

