from .funciones import *

def ejecutar_juego(tablero: list, posicion: list, preguntas: list, pregunta: dict, texto: str)-> bool:
    trivia(preguntas, pregunta)
    determinar_victoria_derrota(determinar_movimiento(verificar_respuesta(input("Ingrese su respuesta: ").lower(), pregunta),tablero, posicion))
    return imprimir_fin_o_continuar(posicion[0], preguntas, texto)

def ejecutar_fin_del_juego(nombre: str, puntuacion: int):
    guardar_puntuacion(nombre,puntuacion)