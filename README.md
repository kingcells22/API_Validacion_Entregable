# API de Validación de Certificados SOFII (Microservicio de Producción)

Microservicio aislado y empaquetado para consultar en línea el estado e información de un certificado digital (`.p12`) emitido por la FII. 

Este repositorio contiene **únicamente** la lógica de validación e intermediación segura con el OCSP, diseñado para ser consumido por terceros.

## 📦 Contenido del Entregable
- `api_validate.py`: Servidor Flask/Gunicorn que actúa como intermediario seguro (API Gateway).
- `Dockerfile`: Script de orquestación para crear la imagen de producción.
- `Documentacion_API_Validacion.md`: Manual de integración para entregar a clientes (XXXX, etc.).
- `Sofii_Validation_API.postman_collection.json`: Colección para pruebas rápidas.

## 🚀 Despliegue en Servidor (Docker)

Esta API está diseñada para correr en contenedores Docker de manera ininterrumpida (`--restart always`).

1. **Construir la imagen:**
   ```bash
   sudo docker build -t sofii-validacion-api:latest .
2. **Levantar el contenedor en producción:**
   ```bash
   sudo docker run -d --name api_validacion_fii --restart always -p 5001:5001 sofii-validacion-api:latest

🔒 Arquitectura de Seguridad
La API no expone las llaves internas de comunicación. Actúa como puente procesando el .p12 recibido por el cliente, extrayendo el serial, consultando el estado al OCSP central de consulta y devolviendo un objeto JSON estructurado.

Se recomienda colocar este contenedor detrás de un Proxy Inverso (ej. Nginx) que maneje SSL (HTTPS) y API Keys para control de acceso por cliente.


