# Fille: Converión de datos.
# Purpose: Explicación del cambio o transformación en los tipos de datos.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
las conversiones de datos se utiliza para que las variables sean compatibles entre sí, para evitar 
errores de programación

Error: TypeError

"""

saludo = "Hola, soy Fernanado. Tengo "
edad = 18

print(saludo + str(edad))     #Concatenación de valores sin errores de sintaxis, por la conversión ->
                              #De datos.
edad = str(18)
print(type(edad))

edad = int(18)                #Conversión del tipo de valor asiganado.
print(type(edad))

edad = float(18.5)            
print(type(edad))

