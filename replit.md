# Servidor IoT DHT Sensor

## Descripción General
Este proyecto es un servidor Flask que recibe datos de sensores de temperatura y humedad (DHT11/DHT22) desde dispositivos IoT y los almacena en un archivo CSV para análisis posterior.

## Estado del Proyecto
- **Última actualización**: 13 de octubre de 2025
- **Estado**: Totalmente configurado y funcional en Replit
- **Puerto**: 5000
- **Tipo de deployment**: Autoscale (sin estado)

## Estructura del Proyecto

### Archivos Principales
- **`app.py`**: Punto de entrada de la aplicación
- **`server.py`**: Aplicación Flask principal con endpoints
- **`sensor_sim.py`**: Simulador de sensor para pruebas
- **`dht_send.py`**: Cliente para hardware real (Raspberry Pi con sensor DHT)
- **`data.csv`**: Archivo de almacenamiento de datos

### Endpoints Disponibles
- **`GET /`**: Página de inicio con información del servidor
- **`POST /data`**: Recibe datos de sensores (temperatura y humedad)

## Formato de Datos

### Envío de Datos
```json
{
    "temperature": 25.5,
    "humidity": 60.2
}
```

### Almacenamiento CSV
Los datos se guardan con el siguiente formato:
```
timestamp,temperature,humidity
2025-10-13 20:54:40,25.5,60.2
```

## Configuración de Replit

### Variables de Entorno
- `REPLIT_DEV_DOMAIN`: Dominio de desarrollo de Replit (automático)

### Dependencias
- Flask 3.0.0
- requests 2.31.0
- gunicorn 21.2.0 (para producción)

### Workflow
- **Servidor**: `python app.py` (desarrollo)
- **Producción**: `gunicorn --bind=0.0.0.0:5000 --reuse-port server:app`

## Uso

### Modo Desarrollo
El servidor se ejecuta automáticamente en Replit. Puedes:
1. Ver la página de inicio en el navegador web
2. Enviar datos usando el simulador: `python sensor_sim.py`
3. Monitorear los logs del servidor en la consola

### Enviar Datos desde Código
```python
import requests

url = "https://tu-replit-domain.replit.dev/data"
data = {
    "temperature": 25.5,
    "humidity": 60.2
}
response = requests.post(url, json=data)
print(response.json())
```

### Usar con Hardware Real (Raspberry Pi)
1. Conecta el sensor DHT al GPIO 4
2. Actualiza la URL en `dht_send.py` con tu dominio de Replit
3. Ejecuta: `python dht_send.py`

## Características
- ✅ Recepción de datos en tiempo real
- ✅ Almacenamiento en CSV
- ✅ Interfaz web informativa
- ✅ Compatible con sensores DHT11/DHT22
- ✅ Simulador para pruebas
- ✅ Listo para producción con gunicorn

## Arquitectura
El proyecto sigue una arquitectura simple de servidor Flask:
1. Dispositivos IoT envían datos vía POST
2. Flask recibe y valida los datos
3. Los datos se almacenan en CSV con timestamp
4. Respuesta JSON confirma la recepción

## Publicación
El proyecto está configurado para deployment automático con:
- **Tipo**: Autoscale (escalado automático)
- **Servidor**: Gunicorn (producción)
- **Puerto**: 5000
- **Host**: 0.0.0.0

Para publicar, simplemente haz clic en el botón "Publish" en Replit.
