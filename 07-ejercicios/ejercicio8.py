# Fille: ejercicio 8.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1-. Ingresar un número.
    2-. Sacar el porcentaje de ese número.

"""

num = (float(input("\nIngresa aqui el número al que le quieres sacar un porcentaje: ")))

porciento = (float(input(f"\nIngresa aqúi el porcentaje que quieres saber de {num} : %")))

porcentaje = (porciento*num / 100)

# Redondear el decimal a centésimas o a dos cifras.
print(f"\nEl {porciento}% de {num} es: {round(porcentaje,2)}")

