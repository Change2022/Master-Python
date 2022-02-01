# File: Package/paqueterias en python 3.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
PAQUETES / PACKAGE:

    - Los paquetes, son un conjunto de módulos o librerías que sirven, para exportas tantos módulos posibles
    sea dentro de un proyecto.

    [__init__]: Se requiere este tipo de archivo dentro del proyecto, para especificar al lenguaje que
    se trata de una paquetería.
    Este archivo debe estar almacenado dentro de una carpeta interna dentro del proyecto principal, en donde, tambíen se guardarán
    los módulos de la paquetería.

    [from and import]: (From / Desde : import / Importado) está función predeterminada se útiliza, para exportar paquetes y demás recursos
    del lenguaje.

    [__pycache__]: Es una carpeta que genera Python 3, la momento de generar módulos y paquetes, su función
    se simplemente servir como memoria cáche.
"""

print("\n**PROBANDO PAQUETES**")

from mis_paquetes import pruebas       # Importar módulos de la paquetería por separado.
from mis_paquetes import herramientas

from mis_paquetes import pruebas, herramientas   # Importar módulos de la paquetería en conjunto.

# Acceso al módulo e impresíon de funciones dentro del módulo.
pruebas.prueba()
herramientas.nombreCompleto("Roberto Jaime", "Rico Sandoval")

