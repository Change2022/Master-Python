# Fille: ejercicio6.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Mostrar todas las tablas de multiplicar del 1 al 10.

"""

multiplicador = 1
contador = 1

print(f"\n### TABLA DE MÚLTIPLICAR DEL {multiplicador} ###")

while multiplicador <= 10:
    
    if contador == 11:
        multiplicador += 1  

        if multiplicador == 11:
            break

        print(f"\n### TABLA DE MÚLTIPLICAR DEL {multiplicador} ###\n")
        contador = 1

    print(f"{multiplicador} x {contador} = {multiplicador * contador}")

    contador += 1

