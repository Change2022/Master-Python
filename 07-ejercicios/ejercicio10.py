# File: ejercicio 10.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
CRITERIOS:

    1-. Generar la calificación de 15 alumnos.
    2-. Verificar cuales alumnos aprobaron y cuales reprobaron.
"""

import random

alumno = 0
aprobados = 0
reprobados = 0

lista = []

while alumno <= 14:

    num_random = random.uniform(0.0, 10.0)

    alumno += 1
    print(f"\nEl alumno {alumno} tiene por calificación {round(num_random,1)}")
    
    if num_random < 6.0:
        print(f"\nEl alumno [{alumno}] ha reprobado ")
        lista.append(round(num_random,1))
    
    elif num_random <= 6.9 and num_random >= 6.5:
        print(f"\nEl alumno [{alumno}] tiene por calificación {round(num_random,1)} ha aprobado, su calificación incremento a 7.0")
        lista.append(round(num_random,1))

    elif num_random <= 7.9 and num_random >= 7.5:
        print(f"\nEl alumno [{alumno}] tiene por calificación {round(num_random,1)} ha aprobado, su calificación incremento a 8.0")
        lista.append(round(num_random,1))

    elif num_random <= 8.9 and num_random >= 8.5:
        print(f"\nEl alumno [{alumno}] tiene por calificación {round(num_random,1)} ha aprobado, su calificación incremento a 9.0")
        lista.append(round(num_random,1))

    elif num_random <= 9.9 and num_random >= 9.5:
        print(f"\nEl alumno [{alumno}] tiene por calificación {round(num_random,1)} ha aprobado, su calificación incremento a 10.0")
        lista.append(round(num_random,1))
    
    else:
        print(f"\nEl alumno [{alumno}] ha aprobado con calificación de [{round(num_random,1)}]")
        lista.append(round(num_random,1))

    if num_random >= 6.0:
        aprobados += 1
    else:
        reprobados += 1

    print("\n--------------------")        

print("\n")
print("Las calificaciones son:", lista)

print(f"\nHay {reprobados} alumnos reprobas.\nHay {aprobados} alumnos aprobados.")

