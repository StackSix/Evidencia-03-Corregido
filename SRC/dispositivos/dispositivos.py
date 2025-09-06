from SRC.automatizaciones.automatizaciones import crear_automatizacion_por_defecto

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RUTA = os.path.join(BASE_DIR, "data", "dispositivos.json")
dispositivos = {}

def cargar_dispositivos():
    global dispositivos
    if os.path.exists(RUTA):
        with open(RUTA, "r") as f:
            dispositivos = json.load(f)
    else:
        dispositivos = {}

def guardar_dispositivos():
    os.makedirs(os.path.dirname(RUTA), exist_ok=True)
    with open(RUTA, "w") as f:
        json.dump(dispositivos, f, indent=4)

def listar_dispositivos_usuario(email):
    if email in dispositivos:
        print("\n📋 Dispositivos registrados:")
        for nombre, info in dispositivos[email].items():
            print(f"- {nombre} ({info['modelo']}) - Estado: {info['estado']}")
    else:
        print("⚠️ No hay dispositivos registrados.")

#Se elimino registrar_dispositivos

def mostrar_dispositivos(email):
    cargar_dispositivos()
    if email in dispositivos:
        print(f"\n📋 Dispositivos para {email}:")
        for nombre, datos in dispositivos[email].items():
            print(f"- {nombre} ({datos['modelo']}) - Estado: {datos['estado']}")
    else:
        print("⚠️ No se encontraron dispositivos para este usuario.")


def agregar_dispositivo(email):
    cargar_dispositivos()
    nombre = input("Nombre del dispositivo: ").strip()
    if not nombre:
        print("❌ El nombre no puede estar vacío.")
        return
    modelo = input("Modelo del dispositivo: ").strip()
    if not modelo:
        print("❌ El modelo no puede estar vacío.")
        return

    if email not in dispositivos:
        dispositivos[email] = {}

    if nombre in dispositivos[email]:
        print("❌ Ya existe un dispositivo con ese nombre.")
        return

    dispositivos[email][nombre] = {
        "tipo": "cámara de seguridad",
        "modelo": modelo,
        "estado": "encendido"
    }
    guardar_dispositivos()
    crear_automatizacion_por_defecto(email, nombre)

    print(f"✅ Dispositivo '{nombre}' agregado correctamente.")


def eliminar_dispositivo(email):
    cargar_dispositivos()
    if email not in dispositivos or not dispositivos[email]:
        print("❌ El usuario no tiene dispositivos registrados.")
        return

    print("📋 Dispositivos del usuario:")
    for nombre in dispositivos[email]:
        print(f"- {nombre}")
    nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip()
    if nombre in dispositivos[email]:
        del dispositivos[email][nombre]
        guardar_dispositivos()
        print(f"✅ Dispositivo '{nombre}' eliminado.")
    else:
        print("❌ Dispositivo no encontrado.")

def modificar_dispositivo(email):
    cargar_dispositivos()
    if email not in dispositivos or not dispositivos[email]:
        print("❌ El usuario no tiene dispositivos registrados.")
        return

    print("📋 Dispositivos del usuario:")
    for nombre in dispositivos[email]:
        print(f"- {nombre}")
    nombre = input("Ingrese el nombre del dispositivo a modificar: ").strip()
    if nombre not in dispositivos[email]:
        print("❌ Dispositivo no encontrado.")
        return

    modelo_nuevo = input("Ingrese nuevo modelo: ").strip()
    estado_nuevo = input("Nuevo estado (encendido/apagado): ").strip().lower()

    if modelo_nuevo:
        dispositivos[email][nombre]["modelo"] = modelo_nuevo
    if estado_nuevo in ["encendido", "apagado"]:
        dispositivos[email][nombre]["estado"] = estado_nuevo

    guardar_dispositivos()
    print(f"✅ Dispositivo '{nombre}' actualizado.")