import json
import os

ARCHIVO_DISPOSITIVOS = "dispositivos.json"
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

    dispositivo = {
        "tipo_de_dispositivo": tipo_normalizado,
        "modelo": modelo,
        "modo_ahorro": False if tipo_normalizado == "cámara de seguridad" else None
    }

    dispositivos[email_usuario][nombre_del_dispositivo] = dispositivo
    print(f"Dispositivo '{nombre_del_dispositivo}' registrado correctamente.")
    guardar_dispositivos()

def eliminar_dispositivo(nombre_del_dispositivo, email_usuario):
    if email_usuario in dispositivos and nombre_del_dispositivo in dispositivos[email_usuario]:
        dispositivos[email_usuario].pop(nombre_del_dispositivo)
        print(f"Dispositivo '{nombre_del_dispositivo}' eliminado correctamente.")
        guardar_dispositivos()
    else:
        print("Error: El dispositivo no existe o no pertenece a este usuario.")

def buscar_dispositivo(nombre_del_dispositivo):
    encontrado = False
    for email, dispositivos_usuario in dispositivos.items():
        if nombre_del_dispositivo in dispositivos_usuario:
            info = dispositivos_usuario[nombre_del_dispositivo]
            print(f"\nDispositivo encontrado para {email}:")
            print(f"Nombre: {nombre_del_dispositivo}")
            print(f"Tipo: {info['tipo_de_dispositivo']}")
            print(f"Modelo: {info['modelo']}")
            if info["tipo_de_dispositivo"] == "cámara de seguridad":
                print(f"Modo Ahorro: {'Sí' if info.get('modo_ahorro') else 'No'}")
            encontrado = True
    if not encontrado:
        print("No se encontró ningún dispositivo con ese nombre.")

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

def listar_dispositivos_usuario(email_usuario):
    if email_usuario in dispositivos and dispositivos[email_usuario]:
        print(f"\nDispositivos registrados para el usuario {email_usuario}:")
        for nombre, info in dispositivos[email_usuario].items():
            linea = f" - {nombre} (Tipo: {info['tipo_de_dispositivo']}, Modelo: {info['modelo']})"
            if info["tipo_de_dispositivo"] == "cámara de seguridad":
                linea += f", Modo Ahorro: {'Sí' if info.get('modo_ahorro') else 'No'}"
            print(linea)
    else:
        print(f"No hay dispositivos registrados para el usuario {email_usuario}.")

def activar_modo_ahorro(email_usuario):
    if email_usuario not in dispositivos:
        print("Este usuario no tiene dispositivos registrados.")
        return

    camaras = {nombre: info for nombre, info in dispositivos[email_usuario].items()
               if info["tipo_de_dispositivo"] == "cámara de seguridad"}

    if not camaras:
        print("No se encontraron cámaras de seguridad para activar el modo ahorro.")
        return

    print("\n--- CÁMARAS DISPONIBLES ---")
    for i, (nombre, info) in enumerate(camaras.items(), start=1):
        print(f"{i}. {nombre} (modelo: {info.get('modelo', 'Desconocido')})")

    try:
        opcion = int(input("Seleccione la cámara que desea poner en modo ahorro: "))
        camara_seleccionada = list(camaras.keys())[opcion - 1]

        dispositivos[email_usuario][camara_seleccionada]["modo_ahorro"] = True
        print(f"\n✅ Cámara '{camara_seleccionada}' ahora está en modo ahorro.")
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
        print("No hay cámaras en modo ahorro para este usuario.")
        return

    print("\n--- CÁMARAS EN MODO AHORRO ---")
    for i, (nombre, info) in enumerate(camaras_ahorro.items(), start=1):
        print(f"{i}. {nombre} (modelo: {info.get('modelo', 'Desconocido')})")

    try:
        opcion = int(input("Seleccione la cámara que desea desactivar del modo ahorro: "))
        camara_seleccionada = list(camaras_ahorro.keys())[opcion - 1]

        dispositivos[email_usuario][camara_seleccionada]["modo_ahorro"] = False
        print(f"\n✅ Cámara '{camara_seleccionada}' ha salido del modo ahorro.")
        guardar_dispositivos()
    except (ValueError, IndexError):
        print("❌ Opción inválida.")

