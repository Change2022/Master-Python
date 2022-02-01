# File: Módulos o líbrerias en Python.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
MÓDULOS:

    - Son funciones programadas, que pueden ser reutilizadas. En python existe una cantidad inmensa de módulos
    , estos módulos pueden ser descargados por internet, estar cargados por defecto en el lenguaje o
    podemos crear nuestros módulos: https://docs.python.org/3/py-modindex.html
"""

# Importar módulos hechos por mí.
 
import mis_modulos                        # Manera 1 de importar un módulo.
from mis_modulos import holaMundo         # Manera 2 de importar sólo una función del módulo.
from mis_modulos import *                 # Manera 3 de importar todas las funciones del módulo.

print(mis_modulos.holaMundo("Roberto"))   # M1
print(mis_modulos.porcentaje())           # M1
 
print(holaMundo("Roberto"))               # M2
print(porcentaje())                       # M3
 
