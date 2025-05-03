from listas_personas import *

def listar_datos_de_mexico()->list:
    mexicanos = []
    for i in range(len(country)):
        if country[i] == "Mexico":
            mexicanos += [[nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],edades[i]]]
    return mexicanos

def listar_datos_de_brasil()->list:
    brasileros = []
    for i in range(len(country)):
        if country[i] == "Brazil":
            brasileros += [[nombres[i],telefonos[i],mails[i]]]
    return brasileros

def listar_datos_joven()->list:
    jovenes = []
    menor = 999
    for i in range(len(edades)):
        if edades[i] < menor:
            menor = edades[i]
    for i in range(len(edades)):
        if edades[i] == menor:
            jovenes += [[nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],edades[i]]]
    return jovenes

def determinar_premedio_de_edad()->int:
    suma = 0
    for edad in edades:
        suma += edad
    promedio = suma // len(edades)
    return promedio

def listar_mayor_de_brasil()->list:
    edad_alta = -1
    mayor = []
    for i in range(len(country)):
        if country[i] == "Brazil" and edades[i] > edad_alta:
            edad_alta = edades[i]
    for i in range(len(country)):
        if edades[i] == edad_alta:
            mayor = [nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],edades[i]]
    return mayor

def listar_mexico_brasil_zip8000()->list:
    mbzip8000 = []
    for i in range(len(country)):
        if country[i] == "Mexico" or country[i] == "Brazil":
            if postalZip[i] > 8000:
                mbzip8000 += [[nombres[i],telefonos[i],mails[i],address[i],postalZip[i],region[i],edades[i]]]
    return mbzip8000

def listar_datos_italianos40()->list:
    mayores_italianos = []
    for i in range(len(country)):
        if country[i] == "Italy":
            if edades[i] > 40:
                mayores_italianos += [[nombres[i],telefonos[i],mails[i]]]
    return mayores_italianos

def cerrar_menu()->str:
    seguro = input("¿Está seguro de que desea cerrar el programa?\n(s/n):").lower()
    while seguro != "s" and seguro != "n":
            print("Opción inválida, intente denuevo.\n")
            seguro = input("¿Está seguro de que desea cerrar el programa?\n(s/n):")
    if seguro == "n":
        print("-" * 100)
        return None
    else:
        print("Finalizando programa...")
        return "0"

def listar_mexicanos_ascendente()->list:
    datos = listar_datos_de_mexico()
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            contenedor_datos_i = [datos[i]]
            contenedor_datos_j = [datos[j]]
            if contenedor_datos_i[0] > contenedor_datos_j[0]:
                contenedor_datos = datos[i]
                datos[i] = datos[j]
                datos[j] = contenedor_datos
    return datos

def listar_jovenes_ascendente()->list:
    datos = listar_datos_joven()
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            contenedor_datos_i = datos[i]
            contenedor_datos_j = datos[j]
            if contenedor_datos_i[-1] == contenedor_datos_j[-1]:
                if contenedor_datos_i[0] > contenedor_datos_j[0]:
                    contenedor_datos = datos[i]
                    datos[i] = datos[j]
                    datos[j] = contenedor_datos
            else:
                if contenedor_datos_i[-1] > contenedor_datos_j[-1]:
                    contenedor_datos = datos[i]
                    datos[i] = datos[j]
                    datos[j] = contenedor_datos
    return datos

def listar_ascendente_mexico_brasil_zip8000():
    datos = listar_mexico_brasil_zip8000()
    for i in range(len(datos)-1):
        for j in range(i+1, len(datos)):
            contenedor_datos_i = datos[i]
            contenedor_datos_j = datos[j]
            if contenedor_datos_i[0] == contenedor_datos_j[0]:
                if contenedor_datos_i[-1] > contenedor_datos_j[-1]:
                    contenedor_datos = datos[i]
                    datos[i] = datos[j]
                    datos[j] = contenedor_datos
            else:
                if contenedor_datos_i[0] > contenedor_datos_j[0]:
                    contenedor_datos = datos[i]
                    datos[i] = datos[j]
                    datos[j] = contenedor_datos
    return datos