import json
import os
import re

#En este modulo esta lo siguiente:
# - Cargar y guardar usuarios desde un archivo JSON
# - Verificar credenciales de usuario
# - Iniciar sesión
# - Registrar nuevos usuarios con validaciones nuevas
# - Cambiar contraseña de usuario


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
            return categoria  # 🔧 Retorna la categoría
        else:
            print("❌ Error: Contraseña incorrecta.")
    else:
        print("❌ Error: No existe ningún usuario con ese email.")
    return False

 # funcion de registro de usuario modificada con atributo categoria de usuario y mejora en validaciones de registro
def registrar_usuario(nombre, email, contraseña, categoria):
    categoria = categoria.lower()
    if categoria not in ["administrador", "usuario"]:
        print("❌ Error: Categoría inválida. Debe ser 'administrador' o 'usuario'.")
        return

    # Validar formato email
    patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # ejemplo: abc@gmail.com
    if not re.match(patron_email, email):
        print("❌ Error: Email inválido, debe ser abcd@gmail.com por ejemplo.")
        return
    
    # Exigir mínimo 8 caracteres en contraseña
    if len(contraseña) <= 8:
        print("❌ Error: La contraseña debe tener más de 8 caracteres.")
        return
    
    # Validar que la contraseña tenga mayúscula, número y carácter especial
    patron_contraseña = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+=\[\]{};:\'",.<>?/\\|])\S+$'
    if not re.match(patron_contraseña, contraseña):
        print("❌ Error: La contraseña debe contener al menos una letra mayúscula, un número, un carácter especial y no debe incluir espacios en blanco.")
        return

    # Normalizar nombre a minúsculas para evitar errores en la base de datos
    nombre = nombre.lower()

    if email in usuario:
        print("❌ Error: Ya existe un usuario con ese email.")
    else:
        usuario[email] = {
            "nombre": nombre,
            "contraseña": contraseña,
            "categoria": categoria
        }
        print(f"✅ Usuario '{nombre}' registrado correctamente como {categoria}.")
        guardar_usuarios()

   
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







def listar_usuarios():
    if usuario:
        print("\n📋 Lista de usuarios:")
        for email, datos in usuario.items():
            print(f" - {datos['nombre']} ({email}) - Rol: {datos['categoria']}")
    else:
        print("ℹ️ No hay usuarios registrados.")
