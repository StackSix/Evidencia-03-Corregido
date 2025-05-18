# dispositivos.py

# Diccionario para almacenar dispositivos

dispositivos = {}

def registrar_dispositivo(nombre_del_dispositivo, tipo_de_dispositivo, modelo, email_usuario):
    """
    Registra un dispositivo nuevo en el diccionario 'dispositivos'.
    La clave será: nombre_del_dispositivo, que debe ser único.
    El dispositivo se vincula al email de un usuario existente.
    """
    if nombre_del_dispositivo in dispositivos:
        print("Error: Ya existe un dispositivo con ese nombre.")
    else:
        dispositivos[nombre_del_dispositivo] = {
            "tipo_de_dispositivo": tipo_de_dispositivo,
            "modelo": modelo,
            "propietario": email_usuario
        }
        print(f"Dispositivo '{nombre_del_dispositivo}' registrado correctamente.")

def eliminar_dispositivo(nombre_del_dispositivo, email_usuario):
    """
    Elimina un dispositivo si existe y pertenece al usuario especificado.
    """
    if nombre_del_dispositivo in dispositivos:
        # Verificar que el dispositivo pertenezca al usuario
        if dispositivos[nombre_del_dispositivo]["propietario"] == email_usuario:
            dispositivos.pop(nombre_del_dispositivo)
            print(f"Dispositivo '{nombre_del_dispositivo}' eliminado correctamente.")
        else:
            print("Error: Este dispositivo no pertenece al usuario especificado.")
    else:
        print("Error: El dispositivo no existe.")

def buscar_dispositivo(nombre_del_dispositivo):
    """
    Busca un dispositivo por su nombre.
    """
    if nombre_del_dispositivo in dispositivos:
        info = dispositivos[nombre_del_dispositivo]
        print(f"\nDispositivo encontrado:")
        print(f"Nombre: {nombre_del_dispositivo}")
        print(f"Tipo: {info['tipo_de_dispositivo']}")
        print(f"Modelo: {info['modelo']}")
        print(f"Propietario: {info['propietario']}")
    else:
        print("No se encontró ningún dispositivo con ese nombre.")

def listar_dispositivos():
    """
    Muestra todos los dispositivos registrados.
    """
    if dispositivos:
        print("\nLista de dispositivos:")
        for nombre, info in dispositivos.items():
            print(f" - {nombre} (Tipo: {info['tipo_de_dispositivo']}, Modelo: {info['modelo']}, Propietario: {info['propietario']})")
    else:
        print("No hay dispositivos registrados.")

def listar_dispositivos_usuario(email_usuario):
    """
    Muestra todos los dispositivos registrados de un usuario específico.
    """
    dispositivos_usuario = {nombre: info for nombre, info in dispositivos.items() 
                          if info["propietario"] == email_usuario}
    
    if dispositivos_usuario:
        print(f"\nDispositivos registrados para el usuario {email_usuario}:")
        for nombre, info in dispositivos_usuario.items():
            print(f" - {nombre} (Tipo: {info['tipo_de_dispositivo']}, Modelo: {info['modelo']})")
    else:
        print(f"No hay dispositivos registrados para el usuario {email_usuario}.")