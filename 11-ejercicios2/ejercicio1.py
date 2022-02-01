# File: Ejecicio 1.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Ejercicio 1:
    - Hacer una lista con 8 números desordenados.
    - Imprimir la lista.
    - Recorrer la lista e imprimirla.
    - Ordenar lista.
"""

lista = [9, 1997, 32, 2, 2.5, 0.24, -18, 15]  # Lista con 8 elementos desordenados.
print(type(lista))                            # Verificar que tipo es la variable.
print(lista)                                  # Imprimir la lista.

print("")
for listas in lista:             # Recorrer los elementos de una lista.
    print(listas)

print("\n" + str(len(lista)))    # Ver cuantos elementos existen en la lista.

print(f"\n{lista.index(-18)}")   # Buscar elemento por índice en la lista.
print(9 in lista)                # Verificar sí éxiste un elemento en la lista.
print(102 in lista)

lista.sort()
print(f"\n{lista}")              # Ordenar lista (De menor a mayor)

print("")                        # Recorrer lista en una función. 
def conteo():
    resultado = ""

    for resultado in lista:
        print(resultado)

conteo()

