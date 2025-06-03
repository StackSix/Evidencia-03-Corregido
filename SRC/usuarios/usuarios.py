import json
import os
import re

usuario = {}

USUARIOS = os.path.join("data", "usuarios.json")

# ------------------------------------------
def cargar_usuarios():
    global usuario
    if os.path.exists(USUARIOS):
        with open(USUARIOS, "r") as archivo:
            usuario = json.load(archivo)
    else:
        usuario = {}

# ------------------------------------------
def guardar_usuarios():
    with open(USUARIOS, "w") as archivo:
        json.dump(usuario, archivo, indent=4)

# ------------------------------------------
def verificar_credenciales(email, contraseña):
    return email in usuario and usuario[email]["contraseña"] == contraseña

# ------------------------------------------
def iniciar_sesion(email, contraseña):
    if email in usuario:
        if usuario[email]["contraseña"] == contraseña:
            nombre = usuario[email]["nombre"]
            categoria = usuario[email]["categoria"]
            print(f"Bienvenido, {nombre}! Rol: {categoria}")
            return categoria
        else:
            print("❌ Error: Contraseña incorrecta.")
    else:
        print("❌ Error: No existe ningún usuario con ese email.")
    return False

# ------------------------------------------
def registrar_usuario(nombre, email, contraseña, categoria="usuario"):
    categoria = categoria.lower()
    if categoria not in ["usuario", "administrador"]:
        print("❌ Error: Categoría inválida. Debe ser 'usuario' o 'administrador'.")
        return

    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_email, email):
        print("❌ Error: Email inválido. Debe tener formato como ejemplo@gmail.com.")
        return

    patron_contraseña = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=\[\]{};:"\',.<>?/\\|]).+$'
    if not re.match(patron_contraseña, contraseña) or len(contraseña) < 8 or " " in contraseña:
        print("❌ Contraseña insegura. Debe tener al menos 8 caracteres, incluir una mayúscula, un número, un símbolo y no contener espacios.")
        return

    if email in usuario:
        print("❌ Ya existe un usuario con ese email.")
        return

    usuario[email] = {
        "nombre": nombre.lower(),
        "contraseña": contraseña,
        "categoria": categoria
    }
    guardar_usuarios()
    print(f"✅ Usuario '{nombre}' registrado exitosamente como '{categoria}'.")

# ------------------------------------------
def cambiar_contraseña(email, nueva_contraseña):
    if email in usuario:
        usuario[email]["contraseña"] = nueva_contraseña
        print("🔐 Contraseña cambiada correctamente.")
        guardar_usuarios()
    else:
        print("❌ Error: No se encontró ningún usuario con ese email.")

# ------------------------------------------
def buscar_usuario(email):
    if email in usuario:
        datos = usuario[email]
        print(f"🔍 Usuario encontrado: {datos['nombre']} ({email}) - Rol: {datos['categoria']}")
    else:
        print("❌ No se encontró ningún usuario con ese email.")

# ------------------------------------------
def eliminar_usuario(email, contraseña):
    if email in usuario:
        if usuario[email]["contraseña"] == contraseña:
            nombre = usuario[email]["nombre"]
            del usuario[email]
            print(f"✅ Usuario '{nombre}' eliminado correctamente.")
            guardar_usuarios()
            return True
        else:
            print("❌ Error: La contraseña no es correcta.")
    else:
        print("❌ Error: No se encontró ningún usuario con ese email.")
    return False

# ------------------------------------------
def listar_usuarios():
    if usuario:
        print("\n📋 Lista de usuarios:")
        for email, datos in usuario.items():
            print(f" - {datos['nombre']} ({email}) - Rol: {datos['categoria']}")
    else:
        print("ℹ️ No hay usuarios registrados.")

# ------------------------------------------
def crear_administrador():
    print("\n--- REGISTRO DEL ADMINISTRADOR ---")
    nombre = input("Nombre: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    for datos in usuario.values():
        if datos["categoria"] == "administrador":
            print("❌ Ya existe un administrador registrado.")
            return

    registrar_usuario(nombre, email, contraseña, categoria="administrador")

# ------------------------------------------
if __name__ == "__main__":
    cargar_usuarios()
    crear_administrador()
