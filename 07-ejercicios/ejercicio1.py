# Fille: ejercicio1.
# Purpose: Impresiones.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:
    1- Crear 2 variables (pais y continente)
    2- Mostrar su valor por pantalla (imprimir)
    3- Poner un comentario diciendo el tipo de dato de las variables
    
"""

pais = input("\n¿En cuál pais vives? - ")              # Tipo String (str)
continente = input("¿\nEn cuál continente vives? - ")  # Tipo String (str)
year = (int(input("¿\nEn qué año vives? - ")))         # Tipo interger (int)

print(f"\nVives en el pais de {pais}, y en el continenete {continente}, estás en el año {str(year)}\n")

print(type(pais))
print(type(continente))
print(type(year))

