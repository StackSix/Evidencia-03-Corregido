# 📚 ABP - Evidencia 03

## 📌 Descripción del Proyecto

Esta evidencia corresponde al segundo entregable del proyecto de Aprendizaje Basado en Proyectos (Reentrega de la evidencia-02). 

Tambien corresponde a la entrega de la evidencia-03 con las correxiones pertinentes mencionadas en la devolucion


## 🧩 Objetivos

- Implementar un sistema de gestión de dispositivos por usuario.
- Permitir el registro seguro de usuarios con validación de datos.
- Asegurar la existencia de **un único administrador**.
- Gestionar automatizaciones predefinidas por usuario/dispositivo.
- Activar/desactivar el **modo ahorro energético**.
- Guardar la información en archivos `.json` para persistencia de datos.


## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y autenticación.
- ✅ Validación de email y contraseña segura (mínimo 8 caracteres, mayúscula, símbolo, sin espacios).
- ✅ Registro **único** de administrador al iniciar el sistema.
- ✅ Clasificación de dispositivos por tipo (solo cámaras de seguridad momentaneamente trabajamos con un tipo de dispositivo).
- ✅ Configuración de automatizaciones preestablecidas:
  - Encendido/Apagado.
  - Modo de grabación (siempre o por movimiento).
  - Horario de encendido/apagado automático.
  - Activar o desactivar notificaciones.
  - Activar o desactivar detección de movimiento.
  - Modo ahorro (graba 15 segundos y envía notificación cuando detecta movimiento).
  - Activación de modo nocturno silencioso.
- ✅ Gestión de dispositivos por parte del administrador:
  - Agregar, modificar y eliminar dispositivos de cualquier usuario.
- ✅ Visualización de automatizaciones activas en dispositivos de los usuarios por parte del administrador.
- ✅ Configuración interactiva de automatizaciones por parte del usuario.
- ✅ Guardado y carga automática desde archivos `usuarios.json`, `dispositivos.json` y `automatizaciones.json`.


## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y dispositivos.
- ✅ Clasificación de dispositivos por tipo (cámara, sensor, etc.).
- ✅ Activación interactiva del modo ahorro por cámara.
- ✅ Guardado y carga automática desde `usuarios.json` y `dispositivos.json`.



### Registro de dispositivo y activacion de automatizacion (modo de ahorro):
```bash
Ingrese el nombre de dispositivo: camara-patio
Ingrese el modelo de su dispositivo: Tapo C310
✅ Dispositivo 'camara-patio' agregado correctamente..

Seleccione el dispositivo:
1. camara-patio
Seleccione una opción de automatización:
6. Modo ahorro
✅ Automatización actualizada correctamente.
```

### Estructura del proyecto:

```
ABP2/
├── data/
│   ├── usuarios.json
│   ├── dispositivos.json
│   └── automatizaciones.json
├── SRC/
│   ├── usuarios/
│   │   └── usuarios.py
│   ├── dispositivos/
│   │   └── dispositivos.py
│   ├── automatizaciones/
│   │   └── automatizaciones.py
├── router.py
├── app.py
└── README.md
```


## 🧪 Guía para Ejecutar la Aplicación desde Cero

### ✅ 1. Requisitos del sistema

- Python 3.10 o superior
- Sistema operativo: Windows, Linux o MacOS
- Editor de texto (opcional): VS Code, Sublime Text, etc.

### 📁 2. Estructura esperada del proyecto

```
ABP2/
├── SRC/
│   ├── usuarios.py
│   ├── router.py
│   ├── dispositivos/
│   │   ├── dispositivos_modulo.py
│   │   ├── automatizaciones.py
├── data/             # Carpeta creada pero vacia, aca se crearan automaticamente los archivos JSON
├── principal.py
└── README.md
```

### ▶️ 3. Como ejecutar el programa

Desde la terminal o consola:
```bash
cd ABP2
python app.py
```

### 🧑‍💻 4. Primer uso - Registro del Administrador

- Se solicita automáticamente registrar al **primer usuario administrador** y se creara archivo usuarios.JSON.

#### Validaciones del registro:
- Email válido
- Contraseña con mínimo 8 caracteres, al menos una mayúscula, un símbolo y sin espacios

### 🔑 5. Iniciar sesión

Después del registro:
- Iniciar sesión como administrador
- Registrar usuarios estándar

### 🧭 6. Funcionalidades para probar

#### Como Administrador:
- Consultar automatizaciones activas de todos los usuarios
- Agregar/modificar/eliminar dispositivos
- Configurar automatizaciones avanzadas (modo ahorro, programación horaria, etc.)

#### Como Usuario Estándar:
- Ver sus dispositivos
- Configurar reglas de automatización
- Activar modo ahorro o activar modo nocturno

### 💾 7. Archivos creados automáticamente

El sistema genera automáticamente:
```
data/
├── usuarios.json
├── dispositivos.json
├── automatizaciones.json
```
No es necesario crear manualmente estos archivos.

### ✅ 8. Pruebas recomendadas

- Registrar dispositivo
- Configurar modo de grabación
- Programar horarios
- Activar modo ahorro (respetando restricciones)
- Activar modo nocturno (respetando exclusión con modo ahorro) (se agrego datetime para verificar superposicion de hora en automatizacion modo ahorro y activacion nocturna silenciosa.)



## 📄 Evidencia 03
La parte escrita se puede descargar en formato PDF desde el siguiente Link:
[📎 Evidencia PDF](https://drive.google.com/file/d/1K-0RIFLDK6z60dtBWyPIVVxLaynjjlXH/view?usp=sharing)

También se adjuntó el archivo PDF en la entrega a través del aula virtual.
