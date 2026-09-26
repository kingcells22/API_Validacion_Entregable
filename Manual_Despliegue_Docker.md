# Manual de Despliegue en Producción (Docker) - API de Validación SOFII

Este manual explica cómo poner a correr la API en tu servidor virtual de manera definitiva, asegurando que si el servidor se apaga o se reinicia, la API vuelva a arrancar automáticamente sin intervención humana.

## 1. Preparación de los Archivos
En tu servidor virtual (Linux, preferiblemente), debes crear una carpeta (ej: `/opt/sofii_api_validacion/`) y subir los siguientes 3 archivos a esa carpeta:
- `api_validate.py`
- `requirements.txt`
- `Dockerfile`

---

## 2. Instalación de Docker (Si no lo tienes)
Si tu servidor es Ubuntu/Debian, instala Docker con:
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl enable docker
sudo systemctl start docker
```

---

## 3. Construir la Imagen (Build)
Sitúate dentro de la carpeta donde están tus archivos y ejecuta este comando. Esto descargará Python e instalará todas las dependencias aisladas en la imagen:

```bash
cd /opt/sofii_api_validacion/
sudo docker build -t sofii-validacion-api:latest .
```
*(No olvides el punto `.` al final del comando)*

---

## 4. Levantar el Contenedor (Eternamente)
Para poner a correr la API de fondo y hacer que arranque automáticamente si se reinicia la máquina, usa la bandera `--restart always`:

```bash
sudo docker run -d \
  --name api_validacion_fii \
  --restart always \
  -p 5001:5001 \
  sofii-validacion-api:latest
```

### ¿Qué hace este comando?
- `-d`: Corre en modo "detached" (de fondo), para que puedas cerrar la terminal y siga corriendo.
- `--name`: Le pone un nombre fácil de reconocer al contenedor.
- `--restart always`: **¡ESTA ES LA MAGIA!** Si Docker se reinicia, si el servidor se apaga y prende, o si la app crashea por error, Docker la volverá a levantar automáticamente en milisegundos.
- `-p 5001:5001`: Conecta el puerto 5001 del contenedor con el 5001 de tu servidor real.

---

## 5. Comandos Útiles de Mantenimiento

**Ver si el contenedor está corriendo:**
```bash
sudo docker ps
```

**Ver los logs (ver quién se está conectando o si hay errores):**
```bash
sudo docker logs -f api_validacion_fii
```

**Detener la API:**
```bash
sudo docker stop api_validacion_fii
```

**Reiniciar la API manualmente:**
```bash
sudo docker restart api_validacion_fii
```
