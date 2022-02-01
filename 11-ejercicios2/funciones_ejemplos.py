# File: Ejecicio de funciones.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

# Funciones con impresión directa.

def funcion1():

    variable1 = 18
    variable2 = 10.25

    variable3 = (variable1 + variable2)

    print("\n##### Función con impresión directa #####")
    print(f"\nEl resultado de la suma es: {variable3}")

funcion1()


# Funciones con retorno/return.

nada = None
print(type(nada))

def funcion2(nombre=None, edad=None):
    
    print(f"\nTú nombre es: {nombre}\n{nombre}: Tú tienes {edad} años")

    variable1 = 189
    variable2 = 2685.347
    variable3 = (variable1 + variable2)

    return str(variable1) + "\n" + str(variable3)

print (funcion2("Roberto", 22))


def funcion3():
    pais = "\nMéxico"
    return pais

print(funcion3())

