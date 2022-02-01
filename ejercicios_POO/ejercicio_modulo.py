# File: Ejercicio de práctica: Programación Orientada a Objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""
CRITERIOS:

    - Define una clase.
    - Crea un objeto.
    - Crea un metódo constructor con 5 atributos de inicio.
    - Verifica que se haya creado correctamente el objeto.
    - Crea 3 objetos más.
    - 5 atributos en construcción.
"""

import random 

class Tortugona:

    comida = "pizza"
    correr = random.randrange(5, 15)

    def __init__(self, nombre, colorBanda, arma, peso, altura):
        
        self.nombre = nombre
        self.colorBanda = colorBanda
        self.arma = arma
        self.peso = peso
        self.altura = altura

    def setComida(self, comida):
        self.comida = comida

    def getComida(self):
        return self.comida

    def correrChido(self):
        return self.correr

    def getDocu(self):

        docu = "///// Datos de la tortuga ninja /////"
        docu += "\nNombre: " + self.nombre
        docu += "\nColor de banda: " + self.colorBanda
        docu += "\nTipo de arma: " + self.arma
        docu += "\nPeso: " + str(self.peso)
        docu += "\nAltura: " + str(self.altura)

        return docu

