# 📚 ABP - Evidencia 03

## 📌 Descripción del Proyecto

Esta evidencia corresponde al segundo entregable del proyecto de Aprendizaje Basado en Proyectos (Reentrega de la evidencia-02). 

Tambien corresponde a la entrega de la evidencia-03 con las correcciones pertinentes mencionadas en la devolucion


## 🧩 Objetivos

- Implementar un sistema de gestión de dispositivos por usuario.
- Permitir el registro seguro de usuarios con validación de datos.
- Asegurar la existencia de **un único administrador**.
- Gestionar automatizaciones predefinidas por usuario/dispositivo.
- Activar/desactivar **programación horaria**.

## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y autenticación.
- ✅ Validación de email (ejemplo@dominio.com) y contraseña segura (mínimo 6 caracteres, mayúscula, símbolo, sin espacios).
- ✅ Registro **único** de administrador al iniciar el sistema.
- ✅ Clasificación de dispositivos por tipo (cámaras de seguridad o sensores de movimiento, momentaneamente trabajamos con estos tipos de dispositivos).
- ✅ Configuración interactiva de automatizaciones por parte del usuario:
  - Horario de encendido y horario de apagado.
  - Ejecutar acción de la automatización: permite visualizar que realmente funciona.
- ✅ Gestión de dispositivos por parte del administrador:
  - Agregar, mostrar, modificar y eliminar dispositivos de cualquier usuario.
- ✅ Visualización de automatizaciones activas en dispositivos de los usuarios por parte del administrador.
- ✅ Almacenamiento de datos en estructuras de datos.

## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y dispositivos.
- ✅ Clasificación de dispositivos por tipo (cámara, sensor).
- ✅ Activación interactiva de la automatización programación horaria por dispositivo.
- ✅ Datos almacenados en diccionarios alojados en memoria.



### Registro de dispositivo y activacion de automatizacion (programación horaria):
```bash
Ingrese el email del usuario al que agregar el dispositivo: nico@hotmail.com
Nombre del dispositivo: camara
1. Cámara de seguridad
2. Sensor de movimiento
Opción: 1
Modelo del dispositivo: C01
✅ Dispositivo 'camara' (cámara de seguridad) agregado correctamente.

📋 Dispositivos disponibles para automatización:
1. camara - Estado actual: False
Seleccione un dispositivo por número: 1
¿Desea activar la automatización horaria? (s/n): s
Ingrese el horario de encendido deseado (HH:MM): 18:30
Ingrese el horario de apagado deseado (HH:MM): 00:30
✅ La automatización para el 'camara' fue configurada correctamente.
```

### Estructura del proyecto:

```
Evidencia-03-Corregido/
├── SRC/
│   ├── usuarios/
│   │   └── usuarios.py
│   ├── dispositivos/
│   │   └── dispositivos.py
│   ├── automatizaciones/
│   │   └── automatizaciones.py
│   └── menus
│       ├── menu_usuario_estandar.py
│       ├── menu_usuario_admin.py
│       └── menu_dispositivos.py
├── router.py
├── app.py
└── README.md
```


## 🧪 Guía para Ejecutar la Aplicación desde Cero

### ✅ 1. Requisitos del sistema

- Python 3.10 o superior
- Sistema operativo: Windows, Linux o MacOS
- Editor de texto (opcional): VS Code, Sublime Text, etc.

### ▶️ 2. Como ejecutar el programa

Desde la terminal o consola:
```bash
cd Evidencia-03-Corregido
python app.py
```

### 🧑‍💻 3. Primer uso - Registro del Administrador

- Se solicita automáticamente registrar al **primer usuario** como **administrador**.

#### Validaciones del registro:
- Email válido
- Contraseña con mínimo 6 caracteres con letras y números.

### 🔑 4. Iniciar sesión

Después del registro:
- Iniciar sesión como administrador
- Registrar usuario estándar

### 🧭 5. Funcionalidades para probar

#### Como Administrador:
- Consultar automatizaciones activas de todos los usuarios
- Gestionar dispositivos: Agregar/mostrar/modificar/eliminar 
- Modificar rol de usuario

#### Como Usuario Estándar:
- Ver sus dispositivos
- Activar y configurar automatización
- Ejecutar acción de la automatización

### ✅ 6. Pruebas recomendadas

- Registrar dispositivo (Admin)
- Configurar automatización programando horarios (Usuario común o estandar)
- Ejecutar acción para revisar que este funcionando la programación horaria (Usuario común o estandar)



## 📄 Evidencia 03
La parte escrita se puede descargar en formato PDF desde el siguiente Link:
[📎 Evidencia PDF](https://drive.google.com/file/d/1bpV9NPMZJu0IPa4T6rpuA-gE6Y6r7RND/view?usp=drive_link)

También se adjuntó el archivo PDF en la entrega a través del aula virtual.
