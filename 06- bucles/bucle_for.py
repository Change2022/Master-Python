# Fille: bucle_for.
# Purpose: Explicación del bucle for.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
FOR

for variable in elemento iterable: #(listas, tuplas, diccionarios, rangos... etc.)
    BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado = 0

for contandor in range(0, 10):
    contador += 1
    print("Soy el número: " + str(contador))

    resultado += contador 


print(f"\nEl RESULTADO es: {resultado}")

# Ejemplo de tablas de multiplicación.

print(f"\n\n---MULTIPLICACIONES---")

numeroM = (float(input("\n¿Qué número vas a múltiplicar por 10? - ")))

if numeroM < 1:
    numeroM = 1

print(f"\n#### TABLA DE MÚLTIPLICAR DEL {numeroM} ####\n")

for numeroC in range(1, 11):

    if numeroM >= 100:
        print("No se pueden procesar números mayores o iguales a 100 :( ")
        break
    
    print(f"{numeroM} x {numeroC} = {numeroM * numeroC}")
else:
    print("\nLa tabla de múltiplicar a finalizado.")

