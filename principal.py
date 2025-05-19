# principal.py
import usuarios
import dispositivos_modulo as dispositivos

def mostrar_menu_principal(nombre_usuario):
    print(f"\n--- MENÚ PRINCIPAL - Bienvenido {nombre_usuario} ---")
    print("1. Gestión de Usuarios")
    print("2. Gestión de Dispositivos")
    print("3. Cerrar sesión")
    return input("Seleccione una opción: ")

def mostrar_menu_usuarios():
    print("\n--- SISTEMA DE GESTIÓN DE USUARIOS ---")
    print("1. Buscar usuario")
    print("2. Listar usuarios")
    print("3. Cambiar contraseña")
    print("4. Eliminar mi cuenta")
    print("5. Volver al menú principal")
    return input("Seleccione una opción: ")

def mostrar_menu_dispositivos():
    print("\n--- SISTEMA DE GESTIÓN DE DISPOSITIVOS ---")
    print("1. Registrar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Buscar dispositivo")
    print("4. Listar todos los dispositivos")
    print("5. Activar modo ahorro de cámaras")
    print("6. Desactivar modo ahorro de cámaras")
    print("7. Volver al menú principal")
    return input("Seleccione una opción: ")


def menu_usuarios(email_actual):
    """Menú de gestión de usuarios para usuarios autenticados"""
    while True:
        opcion = mostrar_menu_usuarios()
        
        if opcion == "1":
            print("\n--- BÚSQUEDA DE USUARIO ---")
            email = input("Email a buscar: ")
            usuarios.buscar_usuario(email)
        
        elif opcion == "2":
            print("\n--- LISTA DE USUARIOS ---")
            usuarios.listar_usuarios()
        
        elif opcion == "3":
            print("\n--- CAMBIAR CONTRASEÑA ---")
            contraseña_actual = input("Contraseña actual: ")
            if usuarios.verificar_credenciales(email_actual, contraseña_actual):
                nueva_contraseña = input("Nueva contraseña: ")
                usuarios.cambiar_contraseña(email_actual, nueva_contraseña)
            else:
                print("Error: Contraseña incorrecta.")
        
        elif opcion == "4":
            print("\n--- ELIMINAR MI CUENTA ---")
            contraseña = input("Ingrese su contraseña para confirmar: ")
            if usuarios.eliminar_usuario(email_actual, contraseña):
                print("Su cuenta ha sido eliminada. Volviendo al menú de ingreso...")
                return True
        
        elif opcion == "5":
            return False  
        
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")
        input("\nPresione Enter para continuar...")

def menu_dispositivos(email_actual):
    """Menú de gestión de dispositivos para usuarios autenticados"""
    while True:
        opcion = mostrar_menu_dispositivos()

        if opcion == "1":
            print("\n--- REGISTRO DE DISPOSITIVO ---")
            
            nombre_del_dispositivo = input("Ingrese el nombre de dispositivo: ")
            print("\nSeleccione el tipo de dispositivo:")
            print("1. Cámara de seguridad")
            print("2. Sensor de movimiento")
            tipo_opcion = input("Opción: ")

            if tipo_opcion == "1":
                tipo_de_dispositivo = "cámara de seguridad"
            elif tipo_opcion == "2":
                tipo_de_dispositivo = "sensor de movimiento"
            else:
                print("Opción no válida. Cancelando registro.")
                continue

            modelo = input("Ingrese el modelo de su dispositivo: ")
            dispositivos.registrar_dispositivo(nombre_del_dispositivo, tipo_de_dispositivo, modelo, email_actual)

        elif opcion == "2":
            print("\n--- ELIMINAR DISPOSITIVO ---")
            nombre_del_dispositivo = input("Ingrese el nombre del dispositivo a eliminar: ")
            contraseña = input("Confirme su contraseña: ")

            if usuarios.verificar_credenciales(email_actual, contraseña):
                dispositivos.eliminar_dispositivo(nombre_del_dispositivo, email_actual)
            else:
                print("No se puede eliminar: contraseña incorrecta.")

        elif opcion == "3":
            print("\n--- BÚSQUEDA DE DISPOSITIVO ---")
            nombre_del_dispositivo = input("Ingrese el nombre del dispositivo a buscar: ")
            dispositivos.buscar_dispositivo(nombre_del_dispositivo)

        elif opcion == "4":
            print("\n--- LISTA DE DISPOSITIVOS ---")
            print("1. Mostrar todos los dispositivos")
            print("2. Mostrar solo mis dispositivos")
            sub_opcion = input("Seleccione una opción: ")

            if sub_opcion == "1":
                dispositivos.listar_dispositivos()
            elif sub_opcion == "2":
                dispositivos.listar_dispositivos_usuario(email_actual)
            else:
                print("Opción no válida.")

        elif opcion == "5":
            print("\n--- ACTIVAR MODO AHORRO DE CÁMARAS ---")
            dispositivos.activar_modo_ahorro(email_actual)

        elif opcion == "6":
            print("\n--- DESACTIVAR MODO AHORRO DE CÁMARAS ---")
            dispositivos.desactivar_modo_ahorro(email_actual)

        elif opcion == "7":
            return

        else:
            print("\nOpción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


def menu_principal(email_usuario):
    """Menú principal que se muestra después de iniciar sesión"""
    nombre_usuario = usuarios.usuario[email_usuario]["nombre"]
    
    while True:
        opcion = mostrar_menu_principal(nombre_usuario)
        
        if opcion == "1":
            # Gestión de usuarios
            cuenta_eliminada = menu_usuarios(email_usuario)
            if cuenta_eliminada:
                return  # Volver al menú de ingreso si la cuenta fue eliminada
                
        elif opcion == "2":
            # Gestión de dispositivos
            menu_dispositivos(email_usuario)
            
        elif opcion == "3":
            # Cerrar sesión
            print("\nCerrando sesión...")
            return
            
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")