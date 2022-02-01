# File: Estructura constructora de objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1


# Importación de clase en forma de módulo.
from coche import Coche 


# Definición de objeto. 
# Parámetros esperados en el constructor __init__

lista = []
auto = 0

for auto in range(0, 4):
    auto += 1

lista.append(auto)


carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4, 1)
carro2 = Coche("Verde", "Seat", "Panda", 240, 200, 4, 2)
carro3 = Coche("Azul", "Citroen", "Xara", 100, 180, 4, 3)
carro4 = Coche("Rojo", "Mercedes", "Clase-A", 350, 400, 4, 4)


# Verificación de creación de objeto.
print(carro)


# Sacar el valor de un atributo.
print(carro.velocidad)
print(carro.color)


# Invocar un método dentro del módulo importado.
print(carro.getVelocidad())
print(carro.getColor())


# Imprimir todos los datos del objeto.
print("\n"+carro.getInfo())
print("\n"+carro2.getInfo())
print("\n"+carro3.getInfo())
print("\n"+carro4.getInfo())


print(f"\nEl total de objetos (autos) es igual a: {lista}")


# Imprimir todos los datos del objeto en una sola línea.
print("\n"+carro.getInfo2())
print("\n"+carro2.getInfo2())
print("\n"+carro3.getInfo2())
print("\n"+carro4.getInfo2())


print(f"\nEl total de objetos (autos) es igual a: {lista}")


# Tipado de un objeto (Tipo o clase de objeto)

if type(carro3) == Coche:
    print(f"\nEste es un objeto de clase Coche.")
else:
    print("!No es un objeto¡")


# Visibildad de atributos (Públicos y privados).
print(f"\n{carro.publico}")         # Invocar atributos públicos.
print(f"\n{carro.getPrivado()}")    # Invocar atributos privados.

