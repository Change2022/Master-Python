# File: Excepciones en bucle.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

from datetime import *

def excepciones():

    try:
        año = int(input("Introduce el año en el que naciste: "))
        mes = int(input("Introduce el mes en el que naciste: "))
        dia = int(input("Introduce el día en el que naciste: "))
        
        actual = 2021
        expediente = []
       
        while dia < 0 or dia > 31:
            print(f"\nEl día es incorrecto: [{dia}], porfavor vuelve a introducirlo.")
            dia = int(input("Introduce el día en el que naciste: "))
            
        while mes < 0 or mes > 12:
            print(f"\nEl mes es incorrecto: [{mes}], porfavor vuelve a introducirlo.")
            mes = int(input("Introduce el mes en el que naciste: "))

        while año > actual or año < 1911:
            print(f"\nEl año es incorrecto: [{año}], porfavor vuelve a introducirlo.")
            año = int(input("Introduce el año en el que naciste: "))

        edad = (actual - año)
        fecha = (f"Tu fecha de nacimiento es: {dia} / {mes} / {año}")

        expediente.append(edad), expediente.append(fecha)

    except Exception as e:
        print("Ha ocurrido un error: ", type(e).__name__)

    else:
        print("\n***** DATOS VALIDOS *****")
        print(f"\nTu edad es de: {edad}\n{fecha}")

        print(f"\n\nExpediente:")
        for elementos in expediente:
            print("Dato: ", elementos)
        
        fch = datetime.now()
        print("\nHora de consulta: {}:{}:{}".format(fch.hour, fch.minute, fch.second))
        print("Fecha actual de la consulta: {}:{}:{}".format(fch.day, fch.month, fch.year))

    finally:
        print("\nFin de la consulta.")

excepciones()

