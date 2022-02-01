# File: listas_multidimensionales.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

"""
LISTAS MULTIDIMENSIONALES:

    Las listas multidimnsionales son colecciones de datos anidadas dentro de otra colección de datos o son
    listas anidadas en otras listas.
"""

print("\n********** LISTADOS DE CONTACTOS **********")

contactos = [
    ["Roberto","robertoricosandoval@gmail.com"],
    ["Alejandra","alejandraromero@teztraño.com"],
    ["Vida","vida@quiero.com"]
    ]

print(contactos)
print("\n" + contactos[1][1])  # Acceder a una dimensión de la lista.

print("")
for contacto in contactos:
    print(contacto[0])

print("")
for elemento in contactos:
    print(elemento[1])

print("")
for contacto in contactos:
    for completo in contacto:
        print(completo)
    print("\n")              

print("")
for contacto in contactos:
    for completo in contacto:
        if contacto.index(completo) == 0:
            print("Nombre: " + completo)
        else:
            print("Email: " + completo)
    print("\n")

