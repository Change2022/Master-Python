# File: Funciones anidadas.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Generar una función que anide a otras 2 funciones externas.
"""
def getNombre(nombre=None):
    texto = f"\nEl nombre es: {nombre}"
    return texto

def getApellidos(apellido=None):
    texto = f"Los apellidos son: {apellido}"
    return texto

def devuelvetodo(nombre, apellido):
    texto = getNombre(nombre) + "\n" + getApellidos(apellido)
    return texto

# Impresión por separado de las funciones.
print(getNombre("Roberto"))
print(getApellidos("Rico Sandoval"))

#Impresión en una sola línea de las impresiones por separado.
print(getNombre("Roberto"), "\n", getApellidos("Rico Sandoval"))

# Impresión de la función anidada.
print(devuelvetodo("Roberto", "Rico Sandoval"))

"""
[return], retorna los valores hacía afuera de la función.
"""

