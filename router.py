from SRC.dispositivos.menu_dispositivos import menu_dispositivos
from SRC.dispositivos import dispositivos_modulo as dispositivos
from SRC.usuarios import usuarios


def menu_usuario(email_usuario):
    nombre_usuario = usuarios.usuario[email_usuario]["nombre"]

    while True:
        print(f"\n--- MENÚ USUARIO - Bienvenido {nombre_usuario} ---")
        print("1. Consultar mis datos personales")
        print("2. Consultar automatizaciones activas")
        print("3. Consultar mis dispositivos")
        print("4. Modificar configuración de mis dispositivos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios.buscar_usuario(email_usuario)
        elif opcion == "2":
            dispositivos.consultar_automatizaciones_activas()
        elif opcion == "3":
            dispositivos.listar_dispositivos_usuario(email_usuario)
        elif opcion == "4":
            dispositivos.modificar_configuracion_dispositivo(email_usuario)
        elif opcion == "5":
            print("👋 Sesión cerrada.")
            return
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")


def menu_admin(email_admin):
    """Menú exclusivo para vos (el administrador del sistema)"""
    nombre_usuario = usuarios.usuario[email_admin]["nombre"]

    while True:
        print(f"\n--- MENÚ ADMINISTRADOR - Bienvenido {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Gestión de dispositivos")
        print("3. Consultar mis dispositivos")
        print("4. Modificar configuración de mis dispositivos")
        print("5. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dispositivos.consultar_automatizaciones_activas()
        elif opcion == "2":
            menu_dispositivos(email_admin)
        elif opcion == "3":
            dispositivos.listar_dispositivos_usuario(email_admin)
        elif opcion == "4":
            dispositivos.modificar_configuracion_dispositivo(email_admin)
        elif opcion == "5":
            print("👋 Volviendo al menú de ingreso...")
            return
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")


def menu_principal(email_usuario):
    """Redirige al menú según el tipo de usuario"""
    datos_usuario = usuarios.usuario[email_usuario]
    rol = datos_usuario["categoria"]

    if rol == "administrador":
        menu_admin(email_usuario)
    else:
        menu_usuario(email_usuario)
