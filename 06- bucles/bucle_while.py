# Fille: bucle_while.
# Purpose: Explicación del bucle while.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
# BUCLE WHILE

Es una estructura de control qwue itera o repite la ejecución de una serie de instrucciones tantas veces
como sea necesario, hasta que deje de cumplirse la condición.

#### EJEMPLO ####

while condición:
    bloque de instrucciones
    actualización de contador

"""

contador = 1
contador2 = 1

coma = str(0)

while contador <= 100:
    print(f"Voy en el número {contador}")
    contador += 1

print("\n-----------\n")

while contador2 <= 100:
    coma = coma + ", " + str(contador2)
    contador2 += 1

print(coma)

# Ejemplo 2

print("\n#### EJEMPLO: TABLA DE MÚLTIPLICAR ####\n")

contador3 = 1
numeroM = (float(input("¿Qué número deseas múltiplicar hasta 10? - ")))

if numeroM < 1:
    numeroM = 1

print(f"\nTabla del {numeroM}: \n")

while contador3 <= 10:
    print(f"{numeroM} x {contador3} = {numeroM * contador3}")
    contador3 += 1
else:
    print("\n## FIN ##")

