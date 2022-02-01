# File: ejercicio 11.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1- Hacer una función que haga operaciones contables para saber cuanto se debe ahorrar.
    2- Establecer un ahorro minímo del 10%
"""

import random

def ahorradito():

    ingresos_totales = random.randrange(6000, 30000)
    gastos_totales = random.randrange(2000, 12000)
    
    flujo_total = (ingresos_totales - gastos_totales)
    ahorro_min = 0.10

    nombre = input("\n¿Cuál es tu nombre? - ")

    print(f"\n{nombre}: Tienes ingresos mensuales de $ {ingresos_totales}\n{nombre}: Tienes gastos mensuales de $ {gastos_totales}")
    print(f"\n{nombre}: Tienes un flujo total mensual de $ {flujo_total}")

    if flujo_total <= 0:
        print("\nTienes una muy mala economía, no puedes ahorrar por el momento.")
    else:
        print(f"\nTu tasa miníma de ahorro sería del 10% sobre tu flujo mensual --- $ [{round(ahorro_min*flujo_total,2)}]")

        eleccion = (int(input(f"\n{nombre}: ¿Quieres saber algún porcentaje en específico de tu flujo mensual?\n\nPresiona el botón 1 = sí\nPresiona cualquier otra botón = No\nInserta aquí - ")))

        if eleccion == 1:
            ahorro_selecto = (int(input("\nIngresa aquí el valor de la tasa a evaluar: ")))
            flujo_total_selecto = (ahorro_selecto * flujo_total / 100)
            print(f"\nEl {ahorro_selecto}% de $ {flujo_total} es: $ {round(flujo_total_selecto,2)}")
            print("\nGracias, vuleva pronto :)")
        else:
            print("\nGracias, vuleva pronto, no hay tortillas :)")

ahorradito()

