from SRC.usuarios import usuarios

def mostrar_menu_usuarios(rol):
    print("\n--- SISTEMA DE GESTIÓN DE USUARIOS ---")
    print("1. Buscar usuario")
    print("2. Listar usuarios")
    print("3. Cambiar contraseña")
    print("4. Eliminar mi cuenta")
    print("5. Volver al menú anterior")
    return input("Seleccione una opción: ")


def menu_usuarios(email_actual):
    """Menú de gestión de usuarios"""
    rol = usuarios.usuario[email_actual]["categoria"]

    while True:
        opcion = mostrar_menu_usuarios(rol)

        if opcion == "1":
            email = input("Email a buscar: ")
            usuarios.buscar_usuario(email)

        elif opcion == "2":
            usuarios.listar_usuarios()

        elif opcion == "3":
            contraseña_actual = input("Contraseña actual: ")
            if usuarios.verificar_credenciales(email_actual, contraseña_actual):
                nueva_contraseña = input("Nueva contraseña: ")
                usuarios.cambiar_contraseña(email_actual, nueva_contraseña)
            else:
                print("❌ Contraseña incorrecta.")

        elif opcion == "4":
            contraseña = input("Ingrese su contraseña para confirmar: ")
            if usuarios.eliminar_usuario(email_actual, contraseña):
                print("Cuenta eliminada. Volviendo al ingreso...")
                return True

        elif opcion == "5":
            return False

        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")