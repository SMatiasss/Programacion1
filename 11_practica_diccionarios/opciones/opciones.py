from .funciones_internas import *
from datos_y_estructura import comprobar

def ejecutar_opcion_1(datos: list):
    imprimir_4_datos(listar_ascendente(datos),"Edad")

def ejecutar_opcion_2(datos: list):
    imprimir_3_datos(obtener_promedio_lista(datos))

def ejecutar_opcion_3(datos: list):
    imprimir_4_datos(listar_datos_por_categorias(datos,"programa","Ingenieria en Informatica"),"Edad")

def ejecutar_opcion_4(datos: list):
    print("-"* 58 +f"\nPromedio de edad: {obtener_promedio_edad(datos)}")

def ejecutar_opcion_5(datos: list):
    imprimir_3_datos(obtener_mayor_promedio_notas(obtener_promedio_lista(datos)))

def ejecutar_opcion_6(datos: list):
    imprimir_3_datos(listar_datos_por_categorias(datos, "grupos", "Club de Informatica"))

def ejecutar_opcion_7(datos: list):
    imprimir_4_datos(listar_datos_jovenes(datos), "         programa        ")

def finalizar_programa()-> str:
    opcion = input(comprobar)
    while opcion != "s" and opcion != "n":
        opcion = input("Opción inválida, intente denuevo\n" + comprobar)
    return opcion