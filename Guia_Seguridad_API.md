# Guía de Implementación: Seguridad por API Keys (Control de Acceso)

Para proteger la API pública y evitar que cualquier persona en internet consuma los recursos de tu servidor, implementaremos un sistema donde cada cliente debe enviar una llave única para ser autorizado.

## Paso 1: Crear el almacén de credenciales en el Servidor
Por regla general de ciberseguridad, **jamás** se deben dejar las contraseñas escritas directamente en el código de Python. 

En el servidor donde alojes tu API de producción, debes crear un archivo de texto nuevo llamado `clientes_keys.json` (asegúrate de que esté en la misma carpeta donde está tu `api_validate.py`).

El contenido de ese archivo `clientes_keys.json` debe ser así:
```json
{
    "LLAVE_SECRETA_XXXXX_12345": "CLIENTE_XXXXX",
    "LLAVE_SECRETA_YYYYY_67890": "CLIENTE_YYYYY"
}
```
*Cada vez que tengas un cliente o institución nueva (como un Ministerio o Banco), simplemente abres ese archivo en el servidor, agregas su nombre y llave inventada por ti. No tienes que reprogramar el Python ni apagar la API.*

---

## Paso 2: Inyectar el código en tu API

Abre el archivo `logica_seguridad_apikeys.py` que se te entregó junto a este manual. Allí verás el código en Python exacto que hace funcionar esto.

Sigue las instrucciones comentadas en ese archivo:
1. Copia el **BLOQUE 1** y pégalo en la parte superior de tu `api_validate.py` (justo después de `CORS(app)`).
2. Ve a la parte de abajo de tu `api_validate.py`, donde está la línea `@app.route(...)`, y agrégale la línea `@requiere_api_key` exactamente como se muestra en el **BLOQUE 2**.

---

## Paso 3: ¿Qué cambia para los clientes de terceros?
Si agregas este sistema, tu Postman anterior dará error de "Acceso Denegado". Debes avisarle a los desarrolladores de terceros sobre este nuevo requisito.

En la documentación que le entregues a los clientes, deberás indicarles lo siguiente:
> *"Al realizar la petición POST al endpoint de validación, deben incluir obligatoriamente en los **Headers (Cabeceras HTTP)** una variable llamada `X-API-KEY` y colocar como valor la llave secreta que se les fue asignada privadamente."*

En **Postman**, el cliente solo va a la pestaña **Headers**, escribe `X-API-KEY` en la columna *Key*, y su llave secreta (ej. `LLAVE_SECRETA_XXXXX_12345`) en la columna *Value*. Al darle enviar, tu API verificará de forma transparente en el archivo JSON si están autorizados.
