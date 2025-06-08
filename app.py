from SRC.usuarios.usuarios import registrar_admin_unico
from SRC.usuarios.usuarios import (
    cargar_usuarios,
    registrar_usuario,
    login,
    obtener_rol,
    modificar_rol
)

from router import menu_usuario, menu_admin

def main():
    cargar_usuarios()

    while True:
        print("\n--- INGRESO ---")
        print("1. Iniciar sesión")
        print("2. Registrarse como usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            usuario = login(email, contraseña)
            if usuario:
                print(f"\nBienvenido, {usuario['nombre']}! Rol: {usuario['rol']}")
                if usuario["rol"] == "administrador":
                    menu_admin(email)
                else:
                    menu_usuario(email)
            else:
                print("❌ Credenciales incorrectas.")
        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            registrar_usuario(nombre, email, contraseña, rol="usuario")
        elif opcion == "3":
            print("¡Gracias por usar nuestro Sistema de Gestión!")
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    try:
        registrar_admin_unico()
        main()
    except KeyboardInterrupt:
        print("\n👋 Sistema interrumpido por el usuario.")