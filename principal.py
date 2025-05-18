# principal.py
import usuarios
import dispositivos

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
    print("5. Volver al menú principal")
    return input("Seleccione una opción: ")

def menu_usuarios(email_actual):
    """Menú de gestión de usuarios para usuarios autenticados"""
    while True:
        opcion = mostrar_menu_usuarios()
        
        if opcion == "1":
            # Buscar usuario
            print("\n--- BÚSQUEDA DE USUARIO ---")
            email = input("Email a buscar: ")
            usuarios.buscar_usuario(email)
        
        elif opcion == "2":
            # Listar usuarios
            print("\n--- LISTA DE USUARIOS ---")
            usuarios.listar_usuarios()
        
        elif opcion == "3":
            # Cambiar contraseña
            print("\n--- CAMBIAR CONTRASEÑA ---")
            contraseña_actual = input("Contraseña actual: ")
            if usuarios.verificar_credenciales(email_actual, contraseña_actual):
                nueva_contraseña = input("Nueva contraseña: ")
                usuarios.cambiar_contraseña(email_actual, nueva_contraseña)
            else:
                print("Error: Contraseña incorrecta.")
        
        elif opcion == "4":
            # Eliminar mi cuenta
            print("\n--- ELIMINAR MI CUENTA ---")
            contraseña = input("Ingrese su contraseña para confirmar: ")
            if usuarios.eliminar_usuario(email_actual, contraseña):
                print("Su cuenta ha sido eliminada. Volviendo al menú de ingreso...")
                return True  # Indica que el usuario ha sido eliminado
        
        elif opcion == "5":
            # Volver al menú principal
            return False  # Indica que el usuario no ha sido eliminado
        
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")
        
        # Pausa antes de volver al menú
        input("\nPresione Enter para continuar...")

def menu_dispositivos(email_actual):
    """Menú de gestión de dispositivos para usuarios autenticados"""
    while True:
        opcion = mostrar_menu_dispositivos()

        if opcion == "1":
            # Registrar dispositivo
            print("\n--- REGISTRO DE DISPOSITIVO ---")
            nombre_del_dispositivo = input("Ingrese el nombre de dispositivo: ")
            tipo_de_dispositivo = input("Ingrese el tipo de dispositivo: ")
            modelo = input("Ingrese el modelo de su dispositivo: ")
            
            # Registramos con el email del usuario actual
            dispositivos.registrar_dispositivo(nombre_del_dispositivo, tipo_de_dispositivo, modelo, email_actual)
        
        elif opcion == "2":
            # Eliminar dispositivo
            print("\n--- ELIMINAR DISPOSITIVO ---")
            nombre_del_dispositivo = input("Ingrese el nombre del dispositivo a eliminar: ")
            contraseña = input("Confirme su contraseña: ")
            
            # Verificar credenciales antes de eliminar
            if usuarios.verificar_credenciales(email_actual, contraseña):
                dispositivos.eliminar_dispositivo(nombre_del_dispositivo, email_actual)
            else:
                print("No se puede eliminar: contraseña incorrecta.")

        elif opcion == "3":
            # Buscar dispositivo
            print("\n--- BÚSQUEDA DE DISPOSITIVO ---")
            nombre_del_dispositivo = input("Ingrese el nombre del dispositivo a buscar: ")
            dispositivos.buscar_dispositivo(nombre_del_dispositivo)

        elif opcion == "4":
            # Listar dispositivos
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
            # Volver al menú principal
            return

        else:
            print("\nOpción no válida. Intente nuevamente.")
            
        # Pausa antes de volver al menú
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