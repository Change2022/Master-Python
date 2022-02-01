# File: funciones predefinidas.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
FUNCIONES PREDEFINIDAS: 

- las funciones predefinidas también se conocen como métodos o palabras reservadas del lenguaje, en donde, insertamos una
  "palabra cláve". la cual,invoca a una función que ya está precargada dentro de las librerías principales del lenguaje
   de programación ocupado.

- Caso de ello pueden ser [isinstance, strip, del, return, print, lower...etc.]
"""

# Funciones generales
nombre = "Roberto Sandoval"
print(nombre)
print(type(nombre))


# Comprobar el tipado o tipo de dato de una variable.
comprobar = isinstance(nombre, str)  # Comprueba sí la variable colocada como argumento es de tipo <str>
if comprobar:
    print("Esa variable es un <str>")
else:
    print("No es un <str>")

if not isinstance(nombre, int):
    print("La variable no es un número entero")


# Limpiar espacios.
frase = "\n        contenido"
print(frase)
print(frase.strip())   #Recore los espacios que hay a los lados de una cadena.


# Eliminar variables.
year = 2021
print(year)
del year    # Elminar una variable.


# Comprobar variable vacía.
texto = "ff"

if len(texto) <= 0:     # Medir cuantos carácteres hay en una cadena de texto.
    print("La variable está vacía")
else:
    print("La variable tiene contenido: " + str(len(texto)) + " carácteres")


# Saber qué tipo y cuántos carácteres hay.
frase = "La vida es bella, pero apesta"
print("\n" + str(frase.find("vida")))


# Remplazar palabras en una cadena de texto.
nueva_frase = frase.replace("vida", "pinche vida")
print(nueva_frase)


# Procesar minusculas y mayusculas.
print("\n")
print(nombre)
print(nombre.lower())   # Converir a todas las letras en minusculas.
print(nombre.upper())   # Convertir a todas las letras en mayusculas.

