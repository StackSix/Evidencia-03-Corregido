from SRC.usuarios import usuarios
from SRC.dispositivos import dispositivos_modulo as dispositivos
from SRC.menus.menu_dispositivos import menu_dispositivos

def modificar_rol_usuario(email_admin):
    email_a_modificar = input("Ingrese el email del usuario a modificar: ")
    nuevo_rol = input("Ingrese el nuevo rol (usuario/administrador): ").lower()
    usuarios.modificar_rol(email_a_modificar, nuevo_rol, email_admin)

def consultar_automatizaciones_activas():
    print("\n--- AUTOMATIZACIONES ACTIVAS ---")
    dispositivos.consultar_automatizaciones_activas()

def menu_administrador(email_admin):
    nombre_usuario = usuarios.usuario[email_admin]["nombre"]

    while True:
        print(f"\n--- MENÚ ADMINISTRADOR - Bienvenido {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Gestión de dispositivos")
        print("3. Modificar rol de un usuario")
        print("4. Consultar mis dispositivos")
        print("5. Modificar configuración de mis dispositivos")
        print("6. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_automatizaciones_activas()
        elif opcion == "2":
            menu_dispositivos(email_admin)
        elif opcion == "3":
            modificar_rol_usuario(email_admin)
        elif opcion == "4":
            dispositivos.listar_dispositivos_usuario(email_admin)
        elif opcion == "5":
            dispositivos.modificar_configuracion_dispositivo(email_admin)
        elif opcion == "6":
            print("👋 Cerrando sesión...")
            break
        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")
