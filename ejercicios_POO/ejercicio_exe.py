# File: Ejercicio de práctica: Programación Orientada a Objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

from ejercicio_modulo import Tortugona

tortugona1 = Tortugona("Donatello", "Morado", "Ken-do", 80, 195)
tortugona2 = Tortugona("Miguel Ángel", "Naranja", "Nunchakus", 90, 190)
tortugona3 = Tortugona("Rafael", "Rojo", "Sai", 83, 170)
tortugona4 = Tortugona("Leonardo", "Azul", "Espadas", 78, 180)

print(tortugona1)
print(tortugona2)
print(tortugona3)
print(tortugona4)

print(f"\nLa tortuga ninja {tortugona2.nombre}, tiene de arma {tortugona2.arma}.")
print(f"La tortuga ninja {tortugona4.nombre}, tiene un peso de: {tortugona2.peso} Kg.")

print(f"\nLa comida preferida de las tortugas ninjas es la {tortugona1.getComida()}")
print(f"La tortuga {tortugona2.nombre}, puede correr {tortugona2.correrChido()} KMh")

print(f"\n{tortugona1.getDocu()}")
print(f"\n{tortugona2.getDocu()}")
print(f"\n{tortugona3.getDocu()}")
print(f"\n{tortugona4.getDocu()}")

if tortugona1.peso > tortugona2.peso and tortugona1.peso > tortugona3.peso and tortugona1.peso > tortugona4.peso:
    print(f"\nLa tortuga ninja {tortugona1.nombre} es la más obesa, no mms, bajale a las caguamongas pizzas. ¡rey TKM!")

elif tortugona2.peso > tortugona1.peso and tortugona2.peso > tortugona3.peso and tortugona2.peso > tortugona4.peso:
    print(f"\nLa tortuga ninja {tortugona2.nombre} es la más obesa, no mms, bajale a las caguamongas pizzas. ¡rey TKM!")

elif tortugona3.peso > tortugona1.peso and tortugona3.peso > tortugona2.peso and tortugona3.peso > tortugona4.peso:
    print(f"\nLa tortuga ninja {tortugona3.nombre} es la más obesa, no mms, bajale a las caguamongas pizzas. ¡rey TKM!")

else:
    print(f"\nLa tortuga ninja {tortugona4.nombre} es la más obesa, no mms, bajale a las caguamongas pizzas. ¡rey TKM!")

