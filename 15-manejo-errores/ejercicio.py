# File: Capturar excepciones y errores.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

lista = []

for number in range(1, 101):
    lista.append(number)
    print(f"Número: {number}")


try:
    search = int(input("\nIngresa el número a buscar: "))
    lista.index(search)
except:
    print("\nEl número no está en la lista, La lista va del 1 al 100. lo siento :(")
else:
    print(f"\nSe a encontrado el número [{search}] en el índice [{lista.index(search)}]")
finally:
    print("\nFin de la iteración.")

