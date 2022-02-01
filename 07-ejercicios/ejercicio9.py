# File: ejercicio 9.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Ingresar un número en específico o exacto.
"""

print("\n¿Cuál es el resultado de sumar 50 + 38 + 22 + 1?")

respuesta = (int(input("\nRE: ")))

while respuesta != 111:
    print("\nHaz incertado un valor erroneo, vulve a intentarlo")
    respuesta = (int(input("\nRE: ")))

    if respuesta == 111:
        print(f"\nFelicidades, el número [{respuesta}] es el resultado correcto.")
        break

