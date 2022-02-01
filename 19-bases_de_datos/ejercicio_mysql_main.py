# Fille: SQL en Python (Ejercicio).
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 05/07/2021

import mysql.connector
from mysql.connector import cursor


contador = 0
cereales = [('Bolitas', 'Chocolate', '500g', 60),
            ('Arroz pequeño', 'Chocolate', '500g', 50),
            ('Frutitas', 'Tutifruti', '500g', 55),
            ('Hojuelas de maíz', 'Azucar', '500g', 45)]

try:

    database = mysql.connector.connect(
        host ="localhost",      
        user ="root",         
        passwd ="",           
        database ="practica_1")

except:
    print("No se a podido conectar la base de datos :'(")
else:
    print(f"Base de datos conectada: {database}")

search = (database.cursor(buffered = True))

search.execute("CREATE DATABASE IF NOT EXISTS practica_1")
search.execute("SHOW DATABASES")


print("")
for bases in search:
    print(f"base de datos: {bases}")


search.execute("""
CREATE TABLE IF NOT EXISTS Seriales2(
    No int(10) auto_increment not null,
    Tipo varchar(40) not null,
    Sabor varchar(40) not null,
    Tamallo varchar(40) not null,
    Precio float(6,2) not null,
    CONSTRAINT pk_game PRIMARY KEY(No) 
)""")


database.commit()
search.execute("SHOW TABLES")


print("")
for tabla in search:
    print(f"Tabla existente: {tabla}")

"""
search.execute("INSERT INTO Seriales2 VALUES(null, 'Bolita de arroz', 'Poo', '500g', 50)")
database.commit()

search.executemany("INSERT INTO Seriales2 VALUES(null, %s, %s, %s, %s)", cereales)
"""

search.execute("SELECT * FROM Seriales2")
resultadoBusqueda = search.fetchall()
search.execute("SELECT * FROM Seriales2")
primerResultado = search.fetchone()


print(f"\nPrimer registro en la tabla: {primerResultado}")
print("\n*** Todos los ceareales en la tabla ***")
for cereal in resultadoBusqueda:
    print(cereal)


# Solo precios.
print("\n*** Precio del cereal ***")
for cereal in resultadoBusqueda:
    contador += 1
    print(f"{contador}) {cereal[1]} : ${cereal[4]}")


# Solo datos inferiores o iguales a 50.
search.execute("SELECT * FROM Seriales2 WHERE Precio <= 50")
resultadoCondi = search.fetchall()


print("\n*** Solo cereales con precio inferior a $50 ***")
for cereal in resultadoCondi:
    print(cereal)


# Solo precios.
print("\n*** Precio del cereal (Solo cereales con precio inferior a $50) ***")
for cereal in resultadoCondi:
    contador += 1
    print(f"{contador}) {cereal[1]} : ${cereal[4]}")


if search.execute("DELETE FROM Seriales2 WHERE Tipo = 'Frutitas'"):
    print("\nElementos borrados : ", search.rowcount)
    database.commit()
else:
    print(f"\nNo se han borrado elementos en: {database}")


if search.execute("UPDATE Seriales2 SET Sabor = 'Fresita' WHERE Tipo = 'Arroz pequeño'"):
    print("Elementos actualizados : ", search.rowcount)
    database.commit()
else:
    print(f"\nNo se han actualizado elementos en la base de datos: {database}")

