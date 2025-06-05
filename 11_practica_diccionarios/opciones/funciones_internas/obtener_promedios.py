def obtener_promedio_lista(datos: list)-> list:
    nueva_lista = []
    for i in range(len(datos)):
        suma = 0
        for nota in datos[i]["notas"]:
            suma += nota
        nueva_lista.append([datos[i]["nombre"],datos[i]["apellido"], int(((suma / len(datos[i]["notas"])) * 100)) / 100])
    return nueva_lista

def obtener_promedio_edad(datos: list)-> int:
    suma = 0
    for i in range(len(datos)):
        suma += datos[i]["edad"]
    return suma // len(datos)

def obtener_mayor_promedio_notas(datos: list)-> list:
    lista = [datos[0]]
    maximo = datos[0][2]
    for i in range(1, len(datos)):
        if maximo == datos[i][2]:
            lista.append(datos[i])
        if maximo < datos[i][2]:
            maximo = datos[i][2]
            lista = datos[i]
    return lista