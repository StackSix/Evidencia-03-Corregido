# 📚 ABP - Evidencia 03

## 📌 Descripción del Proyecto

Esta evidencia corresponde al segundo entregable del proyecto de Aprendizaje Basado en Proyectos (Reentrega de la evidencia-02). 

Tambien corresponde a la entrega de la evidencia-03 con las correxiones pertinentes mencionadas en la devolucion

---
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

---
## ⚙️ Funcionalidades Principales

- ✅ Registro de usuarios y dispositivos.
- ✅ Clasificación de dispositivos por tipo (cámara, sensor, etc.).
- ✅ Activación interactiva del modo ahorro por cámara.
- ✅ Guardado y carga automática desde `usuarios.json` y `dispositivos.json`.

---

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


### Estructura del proyecto:

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


Evidencia 03
La parte escrita se puede descargar en formato PDF desde el siguiente Link:
https: (aun por definir)
