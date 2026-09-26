# ==============================================================================
# BLOQUE 1: CÓDIGO A INSERTAR EN api_validate.py
# (Copia este bloque y pégalo justo debajo de donde dice CORS(app))
# ==============================================================================

import json
from functools import wraps
from flask import request, jsonify

def cargar_api_keys():
    """Lee el archivo clientes_keys.json del servidor"""
    try:
        with open('clientes_keys.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ADVERTENCIA: No se encontró el archivo clientes_keys.json")
        return {}

def requiere_api_key(f):
    """Decorador que bloquea las peticiones sin API Key válida"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        llave_recibida = request.headers.get('X-API-KEY')
        llaves_validas = cargar_api_keys()
        
        # Validación de seguridad
        if not llave_recibida or llave_recibida not in llaves_validas:
            return jsonify({
                "success": False,
                "error": "Acceso Denegado. API Key inválida o faltante."
            }), 401 
            
        return f(*args, **kwargs)
    return decorated_function


# ==============================================================================
# BLOQUE 2: MODIFICACIÓN DEL ENDPOINT (Ruta)
# (Busca tu ruta actual y añádele el @requiere_api_key así como se muestra abajo)
# ==============================================================================

# Así quedará tu ruta protegida:
@app.route("/api/v1/certificado/validar", methods=["POST"])
@requiere_api_key  # <--- SE AÑADE ESTA LÍNEA EXACTAMENTE AQUÍ
def validar_certificado_api():
    """
    API pública protegida por API Key para validación de certificados por terceros.
    """
    # ... (el resto del código se queda exactamente igual) ...
