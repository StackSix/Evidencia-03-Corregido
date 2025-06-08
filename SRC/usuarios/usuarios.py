import json
import os
import re
RUTA_USUARIOS = os.path.join("data", "usuarios.json")
usuarios = {}

# Cargar usuarios desde archivo

def cargar_usuarios():
    global usuarios
    if os.path.exists(RUTA_USUARIOS):
        with open(RUTA_USUARIOS, "r") as f:
            usuarios = json.load(f)
    else:
        usuarios = {}

# Guardar usuarios en archivo

def guardar_usuarios():
    with open(RUTA_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

# Registrar usuario estándar o administrador (si no existe aún)

def registrar_usuario(nombre, email, contrasena, rol="usuario"):
    cargar_usuarios()

    # Validar formato de email
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_email, email):
        print("❌ Email inválido. Debe tener formato nombre@dominio.com")
        return

    # Validar contraseña: mínimo 8 caracteres, al menos 1 mayúscula, 1 carácter especial, sin espacios
    if len(contrasena) < 8:
        print("❌ La contraseña debe tener al menos 8 caracteres.")
        return
    if not any(c.isupper() for c in contrasena):
        print("❌ La contraseña debe contener al menos una letra mayúscula.")
        return
    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\~`" for c in contrasena):
        print("❌ La contraseña debe contener al menos un carácter especial.")
        return
    if " " in contrasena:
        print("❌ La contraseña no debe contener espacios.")
        return

    # Verificar duplicado
    if email in usuarios:
        print("❌ Ya existe un usuario con ese email.")
        return

    # Validar único administrador
    if rol == "administrador" and any(u["rol"] == "administrador" for u in usuarios.values()):
        print("❌ Ya existe un administrador registrado.")
        return

    usuarios[email] = {
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": rol
    }
    guardar_usuarios()
    print(f"✅ Usuario '{nombre}' registrado como {rol}.")

# Autenticación

def login(email, contrasena):
    cargar_usuarios()
    if email in usuarios and usuarios[email]["contrasena"] == contrasena:
        return usuarios[email]
    return None

# Obtener rol

def obtener_rol(email):
    return usuarios.get(email, {}).get("rol", "usuario")

# Modificar rol (solo admin)

def modificar_rol(email_objetivo, nuevo_rol, email_actual):
    if usuarios.get(email_actual, {}).get("rol") != "administrador":
        print("❌ Solo el administrador puede cambiar roles.")
        return
    if email_objetivo not in usuarios:
        print("❌ Usuario no encontrado.")
        return
    usuarios[email_objetivo]["rol"] = nuevo_rol
    guardar_usuarios()
    print(f"✅ Rol de {email_objetivo} cambiado a {nuevo_rol}.")




def registrar_admin_unico():
    cargar_usuarios()

    if any(usuario["rol"] == "administrador" for usuario in usuarios.values()):
        return  # Ya hay un admin registrado, no hace nada

    print("🔒 Registro de administrador único")
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()

    # Validar email
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron_email, email):
        print("❌ Email inválido. Debe tener formato nombre@dominio.com")
        return

    intentos = 0
    while intentos < 2:
        contrasena = input("Contraseña: ").strip()

        if len(contrasena) < 8:
            print("❌ La contraseña debe tener al menos 8 caracteres.")
        elif not any(c.isupper() for c in contrasena):
            print("❌ Debe contener al menos una letra mayúscula.")
        elif not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/|\\~`" for c in contrasena):
            print("❌ Debe contener al menos un carácter especial.")
        elif " " in contrasena:
            print("❌ No debe contener espacios.")
        else:
            break  # Contraseña válida

        intentos += 1
        if intentos == 2:
            print("❌ Demasiados intentos fallidos. Registro cancelado.")
            return

    usuarios[email] = {
        "nombre": nombre,
        "contrasena": contrasena,
        "rol": "administrador"
    }

    guardar_usuarios()
    print(f"✅ Administrador '{nombre}' registrado correctamente.")