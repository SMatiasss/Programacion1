def ordenar_por_nombre(datos: list,i: int,j: int):
    if datos[i]["nombre"] > datos[j]["nombre"]:
        contenedor = datos[i]
        datos[i] = datos[j]
        datos[j] = contenedor

def ordenar_por_apellido(datos: list,i: int,j: int):
    contenedor = datos[i]
    datos[i] = datos[j]
    datos[j] = contenedor