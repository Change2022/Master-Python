# File: Aburrido alv.jpg
# Autor: Roberto Rico Sandoval
# version: 0.0.1

"""

CRITERIOS:
    - Bucler for recorrido en 100
    - While incremento en 10
    - Decremento sobre el mismo while
"""

def recorrido(): 
    for number in range(1, 101):
        print(f"Número: {number}")

recorrido()

print("\n**********\n")

def operation():
    numero = 0
    print(f"Número: {numero}")
    while numero < 100:
        numero += 10
        print(f"Número: {numero}")

    print("\n**********\n")
    if numero >= 100:
        print(f"Número: {numero}")
        while numero != 0:
            numero -= 10
            print(f"Número: {numero}")

operation()

