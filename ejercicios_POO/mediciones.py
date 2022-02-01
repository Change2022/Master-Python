# File: Ejercicio de práctica: Mediciones.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

print("\nSELECCIONA LA MEDICIÓN:\n\nYarda 1\nGalones 2")

eleccion = (int(input("\nElíge: ")))

while eleccion <= 0 or eleccion >= 3:
    print(f"\nElección no valida: [{eleccion}]\nRecuerda que solo se acepta el número 1 o 2.")
    eleccion = (int(input("\nVuelve a intentarlo: ")))


def yar():

    print("\n***** Has elegido la medición para yardas *****")
    yarda = (int(input("\n¿Cuántas yardas hay? : ")))

    pie = 3
    pulgada = 36

    print(f"\nHay [{yarda}] yardas : [{yarda * pie}] pies : [{yarda * pulgada}] Pulgadas")
    print("\nFin.")
    

def gal():
    print("\n***** Has elegido la medición para galones *****")

    galon = (int(input("\n¿Cuántos galones hay? : ")))

    cuarta = 4
    pinta = 6 
    taza = 16

    print(f"\nHay [{galon}] Galones : [{galon * cuarta}] Cuartas : [{galon * pinta}] Pintas : [{galon * taza}] Tazas")
    print("\nFin.")


if eleccion == 1:
    yar()
elif eleccion == 2:
    gal()

