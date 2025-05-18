# ingreso.py
import usuarios

def mostrar_menu_ingreso():
    print("\n--- SISTEMA DE GESTIÓN - INGRESO ---")
    print("1. Iniciar sesión")
    print("2. Registrar usuario")
    print("3. Salir")
    return input("Seleccione una opción: ")

def menu_ingreso():
    """Menú inicial de ingreso al sistema"""
    print("Bienvenido al Sistema de Gestión")
    
    while True:
        opcion = mostrar_menu_ingreso()
        
        if opcion == "1":
            # Iniciar sesión
            print("\n--- INICIO DE SESIÓN ---")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            exito = usuarios.iniciar_sesion(email, contraseña)
            if exito:
                print("Sesión iniciada correctamente.")
                # Importamos principal aquí para evitar importaciones circulares
                import principal
                principal.menu_principal(email)
        
        elif opcion == "2":
            # Registrar usuario
            print("\n--- REGISTRO DE USUARIO ---")
            nombre = input("Nombre: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            usuarios.registrar_usuario(nombre, email, contraseña)
        
        elif opcion == "3":
            # Salir
            print("\n¡Gracias por usar nuestro Sistema de Gestión!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")
        
        # Pausa antes de volver al menú
        input("\nPresione Enter para continuar...")