from SRC.usuarios import usuarios
import router

def mostrar_menu_ingreso():
    print("\n--- INGRESO ---")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    return input("Seleccione una opción: ")

def menu_ingreso():
    print("Bienvenido al Sistema de Gestión")
    
    while True:
        opcion = mostrar_menu_ingreso()
        
        if opcion == "1":
            print("\n--- INICIO DE SESIÓN ---")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            exito = usuarios.iniciar_sesion(email, contraseña)
            if exito:
                print("Sesión iniciada correctamente.")
                router.menu_principal(email)
                
        elif opcion == "2":
            print("\n--- REGISTRO DE USUARIO ---")
            nombre = input("Nombre: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")

            print("Seleccione tipo de usuario:")
            print("1. Administrador")
            print("2. Usuario estándar")
            tipo_opcion = input("Ingrese opción (1-2): ")

            if tipo_opcion == "1":
                categoria = "administrador"
            elif tipo_opcion == "2":
                categoria = "usuario"
            else:
                print("Opción no válida. Se asignará usuario estándar por defecto.")
                categoria = "usuario"

            usuarios.registrar_usuario(nombre, email, contraseña, categoria)

        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")
