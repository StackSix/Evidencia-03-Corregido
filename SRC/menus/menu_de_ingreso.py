from SRC.usuarios import usuarios
from router import menu_admin, menu_usuario  # importar desde router

def menu_ingreso():
    while True:
        print("\n--- INGRESO ---")
        print("1. Iniciar sesión")
        print("2. Registrarse como usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            categoria = usuarios.iniciar_sesion(email, contraseña)
            
            if categoria == "administrador":
                menu_admin(email)  # se usa el menú desde router.py
            elif categoria == "usuario":
                menu_usuario(email)
            else:
                print("❌ Inicio de sesión fallido.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            usuarios.registrar_usuario(nombre, email, contraseña, categoria="usuario")

        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intente nuevamente.")
