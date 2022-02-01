# File: Módulos incluidos en python 3.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

# Módulo de fechas

import datetime
import math
import random

print(datetime.date.today())

fecha = datetime.datetime.now()
print(fecha)
print(fecha.year)
print(fecha.month)
print(fecha.day)

fecha_personal = fecha.strftime("%d/%m/%Y --- %H:%M:%S")
print(f"Fecha personalizada: {fecha_personal}")

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

# Módulo de matemáticas.

num = int(input("\nElige un número, para sacar su raíz cuadrada: "))
print(f"La raíz cuadrada de {num} es: {round(math.sqrt(num),2)}")

pi = math.pi
print(f"\nNúmero pi: {pi}")

print(f"\nRedondear a la baja: {math.floor(6.49589 )}\nRedondear a la alta: {math.ceil(6.49589 )}")

# Módulo para números random/aleatorios.

# Némeros enteros (int) aleatorios.
print(f"\nNúmero aleatorio entre 0 y 100: {random.randint(0, 100)}")

# Némeros enteros (flooat) decimales.
print(f"\nNúmero aleatorio entre 0 y 100: {random.uniform(0, 100)}")

