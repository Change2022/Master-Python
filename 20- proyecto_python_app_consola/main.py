# Fille: app de consola con python.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 12/09/2021


"""
Creación de app de consola con las tecnologías de Python 3 y SQL.

    1- Crear un asistente.
    2- Crear un servicio de loggin y registro.
    3- Crear y conectar una base de datos.
    4- Crear y guardar usuarios en la base de datos.
    5- ID o credencial del usuario.

    6- FUNCIONALIDADES:
        Crear notas.
        Mostrar notas.
        Eliminar notas.

    7- Refactorización por paquete y módulos.
    8- Captura y excepciones de errores.
    9- Cifrado de contraseñas.
    ---------------------------------------------------------------------------------------

    DOCUMENTACIÓN:

        - Comentarios cortos en SQL [--]
        - Comentarios largos en SQL [/**/]

        - Sustituciones = [%s] (Sustituye los datos esperados por argumentos en variales o atributos).
        - Comando as, para generar abreviaciones de un paquete o módulo importado.
        
    Sección de KEYS (Llaves privadas).

        - PRIMARY KEY (llave primaria): Comado de SQL que permite dstinguir una fila dentro de muchas. Al igual, no permite que se
        repitan datos del mismo valor en la columna. No se admiten campos vacíos. Solo se permite una sola llave primaria por tabla.

        - UNIQUE KEY (Llave única): Comado de SQL que contiene las mismas caracteristícas del comando PRIMARY KEY, a diferencia que,
        este campo si puede estar vacío, puede haber más de una llave de este tipo en la tabla, no permite la repetición de datos.
        Por jerarquía, es inferior a PRIMARY KEY.

        - FOREIGN KEY (Llave foránea): Son comandos de SQL que permiten relacionar tablas y columnas de una misma base de datos.
        Se utiliza el comando [REFERENCES], para terminar y guardar la relación entre tablas. Ejemplo:

        mi_llave_foranea FOREIGN KEY(nombre_de_mi_columna_a_relacionar) REFERENCES nombre_de_la_tabla_a_relacionar(Columna_a_relacioanr)

    Sección de motores (ENGINE) o gestores de bases de datos:

        - InnoDB: Es el motor de bases de datos que contiene MySQL por defecto, este se tiene que almacenar en una variable cuando se
        construya el algoritmo. Ejemplo:

        Motor = InnoDB;

    ---------------------------------------------------------------------------------------

    Librería haslib.

    Descripción: Sirve, para cifrar y decodificar datos almacenados en una variable.

    [haslib] = Llave primaria.
    [sha256] = Método de cifrado.
    [encode("utf8")] = Función, para convertir a bit's una sección de datos dentro de una variable.
    [hexdigest()] = Método que devuelve a la base de datos los datos convertidos en bit's.

"""

# Importación de paquete y módulo.
from personas import acciones

print("""
Acciones disponibles:

    - 1) Registro.
    - 2) Login.
""")

# Creación de objeto y conexión con el módulo y objeto que almacena las funciones.
hacer = acciones.Acciones()

accion = input("¿Qué acción quieres hacer? - ")

while accion !=  "1" and accion != "2" and accion != "Registro" and accion != "Login":
    print(f"\nHas ingresado un dato erroneo [{accion}]. Vuelve a intentarlo.")
    accion = input("¿Qué acción quieres hacer? - ")

if accion == "1" or accion == "Registro":
    hacer.registro()

elif accion == "2" or accion == "Login":
    hacer.log()

