# File: Herramienta PIB.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

import random
from datetime import *

lista = []
datos_secun = []

print("\n***** BIENVENIDO AL SISTEMA DE CÁLCULO DE PIB *****")

def depo():

    print("\n-- EXPORTACIONES NETAS --")
    
    exportaciones = random.uniform(140, 160)
    print(f"\nExportaciones = {round(exportaciones,2)} M")
    importaciones = random.uniform(140, 160)
    print(f"Importaciones = {round(importaciones,2)} M")

    exportaciones_netas = (exportaciones - importaciones)
    print("\nExportaciones netas:", round(exportaciones_netas,2), "M")

    datos_secun.append(round(exportaciones,2)), datos_secun.append(round(importaciones,2)), datos_secun.append(round(exportaciones_netas,2))

    return round(exportaciones_netas,2)


def consumo():
    
    print("\n_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/\n\n-- CONSUMOS --\n")

    precio = random.uniform(5, 60)
    print(f"Precio: {round(precio,2)} M")
    cantidad = random.uniform(5, 60)
    print(f"Cantidad: {round(cantidad,2)} M")

    consumo_total = (precio * cantidad)
    print("\nConsumo total:", round(consumo_total,2), "M")

    datos_secun.append(round(precio,2)), datos_secun.append(round(cantidad,2)), datos_secun.append(round(consumo_total,2))

    return round(consumo_total,2)


def inversion():
    
    print("\n_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/\n\n-- INVERSIONES --\n")

    precio = random.uniform(5, 60)
    print(f"Precio: {round(precio,2)} M")
    cantidad = random.uniform(5, 60)
    print(f"Cantidad: {round(cantidad,2)} M")

    inversion_total = (precio * cantidad)
    print("\nInversión total:", round(inversion_total,2), "M")

    datos_secun.append(round(precio,2)), datos_secun.append(round(cantidad,2)), datos_secun.append(round(inversion_total,2))

    return round(inversion_total,2)


def compras_nacionales():

    print("\n*******************************************\n\n-- COMPRAS NACIONALES --\n")

    precio = random.uniform(5, 60)
    print(f"Precio: {round(precio,2)} M")
    cantidad = random.uniform(5, 60)
    print(f"Cantidad: {round(cantidad,2)} M")

    compras_nacionales_total = (precio * cantidad)
    print("\nTotal de comrpas nacionales:", round(compras_nacionales_total,2), "M")

    datos_secun.append(round(precio,2)), datos_secun.append(round(cantidad,2)), datos_secun.append(round(compras_nacionales_total,2))
    
    return round(compras_nacionales_total,2)


def PIB():
    try:

        year1 = random.randrange(2011, 2021)
        year = random.randrange(2011, 2021)
        habitantes = random.randrange(100, 200)

        if year1 == year or year == year1:
                raise ValueError("\nError de equivalencias.")

    except ValueError:
        print("\nLo siento, el sistema trata de valorar el mismo año. Vuelve a intentarlo.")

    else:
        pib_neto = (compras_nacionales() + inversion() + consumo() + depo())
        print("\n_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/\n\n-- PIB NETO --\n")
        print(f"El PIB NETO del año [{year}] es de:", round(pib_neto,2), "M\n")
        print(f"PIB PERCAPITAL del año {year} es de: {round(pib_neto / habitantes,2)} M")

        pib_real = (compras_nacionales() + inversion() + consumo() + depo())
        print("\n_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/\n\n-- PIB REAL --\n")
                
        print(f"El PIB REAL del año [{year1}] es de:", round(pib_real,2), "M\n")
        print(f"PIB PERCAPITAL del año {year1} es de: {round(pib_real / habitantes,2)} M")

        lista.append(year), lista.append(year1), lista.append(round(pib_neto,2)), lista.append(round(pib_real,2)), lista.append(habitantes)
        lista.append(round(pib_neto / habitantes,2)), lista.append(round(pib_neto / habitantes,2))

        print("\n*******************************************\n\n-- DATOS --\n")
        print(f"Año: {lista[0]} - Cantidad_PIB_neto: {lista[2]} M - cantidad_PIB_per_Capital: {lista[5]} M")
        print(f"Año: {lista[1]} - Cantidad_PIB_real: {lista[3]} M - cantidad_PIB_per_Capital: {lista[5]} M")
        print(f"\nNum. Habitantes en la ciudad: [{lista[4]}] M")

        print("\n*******************************************\n\n-- DATOS SECUNDARIOS --\n")
        
        for date in range(1):
            print(f"{year}: COMPRAS NACIONALES: Precio = {datos_secun[0]}M - Cantidad = {datos_secun[1]}M - Totales = {datos_secun[2]}M")
            print(f"{year}: INVERSIONES: Precio = {datos_secun[3]}M - Cantidad = {datos_secun[4]}M - Totales = {datos_secun[5]}M")
            print(f"{year}: CONSUMOS: Precio = {datos_secun[6]}M - Cantidad = {datos_secun[7]}M - Totales = {datos_secun[8]}M")
            print(f"{year}: EXPORTACIONES: Exportaciones = {datos_secun[9]}M - Importaciones = {datos_secun[10]}M - Exportaciones netas = {datos_secun[11]}M")
            print("\n-------------------------------------")
            print(f"{year1}: COMPRAS NACIONALES: Precio = {datos_secun[12]}M - Cantidad = {datos_secun[13]}M - Totales = {datos_secun[14]}M")
            print(f"{year1}: INVERSIONES: Precio = {datos_secun[15]}M - Cantidad = {datos_secun[16]}M - Totales = {datos_secun[17]}M")
            print(f"{year1}: CONSUMOS: Precio = {datos_secun[18]}M - Cantidad = {datos_secun[19]}M - Totales = {datos_secun[20]}M")
            print(f"{year1}: EXPORTACIONES: Exportaciones = {datos_secun[21]}M - Importaciones = {datos_secun[22]}M - Exportaciones netas = {datos_secun[23]}M")


    finally:
        print("\n*******************************************\n\n-- FECHA DE CONSULTA --\n")
        fecha = datetime.now()
        print("\nHora de consulta: {}:{}:{}".format(fecha.hour, fecha.minute, fecha.second))
        print("Fecha actual de la consulta: {}:{}:{}".format(fecha.day, fecha.month, fecha.year))

    try:
        print("\n*******************************************\n\n-- DEFLACTOR --\n")
        eleccion = (int(input(f"\nElige de que año quieres saber la deflacción:\n{year} = Tecla 1\n{year1} = Tecla 2\nelección: ")))

        while eleccion < 1 or eleccion > 2:
            print("\nElegiste una opción incorrecta, vuelve a intentarlo, porfavor.")
            eleccion = (int(input(f"\nElige de que año quieres saber la deflacción:\n{year} = Tecla 1\n{year1} = Tecla 2\nelección: ")))

    except ValueError:
        print("Ocurrio un error, no se aceptan letras ni signos, solo números. Vuelve a intentarlo.")
        
    else: 
            
        if eleccion == 1:
            base = (pib_neto/pib_neto * 100)
            deflactor = (pib_neto / pib_real * base)
            final = (base - deflactor)
            print(f"\nEl deflactor del año {year} es: {round(final,2)}%")

        elif eleccion == 2:
            base = (pib_real/pib_real * 100)
            deflactor = (pib_real / pib_neto * base)
            final = (base - deflactor)
            print(f"\nEl deflactor del año {year1} es: {round(final,2)}%")
    
    finally:
        print("Fin de la iteración.")
PIB()
        
