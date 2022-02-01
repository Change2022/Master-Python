# Fille: condicionales2.
# Purpose: Explicación de él uso de estructuras de selección múltiple.
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

if condicion:
    se ejecuta instruccion

    if condicion:
        se ejecuta instrucción con datos relacionados al if anterior
    else:
        se ejecutan otras instrucciones

else:
    se ejecutan otras instrucciones

 -------------------------------------------------

if condicion 1:
    se ejecuta instruccion
elif condicion 2:
    se ejecuta instruccion
elif condicion 3:
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

# Ejemplo 4 (Estructura de selección múltiple/ Elif)
print("##### EJEMPLO 4 #####\n")

dia = (int(input("¿Qué día numérico de la semana es?\n\nIngresa el número aquí: ")))

if dia == 1:
    print("\nHoy es Lunes.")
elif dia == 2:
    print("\nHoy es Martes.")
elif dia == 3:
    print("\nHoy es Miercoles.")
elif dia == 4:
    print("\nHoy es Jueves.")
elif dia == 5:
    print("\nHoy es Viernes.")
elif dia == 6:
    print("\nHoy es Sábado.")
elif dia == 7:
    print("\nHoy es Domingo.")
else:
    print("\nDato no valido.")


"""
La estructura de selección múltiple "ELIF", también conocida en otros lenguajes de programación como "Else If"
, es una estructura que se útiliza cuándo tenemos una variable que puede tener un valor distinto a causa
de una toma de decisión, sin la necesidad de generar múltiples anidaciones de resultados.

VENTAJAS:

** Se ocupan menos recursos del programa.
** Se generan menos hílos de procesamiento.
** Se lee más fácil el código.
** Se ve más limpio el código.

"""

