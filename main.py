# main.py

import usuarios  # Importamos el módulo con las funciones de usuario

def mostrar_menu():
    print("\n--- Menú de Gestión de Usuarios ---")
    print("1. Registrar usuario")
    print("2. Eliminar usuario")
    print("3. Buscar usuario")
    print("4. Listar todos los usuarios")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            contraseña = input ("ingresa tu contraseña:")
            usuarios.registrar_usuario(nombre, email, contraseña)
        
        elif opcion == "2":
            email = input("Ingrese el email del usuario a eliminar: ")
            contraseña = input ("ingresa tu contraseña:")
            usuarios.eliminar_usuario(email, contraseña)

        elif opcion == "3":
            email = input("Ingrese el email del usuario a buscar: ")
            usuarios.buscar_usuario(email)

        elif opcion == "4":
            usuarios.listar_usuarios()

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
