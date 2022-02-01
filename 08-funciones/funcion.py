# File: función.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
FUNCIONES:

    Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto, que pueden
    reutilizarse invocando a la función tantas veces sea necesario.

    La palabra reservada en Python [def], se utiliza para "DEFINIR" o declarar una función.

    EJEMPLO:

    #Así se declara una función.

    def nombreDeMiFunción(parámetros):
        Bloque de código / Conjunto de instrucciones

    ----------------------------------------------------

    #Así se invoca una función.

    nombreDeMiFunción(mi_parámetro)
"""

# Ejemplo 1.
print("\n##### EJEMPLO 1 #####\n")

# Aquí se define la función.
def nombres():
    print("Roberto")
    print("Jaime")
    print("Erick")
    print("Samuel")
    print("Alejandra")

# Aquí se invoca a la función.
nombres()

"""
FUNCIONES CON PARÁMETRO DEFINIDO:

    Un parámetro para una función, es el tomar datos externos al bloque de programación de una función
    como pueden ser datos de algúna variable global, y estos datos externos, pueden interactuar dentro
    del bloque de instrucciones de la funciuón.
"""

# Ejemplo 2.
print("\n##### EJEMPLO 2 #####\n")

def mostrarNombre(nombre, edad):

    print(f"\nTu nombre es: {nombre}")
    print(f"Tu edad es de: {edad}")

    if edad >= 90:
        print("\nEres demaciado grande.")
    elif edad >= 18:
        print("\nEres mayor de edad.")
    else:
        print("\nEres menor de edad")

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

mostrarNombre(nombre, edad)

