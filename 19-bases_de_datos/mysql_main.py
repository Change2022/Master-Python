# Fille: SQL en Python.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 22/07/2021

# Importar SQL en Python.
import mysql.connector
from mysql.connector import cursor

contador = 0
juegos = [('Minecraft', 'JavaEdition', 100),
          ('Forza', '5', 800),
          ('Halo', 'Infiniti', 1000),
          ('Free Fire', 'V.5.12', 0)]
          
#Conexión de la base de datos.
database = mysql.connector.connect(
    host ="localhost",    # Nombre del servidor de alojamiento.  
    user ="root",         # Usuario administrador de la base de datos.
    passwd ="",           # Contraseña de la cuanta Admin.
    database ="pro_python"    # Nombre de la base de datos que se va ha estar ocupando.
)


# Comprobar que la conexión con WAMP es correcta con SQL.
print(database)

# Crar consultor para la base de datos en SQL.
cursore = database.cursor(buffered=True)

# Crear tabla en la base de datos.
cursore.execute("CREATE DATABASE IF NOT EXISTS pro_python")

# Consultar los datos incluidos en una base de datos.
cursore.execute("SHOW DATABASES")


# Comprobar todas las bases de datos en existencía.
for bd in cursore:
    print(f"base de datos: {bd}")

# Crear tablas en la base de datos.
cursore.execute("""
CREATE TABLE IF NOT EXISTS videogames(
    No int(10) auto_increment not null,
    Tipo varchar(40) not null,
    Genero varchar(40) not null,
    Precio float(6,2) not null,
    CONSTRAINT pk_game PRIMARY KEY(No) 
)
""")

# Mostrar tablas disponibles en la base de datos.
cursore.execute("SHOW TABLES")

for tabla in cursore:
    print(f"\n{tabla}")

#Se comenta esta parte del código, para que no se inserten más datos sobre la base de datos.
"""
# Insertar datos
cursore.execute("INSERT INTO videogames VALUES(null, 'COD', 'MW3', 1200)")

# Guardar datos, para que se guarden los datos ingresados.
database.commit()

# Insertar múltiples datos
cursore.executemany("INSERT INTO videogames VALUES(null, %s, %s, %s)", juegos)
"""

# Seleccionar columnas a mostrar de la tabla.
cursore.execute("SELECT * FROM videogames")
resultado = cursore.fetchall()

print("\n*** Todos los juegos ***")
for juegos in resultado:
    print(juegos)

print("\n*** Precios ***")
for juegos in resultado:
    contador += 1
    print(f"{contador}) {juegos[1]} ${juegos[3]}")

# Solo datos inferiores a 10000.
cursore.execute("SELECT * FROM videogames WHERE precio >= 500")
resultado = cursore.fetchall()

print("\n*** Todos los juegos ***")
for juegos in resultado:
    print(juegos)

print("\n*** Precios ***")
for juegos in resultado:
    contador += 1
    print(f"{contador}) {juegos[1]} ${juegos[3]}")


# Borrar datos en la base de datos.
cursore.execute("DELETE FROM videogames WHERE Tipo = 'Halo'")
# Guardar y ejecutar cambios en la base de datos.
database.commit()

# Mostrar los elementos borrados.
print("Elementos borrados : ", cursore.rowcount)

# Actualizar datos.
cursore.execute("UPDATE videogames SET genero = 'V.15.18' WHERE Tipo = 'Free Fire'")
# Guardar y ejecutar cambios en la base de datos.
database.commit()
# Mostrar los elementos actualizados.
print("Elementos actualizados : ", cursore.rowcount)

