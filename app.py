import os

def analizar_meta(texto_meta):
    """
    Simulación de lógica de agente: Analiza el texto para categorizarlo.
    """
    # Pasamos el texto a minúsculas para que no importe si escribes con mayúsculas
    texto_min = texto_meta.lower()
    
    # Palabras clave que el "agente" busca para tomar una decisión
    palabras_clave = ["aprender", "estudiar", "programar", "codigo", "ia", "agent"]
    
    # Verificamos si alguna de las palabras clave está en la meta
    if any(palabra in texto_min for palabra in palabras_clave):
        return f"[CATEGORÍA: DESARROLLO] - {texto_meta}"
    else:
        return f"[CATEGORÍA: GENERAL] - {texto_meta}"

def ejecutar_asistente():
    print("=========================================")
    print("🤖 AGENTE DE METAS v2.0 - BUCLE ACTIVO")
    print("👉 Escribe 'salir' para terminar el programa.")
    print("=========================================\n")
    
    # Bucle continuo (Mientras sea Verdadero, no se detiene)
    while True:
        # Escuchar al usuario
        meta = input("Introduce una meta u objetivo -> ").strip()
        
        # Validar la palabra clave para romper el bucle y salir
        if meta.lower() == "salir":
            print("\n👋 Saliendo del programa. ¡Sigue rompiéndola hoy!")
            break
            
        # Si el usuario no escribió nada, ignorar y volver a preguntar
        if not meta:
            continue
            
        # El "agente" procesa y analiza la información
        meta_procesada = analizar_meta(meta)
        
        # Guardar el resultado procesado
        with open("metas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{meta_procesada}\n")
            
        print(f"✅ Procesado y guardado: {meta_procesada}\n")

if __name__ == "__main__":
    ejecutar_asistente()