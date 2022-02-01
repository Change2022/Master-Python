# Fille: Operadores_logicos.
# Purpose: Explicación de él uso de operadores lógicos en la programación.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
Los operadores lógicos se pueden utilizar en conjunto con las tomas de decisión o cindiciones del programa, 
para obtener resultados más óptimo y más certero.

***** OPERADORES LÓGICOS *****

AND = Y (Y sí también...)
OR = O  (O sino...)
NOT = NO (NEGACIÓN)

-------------------------------------------------------

***** TABLA DE LA VERDAD DE LOS OPERADORES LÓGICOS *****

-- AND --

verdadero and verdadero = VERDADERO
falso and verdadero = FALSO
verdadero and falso = FALSO
falso and falso = FALSO

----------

-- OR --

verdadero or verdadero = VERDADERO
falso or verdadero = VERDADERO
verdadero or falso = VERDADERO
falso or falso = FALSO

----------

-- NOT --

NOT(true) = FALSE
NOT(false) = TRUE


"""

# Ejemplo 1
print("***** EJEMPLO 1 *****")


edad = (int(input("\n¿Cuál es tú edad?\n\nInserta aquí tu edad: ")))

if edad >= 18 and edad <= 65:
    print(f"\nTienes {edad} años. Eres mayor de edad, puedes trabajar.")
elif edad < 18:
    print(f"\nTienes {edad} años. Eres menor de edad, no puedes trabajar.")
else:
    print(f"\nTienes {edad} años. Eres demaciado grande de edad, no puedes trabajar.")



# Ejemplo 2
print("\n***** EJEMPLO 2 *****")

paises = input("\nMenciona a uno de los 3 paises que conforman el Tratado de Libre Comercio (TLC)\n\n")

if paises == "Mexico" or paises == "EUA" or paises == "Canada":
    print(f"\nCorrecto, {paises} es un pais que conforma el TLC.")
else:
    print(f"\nIncorrecto, {paises} no pertenece al tratado TLC.")

