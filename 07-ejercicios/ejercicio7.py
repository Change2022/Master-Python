# Fille: ejercicio7.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Mostrar número impares hasta el 100 con elección del número impar del usuario.

"""

eleccion = (int(input("Coloca el número impar que más te guste del 1 al 100\nIngresa aquí: ")))

while eleccion > 100 or eleccion <= 0:
    print(f"\n[{eleccion}] El número ingreado no es valido, sólo se admiten números del 1 al 100")
    eleccion = (int(input("\nColoca el número impar que más te guste del 0 al 100\nIngresa aquí: ")))

while not(eleccion % 2):
    print(f"\n[{eleccion}] no es un número impar, vuelve a intentarlo.")
    eleccion = (int(input("\nColoca el número impar que más te guste del 0 al 100\nIngresa aquí: ")))

print("\n----------------\n\nInicio de la cuenta de los números impares:\n")

for eleccion in range(eleccion, 101):
    if eleccion % 2:
        not(eleccion)
        print(eleccion)

print("\n----------------\n\nFin de la cuenta de los números impares:")

