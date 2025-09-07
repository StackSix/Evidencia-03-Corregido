import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(BASE_DIR, "data", "automatizaciones.json")
automatizaciones = {}

def validar_dependencias(datos):
    if not datos["encendido"]:
        datos["grabacion_modo"] = "movimiento"
        datos["programacion_horaria"] = {"activo": False}
        datos["notificaciones"] = False
        datos["deteccion_movimiento"] = False
        datos["modo_ahorro"] = False
        datos["activacion_nocturna_silenciosa"] = False
        return

    if not datos["deteccion_movimiento"]:
        datos["notificaciones"] = False
        datos["modo_ahorro"] = False

    if not datos["notificaciones"]:
        datos["modo_ahorro"] = False

    if datos["modo_ahorro"]:
        datos["activacion_nocturna_silenciosa"] = False

    if isinstance(datos["activacion_nocturna_silenciosa"], dict):
        if not datos["activacion_nocturna_silenciosa"].get("activo", False):
            datos["activacion_nocturna_silenciosa"] = False


def cargar_automatizaciones():
    global automatizaciones
    if os.path.exists(RUTA):
        with open(RUTA, "r") as f:
            automatizaciones = json.load(f)
    else:
        automatizaciones = {}

def guardar_automatizaciones():
    os.makedirs(os.path.dirname(RUTA), exist_ok=True)
    with open(RUTA, "w") as f:
        json.dump(automatizaciones, f, indent=4)

def modificar_automatizacion(email, dispositivo):
    cargar_automatizaciones()

    if email not in automatizaciones or dispositivo not in automatizaciones[email]:
        print("❌ Automatización no encontrada.")
        return

    datos = automatizaciones[email][dispositivo]

    while True:
        print("\n--- CONFIGURACIÓN ACTUAL ---")
        for k, v in datos.items():
            print(f"{k}: {v}")

        print("\n¿Qué desea modificar?")
        print("1. Encendido/Apagado")
        print("2. Modo de grabación (siempre/movimiento)")
        print("3. Programar horario automático")
        print("4. Notificaciones por movimiento")
        print("5. Detección de movimiento")
        print("6. Modo ahorro")
        print("7. Activación nocturna silenciosa")
        print("8. Volver al menú")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos["encendido"] = not datos["encendido"]

        elif opcion == "2":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            modo = input("Ingrese 'siempre' o 'movimiento': ").lower()
            if modo in ["siempre", "movimiento"]:
                datos["grabacion_modo"] = modo
            else:
                print("❌ Modo inválido.")

        elif opcion == "3":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            activar = input("¿Desea activar la programación horaria? (s/n): ").lower()
            if activar == "s":
                on = input("Horario de encendido (HH:MM): ")
                off = input("Horario de apagado (HH:MM): ")
                datos["programacion_horaria"] = {
                    "activo": True,
                    "encendido": on,
                    "apagado": off
                }
            else:
                datos["programacion_horaria"] = {"activo": False}

        elif opcion == "4":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            if not datos["deteccion_movimiento"]:
                print("⚠️ No se puede activar notificaciones sin detección de movimiento.")
                continuar = input("¿Deseás activar detección de movimiento ahora? (s/n): ").lower()
                if continuar == "s":
                    datos["deteccion_movimiento"] = True
                else:
                    continue
            datos["notificaciones"] = not datos["notificaciones"]

        elif opcion == "5":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            if datos["grabacion_modo"] == "movimiento" and datos["deteccion_movimiento"]:
                confirmar = input("⚠️ Estás usando grabación por movimiento. ¿Deseás cambiar a 'siempre' antes de desactivar la detección? (s/n): ").lower()
                if confirmar == "s":
                    datos["grabacion_modo"] = "siempre"
                else:
                    continue
            datos["deteccion_movimiento"] = not datos["deteccion_movimiento"]

        elif opcion == "6":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            if not datos["deteccion_movimiento"] or not datos["notificaciones"]:
                print("⚠️ Requiere detección de movimiento y notificaciones activas.")
                activar = input("¿Deseás activarlas ahora? (s/n): ").lower()
                if activar == "s":
                    datos["deteccion_movimiento"] = True
                    datos["notificaciones"] = True
                else:
                    continue

            if esta_en_horario_nocturno(datos.get("activacion_nocturna_silenciosa", False)):
                print("⚠️ No se puede activar modo ahorro porque ya está activo el modo nocturno silencioso.")
                continue

            datos["modo_ahorro"] = not datos["modo_ahorro"]

        elif opcion == "7":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            if datos["modo_ahorro"]:
                print("⚠️ No puede activarse junto al modo ahorro.")
                continue
            configurar = input("¿Deseás configurar un horario nocturno silencioso? (s/n): ").lower()
            if configurar == "s":
                desde = input("Hora de inicio silencioso (HH:MM): ")
                hasta = input("Hora de fin silencioso (HH:MM): ")
                datos["activacion_nocturna_silenciosa"] = {
                    "activo": True,
                    "desde": desde,
                    "hasta": hasta
                }

                # Verificamos si ya está en horario y hay conflicto con modo ahorro
                if datos["modo_ahorro"] and esta_en_horario_nocturno(datos["activacion_nocturna_silenciosa"]):
                    print("⚠️ Hay conflicto con el modo ahorro activo. Desactivándolo.")
                    datos["modo_ahorro"] = False

            else:
                datos["activacion_nocturna_silenciosa"] = False

def mostrar_automatizaciones_activas():
    cargar_automatizaciones()
    if not automatizaciones:
        print("⚠️ No hay automatizaciones configuradas.")
        return

    for email, dispositivos in automatizaciones.items():
        print(f"\n📧 Usuario: {email}")
        for nombre_disp, config in dispositivos.items():
            print(f"  📷 Dispositivo: {nombre_disp}")
            for clave, valor in config.items():
                print(f"    🔧 {clave}: {valor}")

def configurar_automatizacion(email):
    cargar_automatizaciones()

    if email not in automatizaciones or not automatizaciones[email]:
        print("⚠️ No hay automatizaciones disponibles para este usuario.")
        return

    dispositivos = list(automatizaciones[email].keys())
    print("\n📋 Dispositivos con automatizaciones:")
    for i, nombre in enumerate(dispositivos):
        print(f"{i+1}. {nombre}")

    try:
        opcion = int(input("Seleccione un dispositivo por número: "))
        if 1 <= opcion <= len(dispositivos):
            dispositivo = dispositivos[opcion - 1]
            modificar_automatizacion(email, dispositivo)
        else:
            print("❌ Opción fuera de rango.")
    except ValueError:
        print("❌ Entrada inválida.")


def crear_automatizacion_por_defecto(email, nombre_disp):
    cargar_automatizaciones()
    if email not in automatizaciones:
        automatizaciones[email] = {}

    automatizaciones[email][nombre_disp] = {
        "encendido": True,
        "grabacion_modo": "movimiento",
        "programacion_horaria": {"activo": False},
        "notificaciones": True,
        "deteccion_movimiento": True,
        "modo_ahorro": False,
        "activacion_nocturna_silenciosa": False
    }



    guardar_automatizaciones()

def validar_dependencias(datos):
    # Si encendido está apagado, muchas funciones no deben estar activas
    if not datos["encendido"]:
        datos["grabacion_modo"] = "movimiento"
        datos["programacion_horaria"]["activo"] = False
        datos["notificaciones"] = False
        datos["deteccion_movimiento"] = False
        datos["modo_ahorro"] = False
        datos["activacion_nocturna_silenciosa"] = False

    # Si detección de movimiento está apagada, se apagan notificaciones y ahorro
    if not datos["deteccion_movimiento"]:
        datos["notificaciones"] = False
        datos["modo_ahorro"] = False

    # Si notificaciones están apagadas, se apaga modo ahorro
    if not datos["notificaciones"]:
        datos["modo_ahorro"] = False

    # Si modo ahorro está activo, no puede haber activación nocturna
    if datos["modo_ahorro"]:
        datos["activacion_nocturna_silenciosa"] = False    


def esta_en_horario_nocturno(silencioso):
    if not isinstance(silencioso, dict) or not silencioso.get("activo"):
        return False

    ahora = datetime.now().strftime("%H:%M")
    desde = silencioso.get("desde")
    hasta = silencioso.get("hasta")

    if not desde or not hasta:
        return False

    # Caso donde el rango es, por ejemplo, 22:00 a 07:00 (pasa medianoche)
    if desde > hasta:
        return ahora >= desde or ahora <= hasta
    else:
        return desde <= ahora <= hasta