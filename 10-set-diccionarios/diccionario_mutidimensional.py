# File: diccionario mutidimensional.
# By: Roberto Rico Sandoval.
# Version: 0.1.py

Contactos = [
    {
        "Nombre" : "Roberto",
        "Edad" : 22

    },
    {
        "Nombre" : "Alejandra",
        "Edad" : 24
    },
    {
        "Nombre" : "Samuel",
        "Edad" : 20
    }
]

print(Contactos)

print("")
print(Contactos[0]["Nombre"])   # Mostrar el índice sobre una palabra clave

Contactos[2]["Nombre"] = "Nahúm"   # cambiar un valor del diccionarió.
print(Contactos[2]["Nombre"])

print("\nListado de contactos.\n")

for contacto in Contactos:
    print(f"Nombre del contacto: {contacto['Nombre']}")
    print(f"Edad del contacto: {contacto['Edad']}")
    print("-----------------------------------------------")

