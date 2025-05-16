# dispositivos.py

# Diccionario para almacenar dispositivos
import usuarios
dispositivos = {}

def registrar_dispositivos(nombre):
    """
    Registra un usuario nuevo en el diccionario 'usuarios'.
    La clave será el email, que debe ser único.
    """
    if dispositivos in usuarios:
        print("Error: Ya existe un usuario con ese email.")
    else:
        usuarios[email] = {
            "nombre": nombre,
            "contraseña": contraseña}
        print(f"Usuario '{nombre}' registrado correctamente.")

def eliminar_usuario(email, contraseña):
    """
    Elimina un usuario por su email si existe.
    """
    if email in usuarios:
        nombre = usuarios.pop(email)
        if contraseña in usuarios:
            nombre = usuarios == (contraseña)
            print(f"Usuario '{nombre}' eliminado correctamente.")
        else:
            print("La contraseña no es correcta")
    else:
        print("Error: No se encontró ningún usuario con ese email.")

def buscar_usuario(email):
    """
    Busca un usuario por su email.
    """
    if email in usuarios:
        print(f"Usuario encontrado: {usuarios[email]} ({email})")
    else:
        print("No se encontró ningún usuario con ese email.")

def listar_usuarios():
    """
    Muestra todos los usuarios registrados.
    """
    if usuarios:
        print("\nLista de usuarios:")
        for email, nombre in usuarios.items():
            print(f" - {nombre} ({email})")
    else:
        print("No hay usuarios registrados.")