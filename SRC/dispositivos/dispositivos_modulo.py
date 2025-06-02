import json
import os
from datetime import datetime

ARCHIVO_DISPOSITIVOS = os.path.join("data", "dispositivos.json")

dispositivos = {}

def cargar_dispositivos():
    global dispositivos
    if os.path.exists(ARCHIVO_DISPOSITIVOS):
        with open(ARCHIVO_DISPOSITIVOS, "r") as archivo:
            dispositivos = json.load(archivo)
    else:
        dispositivos = {}

def guardar_dispositivos():
    with open(ARCHIVO_DISPOSITIVOS, "w") as archivo:
        json.dump(dispositivos, archivo, indent=4)

def registrar_dispositivo(nombre_del_dispositivo, tipo_de_dispositivo, modelo, email_usuario):
    tipos_permitidos = ["cámara de seguridad", "sensor de movimiento"]
    tipo_normalizado = tipo_de_dispositivo.strip().lower()

    if tipo_normalizado not in tipos_permitidos:
        print("Error: Tipo de dispositivo no permitido. Solo se aceptan 'cámara de seguridad' y 'sensor de movimiento'.")
        return

    if email_usuario not in dispositivos:
        dispositivos[email_usuario] = {}

    if nombre_del_dispositivo in dispositivos[email_usuario]:
        print("Error: Ya existe un dispositivo con ese nombre para este usuario.")
        return

    if tipo_normalizado == "cámara de seguridad":
        dispositivo = {
            "tipo_de_dispositivo": tipo_normalizado,
            "modelo": modelo,
            "estado": "encendido",
            "alerta_movimiento": True,
            "programacion_horaria": {
                "encendido": "07:00",
                "apagado": "22:00"
            },
            "notificar_email": True,
            "modo_ahorro": False
        }
    elif tipo_normalizado == "sensor de movimiento":
        dispositivo = {
            "tipo_de_dispositivo": tipo_normalizado,
            "modelo": modelo,
            "estado": "encendido",
            "notificar_email": True,
            "alarma_activada": True
        }

    dispositivos[email_usuario][nombre_del_dispositivo] = dispositivo
    print(f"✅ Dispositivo '{nombre_del_dispositivo}' registrado correctamente con configuración predeterminada.")
    guardar_dispositivos()

def solicitar_hora(mensaje):
    while True:
        hora = input(mensaje)
        try:
            datetime.strptime(hora, "%H:%M")
            return hora
        except ValueError:
            print("❌ Formato inválido. Debe ser hh:mm (por ejemplo: 07:30)")

def solicitar_hora_rango():
    while True:
        hora_on = solicitar_hora("Ingrese hora de encendido (hh:mm): ")
        hora_off = solicitar_hora("Ingrese hora de apagado (hh:mm): ")

        h_on = datetime.strptime(hora_on, "%H:%M")
        h_off = datetime.strptime(hora_off, "%H:%M")

        if h_off > h_on or hora_off < hora_on:
            return {"encendido": hora_on, "apagado": hora_off}
        else:
            print("❌ La hora de apagado debe ser posterior a la de encendido (o un ciclo nocturno válido como 22:00 → 07:00).")

def modificar_configuracion_dispositivo(email_usuario):
    if email_usuario not in dispositivos or not dispositivos[email_usuario]:
        print("❌ No hay dispositivos registrados para este usuario.")
        return

    print("\n--- MODIFICAR CONFIGURACIÓN DE DISPOSITIVOS ---")
    lista_dispositivos = list(dispositivos[email_usuario].keys())
    for i, nombre in enumerate(lista_dispositivos, 1):
        print(f"{i}. {nombre}")

    try:
        indice = int(input("Seleccione un dispositivo por número: ")) - 1
        nombre_seleccionado = lista_dispositivos[indice]
        disp = dispositivos[email_usuario][nombre_seleccionado]
    except (IndexError, ValueError):
        print("❌ Selección inválida.")
        return

    while True:
        print(f"\nConfiguración actual de '{nombre_seleccionado}':")
        for clave, valor in disp.items():
            print(f" - {clave}: {valor}")

        print("\n¿Qué desea modificar?")
        opciones = []

        print("1. Estado (encendido/apagado)")
        opciones.append("estado")

        if disp["tipo_de_dispositivo"] == "cámara de seguridad":
            print("2. Alerta por movimiento")
            print("3. Programación horaria de encendido/apagado")
            print("4. Notificación por email")
            print("5. Modo ahorro")
            opciones.extend(["alerta_movimiento", "programacion_horaria", "notificar_email", "modo_ahorro"])
        elif disp["tipo_de_dispositivo"] == "sensor de movimiento":
            print("2. Notificación por email")
            print("3. Alarma activada")
            opciones.extend(["notificar_email", "alarma_activada"])

        print("0. Volver")

        seleccion = input("Seleccione una opción: ")

        if seleccion == "0":
            guardar_dispositivos()
            print("✔️ Cambios guardados. Volviendo al menú...")
            break

        try:
            seleccion_idx = int(seleccion) - 1
            opcion_elegida = opciones[seleccion_idx]
        except (IndexError, ValueError):
            print("❌ Opción inválida.")
            continue

        if opcion_elegida == "estado":
            disp["estado"] = "apagado" if disp["estado"] == "encendido" else "encendido"
        elif opcion_elegida == "alerta_movimiento":
            disp["alerta_movimiento"] = not disp.get("alerta_movimiento", False)
        elif opcion_elegida == "programacion_horaria":
            respuesta = input("¿Desea desactivar la programación horaria? (s/n): ").lower()
            if respuesta == "s":
                disp["programacion_horaria"] = None
                print("⏱️ Programación horaria desactivada.")
            else:
                disp["programacion_horaria"] = solicitar_hora_rango()
        elif opcion_elegida == "notificar_email":
            disp["notificar_email"] = not disp.get("notificar_email", False)
        elif opcion_elegida == "modo_ahorro":
            disp["modo_ahorro"] = not disp.get("modo_ahorro", False)
        elif opcion_elegida == "alarma_activada":
            disp["alarma_activada"] = not disp.get("alarma_activada", True)

        guardar_dispositivos()
        print("✔️ Cambio aplicado correctamente.")

def listar_dispositivos():
    if dispositivos:
        print("\nLista de todos los dispositivos registrados:")
        for email, dispositivos_usuario in dispositivos.items():
            for nombre, info in dispositivos_usuario.items():
                linea = f" - {nombre} (Tipo: {info['tipo_de_dispositivo']}, Modelo: {info['modelo']}, Usuario: {email})"
                if info['tipo_de_dispositivo'] == "cámara de seguridad":
                    linea += f", Modo Ahorro: {'Sí' if info.get('modo_ahorro') else 'No'}"
                print(linea)
    else:
        print("No hay dispositivos registrados.")

def consultar_automatizaciones_activas():
    print("\n--- AUTOMATIZACIONES ACTIVAS (simuladas) ---")
    print("✅ Cámara de seguridad programada para encender a las 21:00 y apagarse a las 06:00")
    print("✅ Sensor de movimiento enviará alerta si no detecta movimiento en 12 horas")

def buscar_dispositivo(nombre_del_dispositivo):
    encontrado = False
    for email, dispositivos_usuario in dispositivos.items():
        if nombre_del_dispositivo in dispositivos_usuario:
            info = dispositivos_usuario[nombre_del_dispositivo]
            print(f"\n🔎 Dispositivo encontrado para {email}:")
            print(f" - Nombre: {nombre_del_dispositivo}")
            print(f" - Tipo: {info['tipo_de_dispositivo']}")
            print(f" - Modelo: {info['modelo']}")
            print(f" - Estado: {info.get('estado', 'desconocido')}")
            if info["tipo_de_dispositivo"] == "cámara de seguridad":
                print(f" - Modo Ahorro: {'Sí' if info.get('modo_ahorro') else 'No'}")
                print(f" - Programación Horaria: {info.get('programacion_horaria')}")
                print(f" - Alerta Movimiento: {info.get('alerta_movimiento')}")
            elif info["tipo_de_dispositivo"] == "sensor de movimiento":
                print(f" - Alarma Activada: {info.get('alarma_activada')}")
            print(f" - Notificación Email: {info.get('notificar_email')}")
            encontrado = True
    if not encontrado:
        print("❌ No se encontró ningún dispositivo con ese nombre.")

def eliminar_dispositivo(nombre_del_dispositivo, email_usuario):
    if email_usuario in dispositivos and nombre_del_dispositivo in dispositivos[email_usuario]:
        del dispositivos[email_usuario][nombre_del_dispositivo]
        print(f"🗑️ Dispositivo '{nombre_del_dispositivo}' eliminado correctamente.")
        guardar_dispositivos()
    else:
        print("❌ El dispositivo no existe o no pertenece a este usuario.")


def activar_modo_ahorro(email_usuario):
    if email_usuario not in dispositivos:
        print("Este usuario no tiene dispositivos registrados.")
        return

    camaras = {
        nombre: info for nombre, info in dispositivos[email_usuario].items()
        if info["tipo_de_dispositivo"] == "cámara de seguridad"
    }

    if not camaras:
        print("❌ No se encontraron cámaras de seguridad.")
        return

    print("\n--- CÁMARAS DISPONIBLES ---")
    for i, (nombre, info) in enumerate(camaras.items(), 1):
        print(f"{i}. {nombre} (modelo: {info.get('modelo')})")

    try:
        opcion = int(input("Seleccione la cámara a poner en modo ahorro: "))
        seleccion = list(camaras.keys())[opcion - 1]
        dispositivos[email_usuario][seleccion]["modo_ahorro"] = True
        print(f"🔋 Cámara '{seleccion}' ahora está en modo ahorro.")
        guardar_dispositivos()
    except (ValueError, IndexError):
        print("❌ Opción inválida.")


def desactivar_modo_ahorro(email_usuario):
    if email_usuario not in dispositivos:
        print("Este usuario no tiene dispositivos registrados.")
        return

    camaras_ahorro = {
        nombre: info for nombre, info in dispositivos[email_usuario].items()
        if info["tipo_de_dispositivo"] == "cámara de seguridad" and info.get("modo_ahorro")
    }

    if not camaras_ahorro:
        print("❌ No hay cámaras en modo ahorro.")
        return

    print("\n--- CÁMARAS EN MODO AHORRO ---")
    for i, (nombre, info) in enumerate(camaras_ahorro.items(), 1):
        print(f"{i}. {nombre} (modelo: {info.get('modelo')})")

    try:
        opcion = int(input("Seleccione la cámara para desactivar el modo ahorro: "))
        seleccion = list(camaras_ahorro.keys())[opcion - 1]
        dispositivos[email_usuario][seleccion]["modo_ahorro"] = False
        print(f"⚡ Cámara '{seleccion}' ha salido del modo ahorro.")
        guardar_dispositivos()
    except (ValueError, IndexError):
        print("❌ Opción inválida.")


def listar_dispositivos_usuario(email_usuario):
    if email_usuario not in dispositivos or not dispositivos[email_usuario]:
        print("❌ No hay dispositivos registrados para este usuario.")
        return

    print(f"\n📋 Dispositivos del usuario '{email_usuario}':")
    for nombre, info in dispositivos[email_usuario].items():
        print(f" - Nombre: {nombre}")
        print(f"   Tipo: {info.get('tipo_de_dispositivo')}")
        print(f"   Modelo: {info.get('modelo')}")
        print(f"   Estado: {info.get('estado')}")
        if info["tipo_de_dispositivo"] == "cámara de seguridad":
            print(f"   Modo Ahorro: {'Sí' if info.get('modo_ahorro') else 'No'}")
            print(f"   Programación Horaria: {info.get('programacion_horaria')}")
            print(f"   Alerta Movimiento: {info.get('alerta_movimiento')}")
        elif info["tipo_de_dispositivo"] == "sensor de movimiento":
            print(f"   Alarma Activada: {info.get('alarma_activada')}")
        print(f"   Notificación Email: {info.get('notificar_email')}")
        print("")
