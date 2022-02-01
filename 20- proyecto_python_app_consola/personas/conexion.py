# Fille: app de consola con python / Gestor de bases de datos (Refactorización a la conexión de la base de datos).
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 36/09/2021

import mysql.connector

def conexion():

    try:
        database = mysql.connector.connect(

        host = "localhost",
        user = "root",
        passwd = "",
        database = "app_python_consola",
        port = 3306
        )

        # print(database) / Para verificar que la base de datos funciona.

        search = database.cursor(buffered= True)

        # Índcie 0 = Creación y conexión con la base de datos / Índice 1 = Buscardor o consultor.
        return [database, search]

    except:
        print("No lograste conectar la base de datos.")

    