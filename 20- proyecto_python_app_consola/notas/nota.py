# Fille: app de consola con python / Modelo de notas.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 03/10/2021

"""
COMANDOS SQL:

    - NOW() = [Creación actomatica del dato fecha]
"""

import personas.conexion as conexion

connect = conexion.conexion()
baseDeDatos = connect[0]
search = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo, descripcion):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):

        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)
        
        # sql = consulta u acción en la base de datos / nota = valores a utilizar en la consulta.
        search.execute(sql, nota)
        baseDeDatos.commit()

        # Retornar el número de filas afectadas.
        return [search.rowcount, self]

