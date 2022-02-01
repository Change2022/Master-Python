# File: Clases de objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

class Persona:
    
    """
    nombre
    apellidos
    altura
    edad
    """

    # Sacar datos.

    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    # Meter datos.

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    # Métodos (Acciones posibles) de la clase Persona.

    def hablar(self):
        return "Ahora puedo hablar."

    def caminar(self):
        return "Ahora puedo caminar."

    def dormir(self):
        return "Ahora puedo dormir."
    
    def cagar(self):
        return "Ahora puedo cagar."

# Clase hija heredadora.

class Informatico(Persona):
    """
    programacion
    experiencia
    """

    def __init__(self):
        self.programacion = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    # Este es un método que extrae los atributos y valores generados en el constructor.
    def getLenguajes(self):
        return self.programacion

    # Incluir nuevos atributos al objeto/clase.
    def setAprenderNuevoLenguaje(self, programacion):
        self.programacion = programacion
        return self.programacion

    def programar(self):
        return "Ahora estoy programando."

    def repararPC(self):
        return "He reparado tu ordenador."

# Clase hija con sobrre herencia.

class TecnicoRedes(Informatico):
    
    def __init__(self): 

        super().__init__()    # Se llama al constructor de la clase padre.
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red."

