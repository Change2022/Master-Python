# File: Curiosidades sobre las funciones.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

# Es recomendable definir a las funciones, hasarriba de la cabecera del código.
def mi_funcion(nombre):   
    print("Hola que tal " + nombre)

# Se puede iprimir directamente las instrucciones de una función o se pueden retornar/return los valores de las intrucciones en función.
def segunda_funcion(appellido):
    return ("Segunda función: " + apellido)

nombre = "Roberto"
apellido = "Rico Sandoval"

print(f"\nHola {nombre}, bienvenido.")

mi_funcion(nombre)
print(segunda_funcion(apellido))

