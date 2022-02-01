# File: Estructura constructora de objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
DOCUMENTACIÓN:

    - Conocido como [Constructor] o [Método maestro], o [Método padre], es un método inicial o que se ejecutará primero ante todos
    los métodos contenidos en el algoritmo. Este método, puede interactuar de forma directa con los demás métodos incluidos en el
    algoritmo.

    Nota: Esto es un módulo y cualquier archivo puede ser un módulo.

    [__variable/atributo] = Se definen atributos privados del objeto, para darle mayor seguridad a la información que este contenga.
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
    num = 0

    # Propiedad pública.
    publico = "Esto es un atributo público."

    # Propiedad privada.
    __privada = "Esto es un atributo privado." 


    # Definir un método (Acción o función del objeto).

    def acelerar(self):
        self.velocidad += 10

    def frenar(self):
        self.velocidad -= 10

    def getVelocidad(self):
        return self.velocidad   # Sacar el valor del atributo velocidad afuera del método.

        # Modificar el valor de un atributo.

    def setColor(self, color):     # Cambiar el valor del atributo.
        self.color = color

    def getColor(self):            # Retornar el nuevo valor del atributo.
        return self.color

    def setModelo(self, modelo):   # Cambiar el valor del atributo.
        self.modelo = modelo

    def getModelo(self):           # Retornar el nuevo valor del atributo.
        return self.modelo

    def setMarca(self, marca):     # Cambiar el valor del atributo.
        self.marca = marca

    def getMarca(self):
        return self.marca          # Retornar el nuevo valor del atributo.

    def setNum(self, num):         # Cambiar el valor del atributo.
        self.num = num

    def getNum(self):
        return self.num          # Retornar el nuevo valor del atributo.


    def getInfo(self):

        info = "***** información del objeto *****"
        info += "\nColor: " + self.getColor()
        info += "\nMarca: " + self.getMarca()
        info += "\nModelo: " + self.getModelo()
        info += "\nvelocidad: " + str(self.getVelocidad())  # Actualización constante de una variable
        info += "\nNúmero de objeto: " + str(self.getNum())

        return info  # Retornar el valor de la variable afuera del bloque del método.
        
    def getInfo2(self):
        # Impresión de datos en una línea.
        infox = (f"***** información del objeto *****\nColor: {self.getColor()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nvelocidad: {str(self.getVelocidad())}\nNúmero de objeto: {str(self.getNum())}")

        return infox # Retornar el valor de la variable afuera del bloque del método.

    # Constructor.
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas, num):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas
        self.num = num

    def getPrivado(self):    # Método get con retorno [return], para obtener el valor del atributo privado.
        return self.__privada

