# Fille: valores_especiales_de_impresion.
# Purpose: Explicación de instrucciones especiales en Python 3, para la impresión de datos.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Criterios:

    Implementación de métodos reservados para la impresión de valores.

-----------------------------------------------------------

Impresión de comillas simples en el texto - ["Somos 'novios'."]
Impresión de comillas dobles en el texto - ["Somos \"Hola mundo\" ."] >>> ["\"\""]

Saltos de línea en el texto >>> [\n]

Generar una tabulación o sangrado en la impresión >>> [\t]

"""

cadena1 = "Lenguaje de programación Python 3 dice: "

#Impresión de cadenas de texto con comillas en el texto.
cadena2 = "\"Hola mundo\" "
cadena3 = "\nLenguaje de programación Python 3 dice: 'Hola mundo'"
cadena4 = "\n\tLenguaje de programación Python 3 dice: 'Hola mundo'"

print(f"{cadena1} {cadena2}")     #Impresión de texto con palabras en comillas dobles entre el texto.

print(cadena3)     #Impresión de texto con palabras en comillas simples entre el texto.
print(cadena4)     #Impresión de valor con tabulación.

