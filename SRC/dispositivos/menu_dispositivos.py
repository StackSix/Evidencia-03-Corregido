from SRC.dispositivos import dispositivos_modulo as dispositivos
from SRC.usuarios import usuarios

def mostrar_menu_dispositivos():
    print("\n--- SISTEMA DE GESTIÓN DE DISPOSITIVOS ---")
    print("1. Registrar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Buscar dispositivo")
    print("4. Listar dispositivos")
    print("5. Activar modo ahorro de cámaras")
    print("6. Desactivar modo ahorro de cámaras")
    print("7. Modificar configuración de un dispositivo")
    print("8. Volver al menú anterior")
    return input("Seleccione una opción: ")

def menu_dispositivos(email_actual):
    while True:
        opcion = mostrar_menu_dispositivos()

        if opcion == "1":
            nombre = input("Nombre del dispositivo: ")
            print("1. Cámara de seguridad\n2. Sensor de movimiento")
            tipo = input("Opción: ")
            if tipo == "1":
                tipo_disp = "cámara de seguridad"
            elif tipo == "2":
                tipo_disp = "sensor de movimiento"
            else:
                print("❌ Tipo inválido.")
                continue
            modelo = input("Modelo del dispositivo: ")
            dispositivos.registrar_dispositivo(nombre, tipo_disp, modelo, email_actual)

        elif opcion == "2":
            nombre = input("Nombre del dispositivo a eliminar: ")
            contraseña = input("Confirmar contraseña: ")
            if usuarios.verificar_credenciales(email_actual, contraseña):
                dispositivos.eliminar_dispositivo(nombre, email_actual)
            else:
                print("❌ Contraseña incorrecta.")

        elif opcion == "3":
            nombre = input("Nombre del dispositivo a buscar: ")
            dispositivos.buscar_dispositivo(nombre)

        elif opcion == "4":
            print("1. Todos los dispositivos\n2. Solo mis dispositivos")
            sub = input("Opción: ")
            if sub == "1":
                dispositivos.listar_dispositivos()
            elif sub == "2":
                dispositivos.listar_dispositivos_usuario(email_actual)
            else:
                print("❌ Opción inválida.")

        elif opcion == "5":
            dispositivos.activar_modo_ahorro(email_actual)

        elif opcion == "6":
            dispositivos.desactivar_modo_ahorro(email_actual)

        elif opcion == "7":
            dispositivos.modificar_configuracion_dispositivo(email_actual)

        elif opcion == "8":
            print("👋 Volviendo al menú anterior...")
            return

        else:
            print("❌ Opción inválida.")

        input("\nPresione Enter para continuar...")


