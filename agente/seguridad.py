import os
from dotenv import load_dotenv

# Cargamos las variables del archivo oculto .env
load_dotenv()

def verificar_infraestructura():
    """
    MÓDULO SEGURIDAD: Verifica si el entorno es seguro y si las llaves existen.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    
    print("🔍 [Módulo Seguridad] Verificando credenciales de IA...")
    if not api_key or api_key == "tu_clave_secreta_aqui":
        print("⚠️  [ALERTA DE ARQUITECTURA]: No se detectó una API Key real.")
        print("💡 El agente funcionará en modo 'Simulado' para proteger tu bolsillo.")
        return False
    else:
        print("🔒 [Seguro] API Key detectada con éxito en memoria volatil.")
        return True