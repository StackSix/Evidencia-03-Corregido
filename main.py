# main.py
"""
Sistema de Gestión de Usuarios y Dispositivos
Punto de entrada principal del programa

Este módulo coordina la funcionalidad entre todos los demás módulos:
- ingreso: Maneja el menú de inicio de sesión y registro
- principal: Gestiona el menú principal y sus opciones
- usuarios: Administra la información de los usuarios
- dispositivos: Administra la información de los dispositivos
"""

# Importamos todos los módulos del sistema
import ingreso
import principal
import usuarios
import dispositivos

def inicializar_sistema():
    """Función para inicializar el sistema"""
    print("Inicializando sistema...")
    
    # Este espacio se puede utilizar para cargar datos desde archivos
    # si se implementa funcionalidad de persistencia en el futuro
    
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
        # Aquí se podrían guardar datos en archivos si fuera necesario
        print("\n¡Gracias por usar nuestro Sistema de Gestión!")

if __name__ == "__main__":
    ejecutar_aplicacion()