# Fille: app de consola con python / Módulo de acciones.
# Autor: Roberto Rico Sandoval.
# Versión: V.0.1
# Fecha de creación: 16/09/2021

# Creación de módulo por objeto (Clase).
# Importación del paquete usuarios> Registros.
# "Modelo", pára modelo de datos.

import personas.usuario as modelo

class Acciones:

    def registro(self):
        
        print("\n¡Ok! Vamos a registrarte en el sistema.")

        nombre = input("\nIngresa tu nombre: ")
        apellidos = input("Ingresa tus apellidos: ")
        email = input("Ingresa tu email: ")
        password = input("Ingresa tu contraseña: ") 

        # Creación de nuevoi usuario en objeto.
        nuevo = modelo.Usuario(nombre, apellidos, email, password)   # Esto es un objeto de la clase Usuario.
        insertar = nuevo.registrar() 

        if insertar[0] >= 1:
            print(f"\nNuevo usuario [{insertar[1].nombre} {insertar[1].apellidos}].\nTe has registrado con el email [{insertar[1].email}]")
        else:
            print("No te has registrado correctamente.")


    def log(self):
        
        print("\nVale, accede al sistema.")

        try:
            email = input("\nIngresa tu email: ")
            password = input("Ingresa tu contraseña: ")

            usuario = modelo.Usuario("", "", email, password)

            login = usuario.identificar()
            

            if email == login[3]:
                print(f"\nBienvenido {login[1]}\n. Te has registrado el día {login[5]}")
                self.accionSecundaria(login)
        
        except Exception as e:
            print(type(e))
            print(type(e),__name__)
            print("Login incorrecto.")

    def accionSecundaria(self, usuario):
        
        print ("""\n
        Acciones posibles:

        1) Crear notas (Tecla 1).
        2) Mostrar notas (Tecla 2).
        3) Eliminar notas (Tecla 3).
        4) Salir del sistema (Tecla 4).
        """)

        accion = int(input("\nNum: Acción - "))

        while accion <= 0 or accion >= 5:
            print(f"Has seleccionado un dato incorrecto [{accion}], vuelve a intentarlo.")
            accion = int(input("\nNum: Acción - "))

        if accion == 1:
            print("\nSe va ha crear una nota nueva.")
            self.accionSecundaria(usuario)

        elif accion == 2:
            print("\nSe van ha mostrar todas las notas existentes.")
            self.accionSecundaria(usuario)

        elif accion == 3:
            print("\nSe va ha eliminar alguna nota.")
            self.accionSecundaria(usuario)

        elif accion == 4:
            print(f"\nHas salido del sistema. Nos vemos en la proxima [{usuario[1]} {usuario[2]}].")
            exit()

