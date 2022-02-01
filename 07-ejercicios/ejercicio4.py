# Fille: ejercicio4.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Pedir dos números al usuario.
    2- pedir que quiere hacer con los números ingresados. ¿sumarlos, restarlos, múltiplicarlos, dividdirlos?

"""

num1 = (float(input("\nIngresa tu primer número - ")))
num2 = (float(input("\nIngresa tu segundo número - ")))

print("\n¿Qué deseás hacer con estos números?")

eleccion = (int(input("\n1 = Suma\n2 = Resta\n3 = Multiplicación\n4 = División\n\nIngresa aquí: ")))

while eleccion < 1 or eleccion > 4:
    print("\nDato incorrecto. Vuelve a intentarlo.")
    eleccion = (int(input("\n1 = Suma\n2 = Resta\n3 = Multiplicación\n4 = División\n\nIngresa aquí: ")))

if eleccion == 1:
    print(f"\nElegiste SUMA de {num1} + {num2} = {num1 + num2}")
elif eleccion == 2:
    print(f"\nElegiste RESTA de {num1} - {num2} = {num1 - num2}")
elif eleccion == 3:
    print(f"\nElegiste MULTIPLICACIÓN de {num1} x {num2} = {round(num1 * num2,2)}")
elif eleccion == 4:
    print(f"\nElegiste DIVISIÓN de {num1} / {num2} = {round(num1 / num2,2)}")

print("### FIN ###")

