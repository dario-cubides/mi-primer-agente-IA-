import os
# 1. IMPORTACIÓN MODULAR: Traemos las funciones desde nuestra carpeta 'agente'
from agente.seguridad import verificar_infraestructura
from agente.analizador import analizar_meta

def guardar_meta_en_archivo(categoria, texto_meta, recurso_sugerido):
    """
    Función local para escribir los resultados en el bloc de notas.
    """
    with open("metas.txt", "a", encoding="utf-8") as archivo:
        if recurso_sugerido:
            archivo.write(f"{categoria} - {texto_meta} | 📝 {recurso_sugerido}\n")
        else:
            archivo.write(f"{categoria} - {texto_meta}\n")

def iniciar_agente():
    print("==================================================")
    print("🤖 BIENVENIDO AL ASISTENTE DE METAS MODULAR V2.0 🤖")
    print("==================================================")
    
    # 2. Usamos el módulo de seguridad para validar el entorno
    es_entorno_real = verificar_infraestructura()
    print("==================================================")
    
    while True:
        # Le agregamos .strip() al final del input para limpiar espacios accidentales
        meta = input("\nIntroduce una meta u objetivo (o escribe 'salir') -> ").strip()
        
        if meta.lower() == 'salir':
            print("\n👋 ¡Hasta luego! Sigue adelante con tus objetivos.\n")
            break
            
        if not meta.strip():
            print("⚠️ Por favor, no dejes el espacio en blanco.")
            continue
            
        # 3. Usamos el módulo analizador para procesar la información
        categoria, recurso = analizar_meta(meta, es_entorno_real)
        
        # 4. Guardamos el registro localmente
        guardar_meta_en_archivo(categoria, meta, recurso)
        
        # 5. Mostramos el resultado en la terminal
        print(f"\n✅ Procesado: {categoria} - {meta}")
        if recurso:
            print(f"📌 {recurso}")
        print("-" * 50)

if __name__ == "__main__":
    iniciar_agente()