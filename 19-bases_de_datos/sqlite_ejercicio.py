# Fille: Ejercicio de bases de datos ligeras en SQLite.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 19/07/2021

import sqlite3

base = sqlite3.connect("tecno_base.db")

consultor1 = base.cursor()
consultor2 = base.cursor()

consultor1.execute("""CREATE TABLE IF NOT EXISTS producto_E(
No INTEGER PRIMARY KEY AUTOINCREMENT not null,
nameProduct TEXT
)""")

consultor2.execute("""CREATE TABLE IF NOT EXISTS datos_E(
Caracteristicas TEXT,
Precio INT(255)
)""")

consultor1.execute("SELECT * FROM producto_E")
print(f"\n{consultor1}")

consultor2.execute("SELECT * FROM datos_E")
print(f"{consultor2}")

inventario = [
    ("Comida china"),
    ("Comida mexicana"),
    ("Comida indú"),
    ("Comida americána")
]

consultor1.executemany("INSERT INTO producto_E VALUES (null,?)", inventario)

productos_E = consultor1.fetchall()
print(f"\n{productos_E}")

datos_E = consultor2.fetchall()
print(f"{datos_E}")

base.commit()

