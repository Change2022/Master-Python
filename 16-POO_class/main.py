# File: Programación Orientada a Objatos (Clases).
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
- DOCUMENTACIÓN.

    [CLASS / CLASES]: Las clases son "moldes" dode podemos crear y alamacenar varios objetos de un mismo tipo.

    En este ejemplo, trataremos con una clase llamada "coche", que van a generar objetos de un mismo tipo con
    caracteristícas similares.

    [class / clase] = Palabra reservada de Python o función predeterminada, para definir o declarar una clase en el algoritmo.
    [coche] = Nombramiento de la clase.

    Nota: Los atributos en un objeto, se ven identificados por medio de variables.

    [Methods / Métodos] = Los métodos, son acciones que puede realizar un objeto. Se puede decir que son funciones imperativas
    o secuenciales dentro del objeto.

    [Def / Definir] = palabra reservada de Python, para invocar o declarar funciones y/o objetos.
    
    [self / "En él mismo"] = Palabra reservada, para retornar e intercambiar atributos dentro de los objetos de una misma clase.
    Que al mismo tiempo, se pueden ver reflejados en los métodos del objeto. Se utiliza un "." (Punto), como Key (Lllave).
    para acceder a los atributos del objeto.
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

# Crear objeto o instanciar la clase.

coche = Coche()   # Objeto creado

# Verificación de objeto creado.
print(f"\n{coche}")      

# Impresión de atributo o de múltiuples atributos.
print(coche.marca)
print(coche.marca, coche.color)

# Ejercicio.

print("\nVelocidad actual:", coche.velocidad, "Km*h")

# Llamar o invocar un método.
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Velocidad actualizada:", coche.velocidad, "Km*h")

coche.frenar()

print("Velocidad actualizada:", coche.velocidad, "Km*h")

