import json

menu = ("""-----------------------------------
A. Leer archivo JSON.
B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente.
C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
D. Salir
-----------------------------------""")

def leer_json(nombre_archivo: str, lista: str)-> list:
    try:
        with open(nombre_archivo, "r") as archivo:
            data = json.load(archivo)[lista]
    except FileNotFoundError:
        data = "Archivo no encontrado"
    except KeyError:
        data = "Lista no encontrada"
    return data

def generar_csv(nombre_archivo: str, lista: list)-> list:
    if lista == []:
        retorno = False
    else:
        contenido = ""
        for clave in lista[0].keys():
            if contenido:
                contenido += ","
            contenido += clave
        contenido += "\n"
        for heroe in lista:
            linea = ""
            for i, valor in enumerate(heroe.values()):
                if i > 0:
                    linea += ","
                linea += str(valor)
            contenido += linea + "\n"
        retorno = guardar_archivo(nombre_archivo, contenido)
    return retorno

def guardar_archivo(nombre: str, contenido: str):
    try:
        with open(nombre, "w+") as archivo:
            archivo.write(contenido)
        estado = True
    except:
        estado = "error"
    return estado