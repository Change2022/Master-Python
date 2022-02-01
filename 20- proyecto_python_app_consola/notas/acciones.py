# Fille: app de consola con python / Módulo de acciones > notas.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 03/10/2021

import notas.nota as modeloNota

class Acciones:

    def crearNota(self, usuario):
        print(f"\nOk! [{usuario[1]}] Vamos a crear una nueva nota.")

        titulo = input("\nIntroduce el titulo de la nota aquí: ")
        descripcion = input("\nIntroduce el contenido de la nota aquí: ")

        nota = modeloNota.Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota correctamente de: {usuario[1]}")

