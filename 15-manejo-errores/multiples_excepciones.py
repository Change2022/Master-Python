# File: Múltiples errores posibles en un código.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

# Múltiples excepciones.

"""
- DOCUMENTACIÓN:

    [except Exception as e] = Esta orden o comando, incluye el identificar y notificar al desarrollador
    o usuario, el tipo de error por medio de una cadena de texto personalizada.

    Se captura el error, imprime e identifica por medio de la ejecución [type(variable).__name__], 
    en donde...

    - [Type / Tipo] = Tipo de dato (str, int. float.., etc.)
    - [Variable] = El tipo de dato se va a almacenar en una variable.
    - [__name__] = Identificador del tipo de error presentado (ValueError, TypeError, IOError, KeyError... etc.)
"""

try:

    num = float(input("Coloca aquí el número a elevar al cuadrado: "))
    print(f"El cuadrado de este número es: {round(num*num,2)}")

#except ValueError:                 # Manera 1
    #print("Dato incorrecto.")

except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)   # Manera 2


