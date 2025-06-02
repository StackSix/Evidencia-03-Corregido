from SRC.dispositivos.menu_dispositivos import menu_dispositivos
from SRC.dispositivos import dispositivos_modulo as dispositivos  # si lo usás en admin
from SRC.usuarios import usuarios
from SRC.usuarios.menu_usuarios import menu_usuarios


### Separamos los menús por tipo de usuario --> este sería para usuario estándar y solo le brinda las opciones que tiene este tipo de usuario
def menu_estandar(email_usuario):
    nombre_usuario = usuarios.usuario[email_usuario]["nombre"]

    while True:
        print(f"\n--- MENÚ USUARIO - Bienvenido {nombre_usuario} ---")
        print("1. Consultar mis datos personales")
        print("2. Ejecutar automatización")
        print("3. Consultar mis dispositivos")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios.buscar_usuario(email_usuario)

        elif opcion == "2":
            print("🔧 Automatización ejecutada (simulada).")

        elif opcion == "3":
            dispositivos.listar_dispositivos_usuario(email_usuario)

        elif opcion == "4":
            print("Sesión cerrada.")
            return

        else:
            print("Opción inválida.")

        input("\nPresione Enter para continuar...")


### Separamos los menús por tipo de usuario (este sería del administrador)
def menu_administrador(email_admin):
    """Menú exclusivo para usuarios administradores"""
    nombre_usuario = usuarios.usuario[email_admin]["nombre"]

    while True:
        print(f"\n--- MENÚ ADMINISTRADOR - Bienvenido {nombre_usuario} ---")
        print("1. Consultar automatizaciones activas")
        print("2. Gestión de dispositivos")
        print("3. Modificar rol de un usuario")
        print("4. Volver al menú de ingreso")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dispositivos.consultar_automatizaciones_activas()

        elif opcion == "2":
            menu_dispositivos(email_admin)

        elif opcion == "3":
            print("\n--- MODIFICAR ROL DE USUARIO ---")
            email_objetivo = input("Email del usuario a modificar: ")
            nuevo_rol = input("Nuevo rol (usuario o administrador): ").lower()

            if nuevo_rol in ["usuario", "administrador"]:
                usuarios.modificar_rol(email_objetivo, nuevo_rol, email_admin)
            else:
                print("❌ Rol no válido.")

        elif opcion == "4":
            print("👋 Volviendo al menú de ingreso...")
            return

        else:
            print("❌ Opción inválida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


def menu_principal(email_usuario):  ### Dejamos a esta sola función la tarea de ver qué tipo de usuario es y redirecciona
    datos_usuario = usuarios.usuario[email_usuario]
    rol = datos_usuario["categoria"]

    if rol == "administrador":
        menu_administrador(email_usuario)
    else:
        menu_estandar(email_usuario)




