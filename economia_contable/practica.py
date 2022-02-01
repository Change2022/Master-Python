# Fille: praáctica 5
# Autor: ZioneR.
# versión: V.0.1

import random

def num():

    clave = random.randrange(0, 5000)
    jack = intento = 0

    while jack != clave:
        jack = random.randrange(0, 5000)
        intento += 1
        print(f"Asimilando la clave...\nNo. intento {intento}\n")
    else:
        print(f"Se ha encontrado la contraseña: {jack}")
        print("Usted a sido jackiado por la chapitxa ;v")

num()

