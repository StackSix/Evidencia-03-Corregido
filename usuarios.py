import json
import os

usuario = {}

USUARIOS = "usuarios.json"

def cargar_usuarios():
    global usuario
    if os.path.exists(USUARIOS):
        with open(USUARIOS, "r") as archivo:
            usuario = json.load(archivo)
    else:
        usuario = {}

def guardar_usuarios():
    with open(USUARIOS, "w") as archivo:
        json.dump(usuario, archivo, indent=4)

def verificar_credenciales(email, contraseña):
    if email in usuario and usuario[email]["contraseña"] == contraseña:
        return True
    return False

def iniciar_sesion(email, contraseña):
    if email in usuario:
        if usuario[email]["contraseña"] == contraseña:
            print(f"Bienvenido, {usuario[email]['nombre']}!")
            return True
        else:
            print("Error: Contraseña incorrecta.")
            return False
    else:
        print("Error: No existe ningún usuario con ese email.")
        return False

def registrar_usuario(nombre, email, contraseña):
    if email in usuario:
        print("Error: Ya existe un usuario con ese email.")
    else:
        usuario[email] = {
            "nombre": nombre,
            "contraseña": contraseña
        }
        print(f"Usuario '{nombre}' registrado correctamente.")
        guardar_usuarios()  # ✅ Persistencia

def eliminar_usuario(email, contraseña):
    if email in usuario:
        if usuario[email]["contraseña"] == contraseña:
            nombre = usuario[email]["nombre"]
            usuario.pop(email)
            print(f"Usuario '{nombre}' eliminado correctamente.")
            guardar_usuarios()  # ✅ Persistencia
            return True
        else:
            print("Error: La contraseña no es correcta.")
            return False
    else:
        print("Error: No se encontró ningún usuario con ese email.")
        return False

def cambiar_contraseña(email, nueva_contraseña):
    if email in usuario:
        usuario[email]["contraseña"] = nueva_contraseña
        print("Contraseña cambiada correctamente.")
        guardar_usuarios()  # ✅ Persistencia
    else:
        print("Error: No se encontró ningún usuario con ese email.")

def buscar_usuario(email):
    if email in usuario:
        print(f"Usuario encontrado: {usuario[email]['nombre']} ({email})")
    else:
        print("No se encontró ningún usuario con ese email.")

def listar_usuarios():
    if usuario:
        print("\nLista de usuarios:")
        for email, datos in usuario.items():
            print(f" - {datos['nombre']} ({email})")
    else:
        print("No hay usuarios registrados.")
