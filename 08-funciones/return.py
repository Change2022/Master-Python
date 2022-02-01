# File: Return / Retorno.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
NOTA: La palabra reservada [return / retorno], nos permite extraer o devolver un valor local de la función al exterior,
      es decir, convierte un valor en estado local a un valor en estado global.
"""

def saludo(nombre):
    saludado = (f"\nHola {nombre}")

    return saludado

print(saludo("Roberto Sandoval"))   # Se imprime lo que está por dentro en la función, por el valor retornado.

print("\n##### EJEMPLO 2 #####\n")

def calculadora(num1, num2, basic = False):

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    divi = num1 / num2

    cadena = ""

    if basic != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(divi)

    return cadena

print(calculadora(20, 15, True))

"""
De está manera, nuestra variable "cadena", se recicla o vuelve a su estado original, cada que retornamos [return] en ella
"""
