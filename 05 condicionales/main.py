# Fille: condicionales.
# Purpose: Explicación de la toma de decisiones en un algoritmo programático.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
1- Condicional IF/Sí
2- Condicional Else/Entonces

Sí (if) se cumple esta condición:
    Se ejecuta este bloquie de instrucciones

Sí no (Else):
    Se ejecutan otras instrucciones

-------------------------------------------------

if condicion:
    se ejecuta instruccion
else:
    se ejecutan otras instrucciones

-------------------------------------------------

*****OPERADORES DE COMPARACIÓN*****

 Operador de asignación de valores (=)
 Operador de comparación de valores (==)
 No es igual o dato diferente (!=)
 Menor que (<)
 Mayor que (>)
 Menor o igual que (<=)
 Mayor o igual que (>=)


"""

# Ejemplo 1
print("##### EJEMPLO 1 #####\n")

color = "azul"
color1 = "verde"

if color == "azul":
    print("El color es AZUL")
else:
    print("El color no es AZUL")

if color1 == "azul":
    print("El color es AZUL")
else:
    print("El color no es AZUL\n")


color2 = input("¿Qué color se obtiene al mezclar el color AZUl con el color AMARILLO? - ")

if color2 == "verde":
    print("\nEs correcto, el color obtenido de la mezcla es VERDE.")
else:
    print("\nEse color es incorrecto.")


# Ejemplo 2
print("\n##### EJEMPLO 2 #####\n")

year = (int(input("¿En que año estamos? - ")))

if year >= 2021:
    print(f"\nEstamos en el año {year}")
else:
    print(f"\nEstamos en el año {year}. estamos en el pasado, antes del 2021.")


# Ejemplo 3
print("\n##### EJEMPLO 3 #####\n")

nombre = (input("¿Cuá es tú nombre? - "))
ciudad = (input("¿Cuá es tú ciudad en donde vives? - "))
continente = (input("¿Cuá es el continente donde vives? - "))
edad = (int(input("¿Cuántos años tienes? - ")))

mayoriaDeEdad = 18

if edad >= mayoriaDeEdad:
    print(f"\nTú edad es de {edad}.\n{nombre}, es mayor de edad")

    # IF ANINADO.

    if continente == "america":
        print(f"{nombre}, es Americanol, vive en {ciudad}")
    else:
        print(f"{nombre}, no es americano.")

else:
    print(f"\nTú edad es de {edad}.\n{nombre}, no es mayor de edad.")


"""
¿Cuándo utilizar un IF anidado?

R. Cuando se tienen 2 estructuras IF seguidas o en secuencia y que comparten datos iterables cómo variables
o valores de datos que se relacionan.

VENTAJAS:

** Se ocupan menos recursos por parte del programa.
** Se vuelve menos pesado el programa.
** Se agiliza el proceso.

NOTA: No es recomendable utilizar más de 3 IF anidados en el programa, ya que, puede ocasionar retrasos y 
errores en las respuestas del programa

"""

