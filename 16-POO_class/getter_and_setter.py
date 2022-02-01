# File: Sacar y meter resultados por medio de get y set.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
DOCUMENTACIÓN:
    
    - [set] = Método predefinido en python, para cambiar el valor de un atributo en Python 3.
    - [get] = Método predefinido en python, para obtener o sacar el valor de un método relizado
              en un objeto o clase.

"""

# Definir clase (Molde para crear objetos).

class Coche:

    # Atributos o propiedades, que son caracteristícas del objeto "coche".
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 350
    caballaje = 500
    plazas = 2


    # Definir un método (Acción o función del objeto).

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10

    def getVelocidad(self):
        return self.velocidad   # Sacar el valor del atributo velocidad afuera del método.
    # Cierre o fin de la clase.


    # Modificar el valor de un atributo.

    def setColor(self, color):     # Cambiar el valor del atributo.
        self.color = color

    def getColor(self):            # Retornar el nuevo valor del atributo.
        return self.color

    def setModelo(self, modelo):   # Cambiar el valor del atributo.
        self.modelo = modelo

    def getModelo(self):           # Retornar el nuevo valor del atributo.
        return self.modelo


# Crear objeto o instanciar la clase.

coche = Coche()   # Objeto creado

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

# Verificación de objeto creado.
print(f"\n{coche}")

# Impresión de atributo o de múltiuples atributos.
print(coche.marca)
print(coche.marca,  coche.getModelo(), coche.getColor())

# Ejercicio.

print("\nVelocidad actual:", coche.getVelocidad(), "Km*h")

# Llamar o invocar un método.
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actualizada:", coche.getVelocidad(), "Km*h")

coche.frenar()

print("Velocidad actualizada:", coche.getVelocidad(), "Km*h")


