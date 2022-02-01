# File: Herencia entre objetos.
# Autor: Roberto Rico Sandoval.
# Version: 0.0.1

"""

Documentación
    - La herencia es una herramienta que permite compartir atributos y métodos entre diferentes clases
    y objetos de un mismo código.

    Teniendo en cuenta que se tendra una clase padre, que heredará a varias clases hijas, que entre sí
    todas tendrán similitudes y diferencias. 

    [super().__init()] = Método predeterminado en las librerías de Python, el cual, funciona para llamar y/o heredar a los
    atributos generado en un constructor de una clase padre. Es decir, son atributos heredados desde un constructor padre
    a un constructor hijo de una clase hija.

    NOTA: Como buena práctica, el constructor debe declarse como prioridad en el objeto, antes de los atributos públicos y
    privados, get y set, y métodos personalizados.
"""

import clases

persona = clases.Persona()     # Objeto sencillo.
persona.setNombre("Roberto")
persona.setApellidos("Rico Sandoval")
persona.setAltura(1.94)
persona.setEdad(23)

persona_informatico = clases.Informatico()   # Objeto con herencía.
persona_informatico.setNombre("Alan")
persona_informatico.setApellidos("Turing")

persona_tecRedes = clases.TecnicoRedes()     # Objeto con sobre-herencía.
persona_tecRedes.setNombre("Fabiruchis")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}\nAltura: {persona.getAltura()} M\nEdad: {persona.getEdad()} años")
print(persona.cagar())
print(persona.caminar())

print(f"\nEl informático es: {persona_informatico.getNombre()} {persona_informatico.getApellidos()}")
print(f"{persona_informatico.programar()}")
print(f"{persona_informatico.getLenguajes()}")
print(f"{persona_informatico.experiencia}")
print(f"{persona_informatico.cagar()}")

print(f"\n{persona_tecRedes.auditarRedes, persona_tecRedes.getNombre(), persona_tecRedes.getLenguajes()}")
print(f"{persona_tecRedes.cagar()}")

