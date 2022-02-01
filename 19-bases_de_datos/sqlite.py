# Fille: Conexión de base de datos.
# Autor: Roberto Rico Sandoval
# Version: v.0.0.1

"""
DOCUMENTACIÓN:

    - Importar módulo de bases de datos Sqlite3 (Para Python V.3.0, en adelante.)

    - Método [connect] = Conexión de base de datos... Utiliza un parámetro, para nombrar al archivo contenedor de la base de datos.
    Este archivo tiene una extensión .db (database / base de datos).

    - Método [close] = Se útiliza, para cerrrar y guardar los datos contenidos en el archivo de la base de datos.

    - Método [cursor] = Se utiliza para crear al cursor o consultante (buscador/search) de la base de datos.

    - Método [execute] = submétodo de [cursor()], se utiliza par generar ordenes de cunsulta al cursor.

    - Orden db [CREATE TABLA] = Crear tablas en sqlite.

    - Orden db [IF NOT EXIST] = Comparación, sino existe la tabla nombrada "x", entonces creala, sí ya existe, entonces no la
    vuelvas a crear.

    - Orden db [VARCHAR] = Orden para delimitar un campo en cuestión de carácteres.

    - Orden db [TEXT] = Orden para especificar que se trata de un campo con texto largo.

    - Orden db [INT] = Orden para delimitar un campo en cuestión de números.

    - Orden db [ INTEGER PRIMARY KEYAUTOINCREMENT not null] = Orden para especificar que el campo puede generar incrementos en 
    sus limites de carácteres o números sin generar errores de sintaxis.

    - Orden db [commit] = Para guardar cambios o ediciones en la base de datos.

    NOTA: La base de datos es un archivo en lenguaje binario que tiene un nombre, al mismo tiempo, tiene tablas con nombres.
    Estas tablas estan hechas por filas y columnas, en donde, hay campos o celdas que pueden contener valores.

    - Orden db [INSERT INTO tabla_nombre] = Oreden, para insertar nuevos valores en una tabla. Se rellenan los campos de la tabla
    basandonos en un parámetro de argumentos, en posición "x" de columnas creadas. En este ejmplo, se rellenan 4 argumentos, para
    4 columnas.

    - Orden db [SELECT] Orden para seleccionar alguna columna o fila de la tabla en la base de datos.

    - Orden db [FROM] Orden para seleccionar en especifico una tabla de la base de datos.

    - Orden db [*/ALL] Orden para seleccionar todos los campos (celdas) de una tabla.

    - Método [fetchall()] = Para convertir a los datos binarios de una tabla, en luenguaje de alto nivel, y mostrarlos en terminal.
    
    - Método [fetchone()] = Se utiliza para imprimir o llamar unicamente al primer registro o valor en una tabla. De esta forma,
    se deve volver hacer una consulta en el código [execute], para colocar el nombre del valor (campo) a consultar.

    - Orden db [DELETE FROM tabla_nombre] = Orden para eliminar todo el contenido de una tabla.

    - Método [executemany()] = Para insertar múltiples y nuevos valores a las tablas en la base de datos.

    - Orden db [Where / Donde] = Para condicionar alguna operación en una tabla de una base de datos.

    - Orden db [UPDATE] = Para actualizar el valor de una columna.

    - Orden db [SET / INSERTAR] = Para insertar y actualizar datos en la tabla.
"""

import sqlite3

# Conexión de base de datos.
conexion = sqlite3.connect("pruebas.db")    # NOMBRE DE LA BASE = pruebas.db

# Crear cursor o consultante de la base de datos.
cursor = conexion.cursor()
tabla2 = conexion.cursor()


# Crear tabla.
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT not null, "+
"Titulo VARCHAR(255), "+
"Descripción TEXT, "+
"Precio INT(255)"+
")")
# Se deben concadenar todos los campos o columnas creadas.
# La tabla se llama productos.
# Columnas: id, Titulo, Descripción, Precio.


# Crear tabla de segunda forma.
tabla2.execute("""CREATE TABLE IF NOT EXISTS tecnologia(
No INTEGER PRIMARY KEY AUTOINCREMENT not null,
Titulo VARCHAR(255),
Descripción TEXT, 
Precio INT(255)
)""")


# Insertar datos en la tabla de la base de datos.
# Se rellenan los campos o celdas de izquierda a derecha sobre la tabla.
conexion.execute("INSERT INTO productos VALUES (null, 'Producto', 'Descripción del prodcuto', 550)")

# Se guardan los cambios.
conexion.commit()


# Listar datos (Leer datos).
cursor.execute("SELECT * FROM productos")
print(f"\n{cursor}")                                # Se imprime un objeto, ya que, Python toma a las bases de datos como objetos.

productos = cursor.fetchall()                # Se imprime en terminal, el contenido de la tabla seleccionada.
print(f"\n{productos}\n")

for producto in productos:                   # Recorre las túplas generadas en la tabla.
    print(producto)

for producto in productos:                   # Recorre las túplas generadas en la tabla con parámetro indexado.
    print("\nNo:", producto[0])
    print("Nombre:", producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])

# Imprimir solamente el primer registro o valor de la tabla.
cursor.execute("SELECT Precio FROM productos")

producto = cursor.fetchone()
print(f"\nPrimer registro en la tabla: {producto}")

# Insertar muchos datos a la vez.
# Se guradan los datos a insertar en la tabla en una variable.
productosE = [
    ("WorkStation", "Condiciones optimas", 15000),
    ("SmartPhone", "Condiciones optimas", 5000),
    ("MotherBoard", "Condiciones optimas", 2000),
    ("PC Gamer", "Condiciones optimas", 18000)
]


tabla2.executemany("INSERT INTO tecnologia VALUES (null, ?,?,?)", productosE)
# Se guardan los cambios.
conexion.commit()

tabla2.execute("SELECT * FROM tecnologia")
print(f"\n{tabla2}")

for producto in tabla2:
    print("\nNo:", producto[0])
    print("Tipo:", producto[1])
    print("Condición:", producto[2])
    print("Precio:", producto[3])

print("\nImprimir solo varos mayores a $ 10,000")


tabla2.execute("SELECT * FROM tecnologia WHERE Precio >= 10000")

for producto in tabla2:
    print("\nNo:", producto[0])
    print("Tipo:", producto[1])
    print("Condición:", producto[2])
    print("Precio:", producto[3])

conexion.commit()

# Update / Actualizar.
tabla2.execute("UPDATE tecnologia SET Precio = 2350 WHERE Precio = 2000")
print(f"\n{tabla2}")

for producto in tabla2:
    print("\nNo:", producto[0])
    print("Tipo:", producto[1])
    print("Condición:", producto[2])
    print("Precio:", producto[3])

conexion.commit()

# Borrar registros en las tablas.
cursor.execute("DELETE FROM productos")

# Guardar cambios en la base.
conexion.commit()

# Cerrar conexión de la base de datos.
conexion.close()

{}