# 1. Importamos la librería oficial para conectar con la IA de Google
from google import genai
import os

def skill_consultar_recursos(tema, entorno_real):
    """
    MÓDULO LÓGICA: Consulta a la IA Real en la nube o usa la base local si estamos simulando.
    """
    if entorno_real:
        try:
            # Inicializamos el cliente usando la API Key que guardamos en el .env
            client = genai.Client(api_key=os.getenv("OPENAI_API_KEY"))
            
            # Cambiamos 'gemini-1.5-flash' por 'gemini-2.5-flash'
            respuesta = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=f"Dame solo una lista de 3 recursos o librerías clave en una sola línea para aprender esto: {tema}",
            )
            return f"🤖 [Gemini AI Real]: {respuesta.text.strip()}"
            
        except Exception as e:
            return f"❌ [Error API] No se pudo conectar con la IA en la nube: {e}"
            
    # Si no hay entorno real, se queda con tu base de datos local que ya funciona
    tema_min = tema.lower()
    if "python" in tema_min or "programar" in tema_min:
        return "👉 [Skill AI Local] Librerías recomendadas: Pandas, Requests, LangChain."
    elif "ia" in tema_min or "agente" in tema_min:
        return "👉 [Skill AI Local] Frameworks recomendados: CrewAI, OpenAI API."
    else:
        return "👉 [Skill AI Local] Recursos: Busca documentación oficial."

def analizar_meta(texto_meta, entorno_real):
    """
    MÓDULO LÓGICA: Sigue clasificando de forma modular.
    """
    texto_min = texto_meta.lower()
    
    palabras_backend = ["ia", "agente", "python", "codigo", "datos", "backend", "seguridad"]
    palabras_frontend = ["interfaz", "pantalla", "diseño", "vista", "frontend", "web", "menu"]
    
    categoria = "[CATEGORÍA: GENERAL]"
    recurso_sugerido = ""
    
    es_backend = any(palabra in texto_min for palabra in palabras_backend)
    es_frontend = any(palabra in texto_min for palabra in palabras_frontend)
    
    if es_backend and es_frontend:
        categoria = "[CATEGORÍA: DESARROLLO FULL-STACK]"
        recurso_sugerido = skill_consultar_recursos(texto_meta, entorno_real)
    elif es_backend:
        categoria = "[CATEGORÍA: DESARROLLO BACKEND / IA]"
        recurso_sugerido = skill_consultar_recursos(texto_meta, entorno_real)
    elif es_frontend:
        categoria = "[CATEGORÍA: DESARROLLO FRONTEND / INTERFAZ]"
        recurso_sugerido = "👉 [Skill UI Local] Tip: Diseña capturas de borde a borde y vistas full-screen limpias."
        
    return categoria, recurso_sugerido