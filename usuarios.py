# usuarios.py

# Diccionario para almacenar los usuarios

usuario = {}

def verificar_credenciales(email, contraseña):
    """
    Verifica las credenciales de un usuario.
    Retorna True si son correctas, False en caso contrario.
    """
    if email in usuario and usuario[email]["contraseña"] == contraseña:
        return True
    return False

def iniciar_sesion(email, contraseña):
    """
    Verifica las credenciales de un usuario para iniciar sesión.
    Retorna True si el login es exitoso, False en caso contrario.
    """
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
    """
    Registra un usuario nuevo en el diccionario 'usuarios'.
    La clave será el email, que debe ser único.
    """
    if email in usuario:
        print("Error: Ya existe un usuario con ese email.")
    else:
        usuario[email] = {
            "nombre": nombre,
            "contraseña": contraseña
        }
        print(f"Usuario '{nombre}' registrado correctamente.")

def eliminar_usuario(email, contraseña):
    """
    Elimina un usuario por su email si existe y la contraseña es correcta.
    Retorna True si el usuario fue eliminado, False en caso contrario.
    """
    if email in usuario:
        if usuario[email]["contraseña"] == contraseña:
            nombre = usuario[email]["nombre"]
            usuario.pop(email)
            print(f"Usuario '{nombre}' eliminado correctamente.")
            return True
        else:
            print("Error: La contraseña no es correcta.")
            return False
    else:
        print("Error: No se encontró ningún usuario con ese email.")
        return False

def cambiar_contraseña(email, nueva_contraseña):
    """
    Cambia la contraseña de un usuario existente.
    """
    if email in usuario:
        usuario[email]["contraseña"] = nueva_contraseña
        print("Contraseña cambiada correctamente.")
    else:
        print("Error: No se encontró ningún usuario con ese email.")

def buscar_usuario(email):
    """
    Busca un usuario por su email.
    """
    if email in usuario:
        print(f"Usuario encontrado: {usuario[email]['nombre']} ({email})")
    else:
        print("No se encontró ningún usuario con ese email.")

def listar_usuarios():
    """
    Muestra todos los usuarios registrados.
    """
    if usuario:
        print("\nLista de usuarios:")
        for email, datos in usuario.items():
            print(f" - {datos['nombre']} ({email})")
    else:
        print("No hay usuarios registrados.")