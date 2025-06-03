# app.py
from SRC.usuarios import usuarios
from SRC.dispositivos import dispositivos_modulo as dispositivos
from SRC.menus import menu_de_ingreso  # Asegurate que esté en esa carpeta
import router  # solo si es necesario importarlo aquí

def inicializar_sistema():
    """Carga los datos desde los archivos JSON y muestra mensaje de inicio"""
    print("🔧 Inicializando sistema...")
    usuarios.cargar_usuarios()
    dispositivos.cargar_dispositivos()
    print("✅ Sistema inicializado correctamente.")

def ejecutar_aplicacion():
    """Punto de entrada principal de la aplicación"""
    try:
        inicializar_sistema()
        menu_de_ingreso.menu_ingreso()
    except KeyboardInterrupt:
        print("\n👋 Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    finally:
        print("\n¡Gracias por usar nuestro Sistema de Gestión!")

if __name__ == "__main__":
    ejecutar_aplicacion()
