'''# Ejercicio 1: Se tiene una lista de diccionarios, donde cada diccionario representa un 
# producto con nombre, precio y categoría. Escribe una función procesar_productos 
# que reciba esta lista y una función de operación. Luego, crear distintas funciones para: 
# Filtrar productos de una categoría dada. 
# Calcular el precio promedio de todos los productos.
productos = [
{"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
{"nombre": "Silla", "precio": 150, "categoria": "hogar"},
{"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
{"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
{"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}
]

def filtrar_productos_por_categoría(lista: list, categoria: str)-> list:
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i]["categoria"] == categoria:
            nueva_lista.append(lista[i])
    return nueva_lista

def calcular_precio_promedio(lista: list)-> int:
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]["precio"]
    return suma // len(lista)

def procesar_productos(lista: list, funcion)-> list| int:
    return funcion(lista)

procesar = procesar_productos
promedio = calcular_precio_promedio
categoria = lambda x: filtrar_productos_por_categoría(x, "hogar")

print(procesar(productos, promedio))
print(f"\n\n{procesar(productos, categoria)}")

# Ejercicio 2: Se tiene una lista de diccionarios donde cada diccionario representa un 
# estudiante con su nombre, curso y calificación. Escribe una función 
# procesar_estudiantes que reciba esa lista y una función como parámetro. Luego, implementa: 
# Una función que devuelva solo los estudiantes aprobados (nota mayor o igual a 60). 
# Otra que calcule el promedio de calificaciones de todos los estudiantes.
estudiantes = [
{"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5},
{"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5},
{"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0},
{"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0},
{"nombre": "Martina", "curso": "Física", "calificacion": 6.8}
]
def obtener_aprobados(lista: list)-> list:
    nueva_lista = []
    for i in range(len(lista)):
        if lista[i]["calificacion"] >= 6:
            nueva_lista.append(lista[i])
    return nueva_lista

def calcular_promedio(lista: list)-> list:
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]["calificacion"]
    return int(((suma / len(lista)) * 10)) / 10

def procesar_estudiantes(lista: list, funcion)-> list| int:
    return funcion(lista)

procesar = procesar_estudiantes
aprobados = obtener_aprobados
promedio = calcular_promedio

for i in procesar(estudiantes, aprobados):
    print(("{:^11}|{:^13}|{:^6}").format(i["nombre"],i["curso"],i["calificacion"]))
print(f"\n\nEl promedio de notas es de: {procesar(estudiantes, promedio)}")
'''
# Ejercicio 3: Se tiene una lista de diccionarios donde cada uno representa una película con título, año y puntaje. 
# Escribe una función procesar_peliculas que reciba esa lista y una función como parámetro. Luego, implementa: 
# Una función que devuelva las películas ordenadas por puntaje de mayor a menor. 
# Otra función que ordene las películas por año de estreno de menor a mayor.
peliculas = [
{"titulo": "Inception", "anio": 2010, "puntaje": 8.8},
{"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7},
{"titulo": "Interstellar", "anio": 2014, "puntaje": 8.6},
{"titulo": "Avatar", "anio": 2009, "puntaje": 7.8},
{"titulo": "The Batman", "anio": 2022, "puntaje": 7.9}
]
import copy as c
def peliculas_puntaje_descendente(lista: list)-> list:
    nueva_lista = c.deepcopy(lista)
    for i in range(len(nueva_lista)-1):
        for j in range(i + 1, len(nueva_lista)):
            if nueva_lista[i]["puntaje"] < nueva_lista[j]["puntaje"]:
                contenedor = nueva_lista[i]
                nueva_lista[i] = nueva_lista[j]
                nueva_lista[j] = contenedor
    return nueva_lista

def peliculas_fecha_ascendente(lista: list):
    nueva_lista = c.deepcopy(lista)
    for i in range(len(nueva_lista)-1):
        for j in range(i + 1, len(nueva_lista)):
            if nueva_lista[i]["anio"] > nueva_lista[j]["anio"]:
                contenedor = nueva_lista[i]
                nueva_lista[i] = nueva_lista[j]
                nueva_lista[j] = contenedor
    return nueva_lista

def procesar_peliculas(lista: list, funcion)-> list:
    return funcion(lista)

procesar = procesar_peliculas
puntaje = peliculas_puntaje_descendente
fecha = peliculas_fecha_ascendente
print(("{:^14}|{:^6}|{:^10}").format("película","año","puntaje"))
for i in procesar(peliculas, puntaje):
    print(("{:^14}|{:^6}|{:^10}").format(i["titulo"],i["anio"],i["puntaje"]))
print("\n" + ("{:^14}|{:^6}|{:^10}").format("película","año","puntaje"))
for i in procesar(peliculas, fecha):
    print(("{:^14}|{:^6}|{:^10}").format(i["titulo"],i["anio"],i["puntaje"]))