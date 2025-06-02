from SRC.usuarios import usuarios
from SRC.dispositivos import dispositivos_modulo as dispositivos
from SRC.menus import ingreso
import router
from SRC.dispositivos import dispositivos_modulo as dispositivos


def inicializar_sistema():
    """Función para inicializar el sistema"""
    print("Inicializando sistema...")

    # Cargar datos desde archivos JSON
    usuarios.cargar_usuarios()
    dispositivos.cargar_dispositivos()

    print("Sistema inicializado correctamente")

def ejecutar_aplicacion():
    """Función principal que ejecuta la aplicación"""
    try:
        inicializar_sistema()
        ingreso.menu_ingreso()
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError inesperado: {e}")
    finally:
        print("\n¡Gracias por usar nuestro Sistema de Gestión!")

if __name__ == "__main__":
    ejecutar_aplicacion()
