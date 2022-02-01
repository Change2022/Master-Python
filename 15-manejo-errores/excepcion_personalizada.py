# File: Ezcepción personalizada.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
DOCUMENTACIÓN:

    - [raise / elevar] = Función predeterminada para generar excepciones personalizadas.
"""

name = input("Introduce aquí tú nombre: ")
age = int(input("Introduce aquí tu edad: "))

try:
    if age < 5 or age > 110:
        raise ValueError("La edad introducida no es real.")
    elif len(name) <= 1:
        raise ValueError("El nombre no es correcto o no esta completo.")
    else:
        print(f"\nBienveido: {name}\nTu edad es de: {age}")
except ValueError:
    print("Introduce los datos correctamente.")
except Exception as e:
    print("Existe un error", e)

