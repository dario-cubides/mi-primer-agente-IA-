import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Cargar la llave oculta desde el .env
load_dotenv()
api_key_secreta = os.getenv("OPENAI_API_KEY")

# 2. Inicializar el cliente de la IA
client = OpenAI(api_key=api_key_secreta)

print("🚀 Enviando pregunta al cerebro de la IA en la nube...")

try:
    # 3. Hacer la petición real a los servidores
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente técnico experto en programación."},
            {"role": "user", "content": "Dame un consejo corto de 2 líneas para un estudiante de desarrollo de software."}
        ]
    )
    
    print("\n🤖 Respuesta de la IA:")
    print(respuesta.choices[0].message.content)

except Exception as e:
    print(f"\n❌ Error en la conexión: {e}")
    print("💡 Nota: Esto es normal si todavía tienes una clave de ejemplo en tu archivo .env.")