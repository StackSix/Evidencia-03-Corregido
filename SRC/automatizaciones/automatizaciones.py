import json
import os

RUTA = os.path.join("data", "automatizaciones.json")
automatizaciones = {}

def cargar_automatizaciones():
    global automatizaciones
    if os.path.exists(RUTA):
        with open(RUTA, "r") as f:
            automatizaciones = json.load(f)
    else:
        automatizaciones = {}

def guardar_automatizaciones():
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

        elif opcion == "3":
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
            if not datos["encendido"] or not datos["deteccion_movimiento"]:
                print("⚠️ Requiere detección de movimiento y estar encendido.")
                continue
            datos["notificaciones"] = not datos["notificaciones"]

        elif opcion == "5":
            if not datos["encendido"]:
                print("⚠️ El dispositivo debe estar encendido.")
                continue
            datos["deteccion_movimiento"] = not datos["deteccion_movimiento"]

        elif opcion == "6":
            if not datos["deteccion_movimiento"] or not datos["notificaciones"]:
                print("⚠️ Requiere detección y notificaciones activas.")
                continue
            datos["modo_ahorro"] = not datos["modo_ahorro"]

        elif opcion == "7":
            if not datos["encendido"] or datos.get("modo_ahorro"):
                print("⚠️ No puede estar en modo ahorro y debe estar encendido.")
                continue
            datos["activacion_nocturna_silenciosa"] = not datos.get("activacion_nocturna_silenciosa", False)

        elif opcion == "8":
            break
        else:
            print("❌ Opción inválida.")

    guardar_automatizaciones()
    print("✅ Automatización actualizada correctamente.")


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