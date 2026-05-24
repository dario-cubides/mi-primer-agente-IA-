import os

def skill_consultar_recursos(tema):
    """
    SKILL: Simula una consulta a una API externa para obtener herramientas recomendadas.
    """
    tema_min = tema.lower()
    
    # Simulación de base de datos o respuestas de una API externa
    if "python" in tema_min or "programar" in tema_min:
        return "👉 [Skill AI] Librerías recomendadas: Pandas, Requests, LangChain."
    elif "ia" in tema_min or "agente" in tema_min or "claude" in tema_min:
        return "👉 [Skill AI] Frameworks recomendados: CrewAI, OpenAI API, HuggingFace."
    elif "github" in tema_min or "git" in tema_min:
        return "👉 [Skill AI] Herramientas recomendadas: GitHub Actions, GitKraken."
    else:
        return "👉 [Skill AI] Recursos: Busca documentación oficial y tutoriales en YouTube."

def analizar_meta(texto_meta):
    """
    CEREBRO DEL AGENTE: Clasifica la meta y decide si activa una habilidad.
    """
    texto_min = texto_meta.lower()
    palabras_clave = ["aprender", "estudiar", "programar", "codigo", "ia", "agent", "github", "git", "python"]
    
    # Inicializamos las variables de lo que va a retornar el análisis
    categoria = "[CATEGORÍA: GENERAL]"
    recurso_sugerido = ""
    
    # Si cumple la condición, el agente cambia su comportamiento
    if any(palabra in texto_min for palabra in palabras_clave):
        categoria = "[CATEGORÍA: DESARROLLO]"
        # ¡ACTIVAMOS LA SKILL! El agente decide usar su herramienta
        recurso_sugerido = skill_consultar_recursos(texto_meta)
        
    return categoria, recurso_sugerido

def ejecutar_asistente():
    print("=========================================")
    print("🤖 AGENTE MULTI-SKILL v3.0 - ACTIVO")
    print("👉 Escribe 'salir' para terminar.")
    print("=========================================\n")
    
    while True:
        meta = input("Introduce una meta u objetivo -> ").strip()
        
        if meta.lower() == "salir":
            print("\n👋 ¡Bucle terminado! No olvides guardar tus cambios en Git.")
            break
            
        if not meta:
            continue
            
        # El cerebro procesa la meta y nos devuelve la categoría y si encontró recursos
        categoria, recurso = analizar_meta(meta)
        
        # Formateamos el texto que se va a guardar y a mostrar
        linea_final = f"{categoria} - {meta}"
        if recurso:
            linea_final += f" | {recurso}"
            
        # Guardar en el archivo
        with open("metas.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{linea_final}\n")
            
        # Mostrar el resultado en pantalla
        print(f"\n✅ Procesado: {categoria} - {meta}")
        if recurso:
            print(f"{recurso}\n")
        print("-" * 40)

if __name__ == "__main__":
    ejecutar_asistente()