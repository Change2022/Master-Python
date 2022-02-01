# File: Variables locales y globales.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
VARIABLES LOCALES:
    Una variable local es aquella variable que se define dentro de un bloque de código como puede ser el que este adentro de una
    función, un bucle/loop o una condicional.

    Las variables locales, no pueden ser utilizadas afuera del bloque de código, en donde, se originaron, ha menos que
    utilicemos la función de la palabra [return], para retornar algún tipo de valor a los argumentos de la función.

VARIABLES GLOBALES:
    Son todas esas variables que se declaran afuera de una función, estás variables pueden ser utilizadas afuera y dentro de
    un bloque de programación.
"""

# Variables globales.

frase = "\n!Qúibo pinche prra¡ *La nalguea y le compra 3 pollos asados y una coca de 3L."
print(frase)

# Variables locales.
def holaMundo():
    frase = "Hola mundo"   # variable local
    print("\nEsto está dentro de la función:\n")
    print(frase)

    global color     # Conversión de variables
    color = "Rojo"
    print("Está es la conversión de una variable local a global:", color)

    year = 2021    # Aquí extraemos un dato del bloque, para el código externo o general, utilizando la palabra reservada [return].
    return "Dato retornado: " + str(year)  

print(holaMundo())
print("Aquí se imprime de forma global nuestra variable convertida:", color)

"""
NOTA: Se útiliza la palabra reservada [global], para hacer una conversión de una variable local a global
"""

