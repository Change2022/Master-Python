# File: Ejecicio 2.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
EJERCICIO 2: 
    - Agregar elemenots a una lista, mientras que su longitud sea menor o igual a 120. Utilizando el bucle
    while y el bucle for.
    - Imprimir la lista.
    - recorrer la lista.
"""

lista = []
contador = []

operador = 0

print("\n***** Incremento de la lista en While *****\n")
while operador <= 119:
    operador += 1
    lista.append(operador)

print(lista)

print("\n***** Elementos recorridos de la lista en While *****\n")
for elementos in lista:
    print(elementos)


print("\n***** Elementos recorridos de la lista en For *****\n")
for element in range(1, 121):
    contador.append(element)

print(contador)

print("\n***** Elementos recorridos de la lista en For *****\n")
for numeros in contador:
    print(numeros)

