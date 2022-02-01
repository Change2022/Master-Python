# File: Simulador de cotizaciones.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

import random 

def cotizacion():

    print("\n***** Bienvenido al sistema de cotizaciones para trabajos electrónicos *****\n")

    precio_electronico = random.uniform(500, 10000)
    piezas = random.uniform(50, 500)

    total_R = (0.5 * precio_electronico + piezas)
    manoDeO = (0.5 * precio_electronico - piezas)

    print(f"\nEl precio del electrónico a reparar es de: $[{round(precio_electronico,2)}]")
    
    if total_R > piezas:
        print(f"\nEl total a cobrar al cliente es de ${round(total_R,2)}")
        print(f"Es posible total tener una ganancia de: {round(manoDeO,2)}")
    else:
        print(f"\nEl total a cobrar al cliente es de ${round(total_R,2)}")
        print(f"No es rocemendable hacer la reparacion")

    if manoDeO < 300:
        print(f"\nLa ganancía es poca: ${round(manoDeO,2)}")
    else:
        print(f"\nEs una buena ganancía: ${round(manoDeO,2)}")

cotizacion()

