import copy as c
from .ordenamientos import ordenar_por_nombre,ordenar_por_apellido
from .obtener_promedios import obtener_promedio_edad

def listar_ascendente(datos: list)-> list:
    nueva_lista = c.deepcopy(datos)
    for i in range(len(nueva_lista)-1):
        for j in range(i+1,len(nueva_lista)):
            if nueva_lista[i]["apellido"] == nueva_lista[j]["apellido"]:
                ordenar_por_nombre(nueva_lista,i,j)
            elif nueva_lista[i]["apellido"] > nueva_lista[j]["apellido"]:
                ordenar_por_apellido(nueva_lista,i,j)
    return nueva_lista

def listar_datos_jovenes(datos: list)-> list:
    promedio = obtener_promedio_edad(datos)
    nueva_lista = []
    for i in range(len(datos)):
        if datos[i]["edad"] < promedio:
            nueva_lista.append([datos[i]["legajo"],datos[i]["nombre"],datos[i]["apellido"],datos[i]["programa"]["nombre"]])
    return nueva_lista

def listar_datos_por_categorias(datos: list, categoria: str, nombre: str)-> list:
    nueva_lista = []
    if categoria == "programa":
        for i in range(len(datos)):
            if datos[i][categoria]["nombre"] == nombre:
                nueva_lista.append([datos[i]["legajo"],datos[i]["nombre"],datos[i]["apellido"],datos[i]["edad"]])
    else:
        for i in range(len(datos)):
            suma = 0
            if len(datos[i]) == 7:
                for j in range(len(datos[i][categoria])):
                    if datos[i][categoria][j]["nombre"] == nombre:
                        for k in datos[i]["notas"]:
                            suma += k
                        nueva_lista.append([datos[i]["nombre"],datos[i]["apellido"],int(((suma / len(datos[i]["notas"])) * 100)) / 100])
            else:
                pass
    return nueva_lista