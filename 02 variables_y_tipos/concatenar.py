# Fille: concatenar
# Purpose: Explicación de la conjunción y/o conbinación de los valores en las variables.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
La concatenación de datos se una operación programática, en donde, se suman o conjuntan dos o más variables
con un tipo de dato programable IGUAL o SEMEJANTE cómo valores STR con valors STR, valores numéricos cómo
enteros/INT con valores INT ó valores FLOAT/decimales.

La concatenación consite en sumar valores de un mismo tipo o semejantes, en una misma línea de impreción
, para mostrar en pantalla.
"""

"""
Criterios:

    1- sumar o concatenar variables tipo str.
    2- concatenar variables str por separación.
    3- concatenar por medio del mecanismo [f-string]
    4- Utilizar el método .format, para concatenar variables.
"""

nombre = "Roberto"
apellido_paterno = "Nahúm"
apellido_materno = "Sandoval"
edad = "22"

nombre_completo_y_edad = (f"\n{nombre} {apellido_paterno} {apellido_materno} {edad}")

print(nombre + " " + apellido_paterno + " " + apellido_materno, "\n")   #Suma de cadenas de texto.
print(nombre, apellido_paterno, apellido_materno, "\n")                 #Concatenación por separación de valores.

#Mecanismo [f-string]
print(f"{nombre} {apellido_paterno} {apellido_materno}")

"""
Este mecanismo "moderno" de Python, "simplifica" a la estructura que maneja una concatenación de variables
en suma [num 1 + num 2], en la impresión de una misma línea de código, en donde, se coloca la palabra
reservada [f] y los parámetros en llave {} que esperán el nombramiento o algún dato dentro.

No es necesario colocar espacios entre los valores de las variables, ya que, el mecanismo "f", ya los
incluye.

Este mecanismo puede estar también incluido dentro de la asignación de algún valor de una variable.
"""

#Concatenación por el método o función [.format]
print("\n!Hola¡ Me llamo {} {}, tengo {} años".format(nombre, apellido_paterno + " " + apellido_materno, edad))

"""
El método .format, en su parámetro esperá que el desarrollador o el flujo del código coloque algún tipo de 
valor informático o el nombre de una variable, para rellenar con ello, los campos en llave que contiene.
"""

print(nombre_completo_y_edad)

