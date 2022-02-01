# File: Capturar excepciones y errores.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
    - Se utiliza la estructura "Try / Finally", para generar opciones de ejecución ante la iteración de errores suseptibles en
      en código.

      [Try / Intentar] = Intentar en este error...
      [Except / Excepto] = Mensaje u operación excepcional para el error.
      [Finally / Finalmente] = Se utiliza como buena práctica, para dejar en claro lque aquí termina el código.

      Está estructura también puede incluir una instrucción de tipo [else], para ejecutar un mensaje opcional a except.
"""

try:
    name = input("¿Cúal es tu nombre? ")
    print(name)

    if len(name) > 1:
        nombre_usuario = "El nombre es: " + name

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, inserte bien el nombre.")
else:
    print("\nTodo a funcionado correctamente.")
finally:
    print("Fin de la iteración.")

