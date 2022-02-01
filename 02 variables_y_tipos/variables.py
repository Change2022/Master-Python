# Fille: variables
# Purpose: Explicación de ¿que son y para que sirven las variables en lña programación?
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Una variables es un "contenedor" o "caja" que contiene información, que por dentro guardara un tipo de 
dato informático/programable. Se pueden generar diferentes variables en un mismo código fuente, las cuales,
puden tener un tipo de valor informaticó/programable distinto.

El valor de una variable, puede ser modificada y/o cambiado por el flujo del código, en cualquier momento.

NOMBRAMIENTO DE VARIABLES:
 
 Tipo camello [sumaDeNumeros = 5]

 Tipo encadenada/secuencial [suma_de_numeros = 5]

 Tipo enumarada correctamente [suma1 = 10]
 
 Tipo enumerada incorrectamente [1suma = Error de sitnaxis]

 Nombramiento de variables con espacios o signos no aceptados [suma de valores = Error de sintaxis]

-------------------------------------------

Python es debilmente tipado, por lo cual, se pueden modificar y/o actualizar el tipo de valor de una variable
de forma "sencilla", sin la necesidad de especificar en el NOMBRAMIENTO de la variable, el tipo de dato
que está mantiene.
"""

"""
CRITERIOS:

    1- Creación de variables con NOMABRAMIENTOS y ASIGNACIÓN DE VARIABLES.
    2- Impresión de los valores asignados en las variables.
    3- Actualizar el valor de asiganmiento en las variables.

"""

cadena_de_texto = "Estoy aprendiendo el lenguaje de Python 3"
print(cadena_de_texto)

cadena_de_texto2 = "Con Roberto Nahúm Sandoval"
print(cadena_de_texto2)
print("----------------------------------")

cadena_de_texto = 5    #Variable actualizada de str a int.
print(cadena_de_texto)
print("----------------------------------")

numeroEntero = 458
print(numeroEntero)

numeroDecimal = 10.11
print(numeroDecimal)
print("----------------------------------")

numeroEntero = 887     #Actualización de variable con el mismo tipo de dato informático, 
numeroDecimal = 8.95   #Pero diferente valor iterable/numerable.

print(numeroEntero)
print(numeroDecimal)

