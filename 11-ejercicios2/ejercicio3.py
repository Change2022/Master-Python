# File: Ejecicio 3.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
EJERCICIO 3:

    - Programar un comprobador para una variables str vacía.
    - Rellenar la variable.
    - Mostrar el contenido en mayusculas.
    - Verificar cuantos elementos (letras) hay en el string.
"""

texto = ""

if len(texto.strip()) <= 0:
    print("\nEl string está vacío.")

texto = (input("\nDigita aquí una frase que te guste - "))

while len(texto.strip()) <= 0:
    print("\nEl string está vacío.")
    texto = (input("\nDigita aquí una frase que te guste - "))


print(f"\nTú dices: {texto.upper()}")
print(f"\nTú frase tiene: {len(texto.strip())} (carácteres)")
