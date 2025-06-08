from SRC.dispositivos.dispositivos import (
    mostrar_dispositivos,
    agregar_dispositivo,
    eliminar_dispositivo,
    modificar_dispositivo
)
from SRC.automatizaciones.automatizaciones import (
    mostrar_automatizaciones_activas,
    configurar_automatizacion
)
from SRC.usuarios.usuarios import (
    registrar_usuario,
    login,
    obtener_rol,
    modificar_rol
)


def mostrar_datos_usuario(email):
    print(f"\n📧 Email: {email}")
    print(f"🔐 Rol: {obtener_rol(email)}")


def menu_usuario(email):
    while True:
        print(f"\n--- MENÚ USUARIO - Bienvenido {email} ---")
        print("1. Ver mis datos")
        print("2. Configurar automatización")
        print("3. Ver dispositivos")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_datos_usuario(email)
        elif opcion == "2":
            configurar_automatizacion(email)
        elif opcion == "3":
            mostrar_dispositivos(email)
        elif opcion == "4":
            print("\n👋 Sesión finalizada.")
            break
        else:
            print("❌ Opción inválida.")


def menu_admin(email):
    while True:
        print(f"\n--- MENÚ ADMINISTRADOR - Bienvenido {email} ---")
        print("1. Ver automatizaciones activas")
        print("2. Gestionar dispositivos")
        print("3. Modificar rol de usuario")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_automatizaciones_activas()
        elif opcion == "2":
            usuario = input("Email del usuario: ").strip()
            if not usuario:
                print("❌ Email no puede estar vacío.")
                continue

            print("\n--- Gestión de dispositivos ---")
            print("1. Agregar dispositivo")
            print("2. Eliminar dispositivo")
            print("3. Modificar dispositivo")
            opcion_sub = input("Seleccione una opción: ")

            if opcion_sub == "1":
                agregar_dispositivo(usuario)
            elif opcion_sub == "2":
                eliminar_dispositivo(usuario)
            elif opcion_sub == "3":
                modificar_dispositivo(usuario)
            else:
                print("❌ Opción inválida.")
        elif opcion == "3":
            objetivo = input("Email del usuario a modificar: ")
            nuevo_rol = input("Nuevo rol (usuario/administrador): ")
            modificar_rol(objetivo, nuevo_rol, email)
        elif opcion == "4":
            print("\n👋 Sesión finalizada.")
            break
        else:
            print("❌ Opción inválida.")


def menu_ingreso():
    while True:
        print("\n--- MENÚ INICIAL ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            usuario = login(email, contraseña)
            if usuario:
                if usuario["rol"] == "usuario":
                    menu_usuario(email)
                elif usuario["rol"] == "administrador":
                    menu_admin(email)
            else:
                print("❌ Credenciales incorrectas.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            categoria = input("Categoría (usuario/administrador): ").lower()
            registrar_usuario(nombre, email, contraseña, categoria)

        elif opcion == "3":
            print("\nGracias por usar el sistema.")
            break
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu_ingreso()
