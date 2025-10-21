# Trabajo Integrador de Virtualización

Este proyecto forma parte del Trabajo Práctico Integrador de **Arquitectura y Sistemas Operativos (UTN)**.  
El objetivo es desplegar una **API REST simple con FastAPI** dentro de una **máquina virtual Ubuntu Server** configurada en **modo puente (Bridge)** para permitir el acceso desde la red local.

---

## Tecnologías utilizadas
- **Python 3**
- **FastAPI** – Framework para construir APIs rápidas y modernas.
- **Uvicorn** – Servidor ASGI liviano que ejecuta la aplicación.
- **Ubuntu Server 22.04** (dentro de VirtualBox)

---

## Cómo ejecutar la API
1. Activar el entorno virtual (si se creó uno).
2. Ejecutar el servidor con:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
Desde la PC anfitriona, acceder en el navegador a:
```bash
http://<ip_de_la_vm>:8000/
```
## Endpoints
GET /
Devuelve un listado en formato JSON con información sobre los juegos de la saga Dark Souls:

```json
{
  "Dark Souls": {
    "Fecha de lanzamiento": 2011,
    "Plataformas": ["PC", "PS3", "XBOX360"]
  },
  "Dark Souls 2": {
    "Fecha de lanzamiento": 2014,
    "Plataformas": ["PC", "XBOX360", "XBOX ONE", "PS3", "PS4"]
  },
  "Dark Souls 3": {
    "Fecha de lanzamiento": 2016,
    "Plataformas": ["PS4", "PC", "XBOX ONE"]
  }
}
```
## Descripción
Esta API sirve como demostración del funcionamiento de un servidor web dentro de un entorno virtualizado, aplicando conceptos de:

Virtualización (uso de hipervisor tipo 2 con VirtualBox)

Redes (configuración modo puente)

Arquitectura cliente-servidor

Desarrollo backend en Python

## Autores
Agustin Miranda,
Tobias Correa

