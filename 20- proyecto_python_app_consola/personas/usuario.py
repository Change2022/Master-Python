# Fille: app de consola con python / Gestor de bases de datos.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 16/09/2021

"""
Paquete y modulación de python, para refactorizar el código.
"""

import datetime  # Módulo para ingresar fechas.
import hashlib

from mysql.connector import connect   # Para cifrado de contraseñas.
import personas.conexion as conexion   # Alias conexión.

conect = conexion.conexion()
baseDeDatos = conect[0]     # Llamar al índice [0/baseDeDatos].
search =  conect[1]     # Llamar al índice [1/cursor_de_la_base_de_datos].


class Usuario:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password


    def registrar(self):

        fecha = datetime.datetime.now()   # Para ingresar la fecha del día de hoy.

        # cifrado de contraseña.
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))   # Decodifica el atributo en bit's.


        R_sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        User = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:

            search.execute(R_sql, User)
            baseDeDatos.commit()

            resultado = [search.rowcount, self]

        except:
            resultado = [0, self]
            print("\nError en el correo electrónico o contraseña.")

        return resultado

    def identificar(self):

        # Consulta para verificar si existe el usuario en la base de datos.
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # cifrado de contraseña.
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))   # Decodifica el atributo en bit's.

        # Datos para la consulta.
        usuario = (self.email, cifrado.hexdigest())

        search.execute(sql, usuario)
        resultado = search.fetchone()

        return resultado

