# Usar una imagen oficial de Python ligera
FROM python:3.10-slim

# Evitar que Python escriba archivos .pyc en el disco y forzar la salida de logs a la consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear el directorio de la aplicación
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las librerías de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código (api_validate.py)
COPY . .

# Exponer el puerto 5001 para que esté disponible fuera del contenedor
EXPOSE 5001

# Ejecutar la API utilizando Gunicorn (Servidor WSGI para producción) en lugar del servidor de desarrollo de Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "--timeout", "120", "api_validate:app"]
