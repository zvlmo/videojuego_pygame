import json

def guardar_configuraciones(configuraciones, archivo):
    # Abre el archivo en modo de escritura
    with open(archivo, "w") as archivo_json:
        # Escribe el diccionario de configuraciones en formato JSON en el archivo
        json.dump(configuraciones, archivo_json)
        print("archivo creado con exito")
# Ejemplo de uso



