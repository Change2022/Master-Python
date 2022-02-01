# Fille: Tipos de datos.
# Purpose: Explicación de los tipos de datos informáticos/programables que son iterables.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Tipos de datos informáticos/programables comunmente utilizados en la programación:

Nada = None (La variable no contiene ningun tipo de dato iterable, no obstante, la nada es su dato guardado)

INT/Interger/Enteros = 12, 1256, 9, 12454566, 22

Float/Decimales = 12.5, 0.23, 1.254678, 1245684.2

STR/String/Cadena de texto = "Palabras" "y" 'Textos'

Bool/Booleanos = True/Verdadero / False/Falso

---------------------------------------------------------------------------
Colecciones de datos:

Tuplas/Tuple (12,"Hola",58.2)

Listas/List [123.65, "Nombre", [124], False]

diccionarios/Dict {palabraClave: valor encontrado}

---------------------------------------------------------------------------
El método [Type/Tipo], se encarga de imprimir en pantalla/consola el tipo de dato que contiene la variable,
esto para que el desarrollador se enteré de que tipo de dato está iterando.

---------------------------------------------------------------------------
La diferencia más notoria entre las colecciones de datos de tipo <list> y tiplo <tuple>, es que, ls tuplas
no pueden modificar sus valores, mientras que una lista sí lo puede hacer, esto de forma automática u por
el flujo que mantiene el código fuente.

Mientras que un diccionario, mantiene el acceso o evocación a los datos guardados por medio de una 
PALABRA CLAVE, también pueden ser modificados los valores que contiene de forma automática.

---------------------------------------------------------------------------
Tipos de datos extraordinarios:

[range/rango] = Muestra una secuencia numérica con rango limitado.

Entre otros...
"""

#Variable con nada.
nada = None
print(nada)
print(type(nada))

cadena = "\nHola, soy Roberto y soy un programador"     #String/Cadena de texto <str>
print(cadena)
print(type(cadena))

entero = 99
print("\n", entero)     #Interger/Entero <int>
print(type(entero))

flotante = 25.5
print("\n", flotante)   #Float/Flotante <float>
print(type(flotante))

booleano_verdadero = True
print("\n", booleano_verdadero)     #Booleano verdadero <bool>
print(type(booleano_verdadero))

booleano_falso = False
print("\n", booleano_falso)         #Booleano falso <bool>
print(type(booleano_falso))

#Tipos de colecciones de datos.

lista = [12, 24, 2.3, "Hola", [2+9], False]    #Listas <list>
print("\n", lista)
print(type(lista))

tupla = (12, 24, 2.3, "Hola", [2+9], False)    #Tuplas <tuple>
print("\n", tupla)
print(type(tupla))

diccionario = {
    "Nombre": "Roberto",
    "Apellidos": "Nahúm Sandoval",             #Diccionarios <dict>
    "Edad": 22

}

print("\n", diccionario)
print(type(diccionario))

rango = range(11)                              #Rango numérico <Range>
print("\n", rango)
print(type(rango))

